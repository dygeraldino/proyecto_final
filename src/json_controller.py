from __future__ import annotations
import json
import random
from classes import *


def create_json(name: str) -> dict:
    data = {}
    with open(f'src/data/{name}.json', 'w') as file:
        json.dump(data, file)
        return True


# Agrega empleados a la base de datos
def add_empleado(empleado: Empleado) -> None/bool:
    with open(f'src/data/empleados.json', 'r') as file:
        data = json.load(file)
    if f'{empleado.cedula}' in data:
        print(f"Ya existe un empleado con cedula {empleado.cedula}")
        return False
    else:
        data[f'{empleado.cedula}'] = {
            "nombre": empleado.nombre,
            "edad": empleado.edad,
            "genero": empleado.genero,
            "estado_civil": empleado.estado_civil,
            "sueldo": empleado.sueldo,
            "correo": empleado.correo,
            "comision": empleado.comision,
            "clientes": {},
            "id": empleado.id
        }
        add_correo(data[f'{empleado.cedula}']['correo'])
        with open('src/data/empleados.json', 'w') as file:
            json.dump(data, file)
        return True


def add_correo(correo: str) -> None/bool:
    with open(f'src/data/login.json', 'r') as file:
        data = json.load(file)
    num = random.randint(100000000, 500000000)
    for email in data.keys():
        if data[f'{email}'] == f's{num}_':
            num = random.randint(100000000, 500000000)
    data[correo] = f"s{num}_"
    with open('src/data/login.json', 'w') as file:
        json.dump(data, file)
    return True


# Agrega clientes a la base de datos
def add_cliente(cliente: Cliente, cedula_empleado: int) -> None/bool:
    with open(f'src/data/empleados.json', 'r') as file:
        data = json.load(file)
    with open(f'src/data/clientes.json', 'r') as file1:
        data1 = json.load(file1)
    if f'{cliente.cedula}' in data[f'{cedula_empleado}']['clientes']:
        raise ClienteExistente(
            f"Ya existe un cliente con cedula {cliente.cedula} en la lista de clientes de otro empleado")
    elif f'{cliente.cedula}' in data1:
        raise ClienteExistente(
            f"Ya existe un cliente con cedula {cliente.cedula} en la lista de clientes de otro empleado")
    else:
        data[f'{cedula_empleado}']['clientes'][f'{cliente.cedula}'] = {
            "nombre": cliente.nombre,
            "edad": cliente.edad,
            "genero": cliente.genero,
            "estado_civil": cliente.estado_civil,
            "direccion": cliente.direccion,
            "telefono": cliente.telefono,
            "correo": cliente.correo,
            "peso": cliente.peso,
            "estatura": cliente.estatura,
            "productos": {}
        }
        data1[f'{cliente.cedula}'] = data[f'{cedula_empleado}']['clientes'][f'{cliente.cedula}']
        with open('src/data/empleados.json', 'w') as file:
            json.dump(data, file)
        with open('src/data/clientes.json', 'w') as file1:
            json.dump(data1, file1)
        return True


# Para agregar un producto a un cliente, el cliente debe estar en la base de datos
def add_producto(seguro: Seguro, cedula_empleado: int) -> None/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    if f'{seguro.cliente.cedula}' in data:
        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'] = {
            "precio": seguro.precio,
            "cobertura": seguro.cobertura,
            "valor_asegurado": seguro.valor_asegurado,
            "tipo": seguro.tipo
        }
        if data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'SOAT' or data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'Automovil':
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['placa'] = seguro.placa
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['modelo'] = seguro.modelo
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['marca'] = seguro.marca
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['color'] = seguro.color
        elif data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'Hogar':
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['direccion'] = seguro.direccion
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['metros_cuadrados'] = seguro.metros_cuadrados
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['numero_habitaciones'] = seguro.numero_habitaciones
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['numero_banos'] = seguro.numero_banos
            data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['valor'] = seguro.valor
        with open('src/data/clientes.json', 'w') as file:
            json.dump(data, file)
        with open(f'src/data/empleados.json', 'r') as file1:
            data1 = json.load(file1)
        data1[f'{cedula_empleado}']['clientes'][f'{seguro.cliente.cedula}'] = data[f'{seguro.cliente.cedula}']
        with open('src/data/empleados.json', 'w') as file1:
            json.dump(data1, file1)
        return True


# Convierte el diccionario producto en un objeto de clase Seguro
def get_producto(id: int, cedula_cliente: int) -> Seguro/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    if f'{id}' in data[f'{cedula_cliente}']['productos']:
        if data[f'{cedula_cliente}']['productos'][f'{id}']['tipo'] == 'Vida':
            producto = Vida(data[f'{cedula_cliente}']['productos']
                            [f'{id}']['precio'], transform_cliente(cedula_cliente))
        elif data[f'{cedula_cliente}']['productos'][f'{id}']['tipo'] == 'Automovil':
            producto = Automovil(data[f'{cedula_cliente}']['productos'][f'{id}']['precio'],
                                 transform_cliente(cedula_cliente), data[f'{cedula_cliente}']['productos'][f'{id}']['placa'], data[f'{cedula_cliente}']['productos'][f'{id}']['modelo'], data[f'{cedula_cliente}']['productos'][f'{id}']['marca'], data[f'{cedula_cliente}']['productos'][f'{id}']['color'])
        elif data[f'{cedula_cliente}']['productos'][f'{id}']['tipo'] == 'SOAT':
            producto = SOAT(transform_cliente(cedula_cliente), data[f'{cedula_cliente}']['productos'][f'{id}']['placa'],
                            data[f'{cedula_cliente}']['productos'][f'{id}']['modelo'], data[f'{cedula_cliente}']['productos'][f'{id}']['marca'], data[f'{cedula_cliente}']['productos'][f'{id}']['color'])
        elif data[f'{cedula_cliente}']['productos'][f'{id}']['tipo'] == 'Hogar':
            producto = Hogar(data[f'{cedula_cliente}']['productos'][f'{id}']['precio'],
                             transform_cliente(cedula_cliente), data[f'{cedula_cliente}']['productos'][f'{id}']['direccion'], data[f'{cedula_cliente}']['productos'][f'{id}']['metros_cuadrados'], data[f'{cedula_cliente}']['productos'][f'{id}']['numero_habitaciones'], data[f'{cedula_cliente}']['productos'][f'{id}']['numero_banos'], data[f'{cedula_cliente}']['productos'][f'{id}']['valor'])
        elif data[f'{cedula_cliente}']['productos'][f'{id}']['tipo'] == 'Desempleo':
            producto = Desempleo(data[f'{cedula_cliente}']['productos']
                                 [f'{id}']['precio'], transform_cliente(cedula_cliente))
        producto.valor_asegurado = data[f'{cedula_cliente}']['productos'][f'{id}']['valor_asegurado']
        return producto
    return False


# Convierte el diccionario cliente en un objeto de clase Cliente sin productos
def transform_cliente(cedula: int) -> Cliente/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    if f'{cedula}' in data:
        cliente = Cliente(data[f'{cedula}']['nombre'], data[f'{cedula}']['edad'], cedula, data[f'{cedula}']['genero'], data[f'{cedula}']['estado_civil'],
                          data[f'{cedula}']['direccion'], data[f'{cedula}']['telefono'], data[f'{cedula}']['correo'], data[f'{cedula}']['peso'], data[f'{cedula}']['estatura'])
        cliente.productos = []
        return cliente
    return False


# Retorna el objeto de clase Cliente con sus productos
def get_cliente(cedula: int) -> Cliente/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    cliente = transform_cliente(cedula)
    if f'{cedula}' in data:
        for producto in data[f'{cliente.cedula}']['productos'].keys():
            cliente.productos.append(
                get_producto(int(producto), cliente.cedula))
        for producto in cliente.productos:
            producto.cliente.productos = cliente.productos
        return cliente
    return False

# Retorna el objeto de clase Empleado con sus clientes


def get_empleado(cedula: int) -> Empleado/bool:
    with open(f'src/data/empleados.json', 'r') as file:
        data = json.load(file)
    if f'{cedula}' in data:
        empleado = Empleado(data[f'{cedula}']['nombre'], data[f'{cedula}']['edad'], cedula, data[f'{cedula}']
                            ['genero'], data[f'{cedula}']['estado_civil'], data[f'{cedula}']['sueldo'], data[f'{cedula}']['correo'])
        for cliente in data[f'{cedula}']['clientes'].keys():
            empleado.clientes.append(get_cliente(int(cliente)))
        return empleado
    return False


def total_empleados() -> List["Empleado"]:
    empleados = []
    with open(f'src/data/empleados.json', 'r') as file:
        data = json.load(file)
    for empleado in data.keys():
        empleados.append(get_empleado(int(empleado)))
    return empleados


def total_clientes() -> List["Cliente"]:
    clientes = []
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    for cliente in data.keys():
        clientes.append(get_cliente(int(cliente)))
    return clientes


# Para que los cambios que se hagan sobre los objetos de tipo Persona y Seguro se vean reflejados en el archivo json, se debe usar la funcion changes_client()
def changes_client(clientes: List["Cliente"]) -> None:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    with open(f'src/data/empleados.json', 'r') as file1:
        data1 = json.load(file1)

    for cedula in data.keys():
        for cliente in clientes:
            if f'{cedula}' == f'{cliente.cedula}':
                data[f'{cedula}'] = {
                    "nombre": cliente.nombre,
                    "edad": cliente.edad,
                    "genero": cliente.genero,
                    "estado_civil": cliente.estado_civil,
                    "direccion": cliente.direccion,
                    "telefono": cliente.telefono,
                    "correo": cliente.correo,
                    "peso": cliente.peso,
                    "estatura": cliente.estatura,
                    "productos": {}
                }
                for seguro in cliente.productos:
                    data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'] = {
                        "precio": seguro.precio,
                        "cobertura": seguro.cobertura,
                        "valor_asegurado": seguro.valor_asegurado,
                        "tipo": seguro.tipo
                    }
                    if data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'SOAT' or data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'Automovil':
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['placa'] = seguro.placa
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['modelo'] = seguro.modelo
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['marca'] = seguro.marca
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['color'] = seguro.color
                    elif data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'][f'tipo'] == 'Hogar':
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['direccion'] = seguro.direccion
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['metros_cuadrados'] = seguro.metros_cuadrados
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['numero_habitaciones'] = seguro.numero_habitaciones
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['numero_banos'] = seguro.numero_banos
                        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}']['valor'] = seguro.valor
                for empleado in data1.keys():
                    if f'{cedula}' in data1[f'{empleado}']['clientes']:
                        data1[f'{empleado}']['clientes'][f'{cedula}'] = data[f'{cedula}']
    with open('src/data/clientes.json', 'w') as file:
        json.dump(data, file)
    with open('src/data/empleados.json', 'w') as file1:
        json.dump(data1, file1)
