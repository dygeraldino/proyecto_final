from __future__ import annotations
import json
import random
from classes import *


def create_json(name: str) -> dict:
    data = {}
    with open(f'src/data/{name}.json', 'w') as file:
        json.dump(data, file)
        return True


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
    data[correo] = f"s{num}_"
    with open('src/data/login.json', 'w') as file:
        json.dump(data, file)
    return True


def add_cliente(cliente: Cliente, cedula_empleado: int) -> None:
    with open(f'src/data/empleados.json', 'r') as file:
        data = json.load(file)
    with open(f'src/data/clientes.json', 'r') as file1:
        data1 = json.load(file1)
    if f'{cliente.cedula}' in data[f'{cedula_empleado}']['clientes']:
        print(f"Ya existe un cliente con cedula {cliente.cedula}")
        return False
    elif f'{cliente.cedula}' in data1:
        print(
            f"Ya existe un cliente con cedula {cliente.cedula} en la base de datos, agregue el producto al cliente")
        return False
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


def add_producto(seguro: Seguro, cedula_empleado: int) -> None/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    if f'{seguro.cliente.cedula}' in data:
        data[f'{seguro.cliente.cedula}']['productos'][f'{seguro.id}'] = {
            "precio": seguro.precio,
            "cobertura": seguro.cobertura
        }
        with open('src/data/clientes.json', 'w') as file:
            json.dump(data, file)
        with open(f'src/data/empleados.json', 'r') as file1:
            data1 = json.load(file1)
        data1[f'{cedula_empleado}']['clientes'][f'{seguro.cliente.cedula}'] = data[f'{seguro.cliente.cedula}']
        with open('src/data/empleados.json', 'w') as file1:
            json.dump(data1, file1)
        return True


# Convierte el diccionario cliente en un objeto de clase Cliente
def get_cliente(cedula: int) -> Cliente/bool:
    with open(f'src/data/clientes.json', 'r') as file:
        data = json.load(file)
    if f'{cedula}' in data:
        cliente = Cliente(data[f'{cedula}']['nombre'], data[f'{cedula}']['edad'], cedula, data[f'{cedula}']['genero'], data[f'{cedula}']['estado_civil'],
                          data[f'{cedula}']['direccion'], data[f'{cedula}']['telefono'], data[f'{cedula}']['correo'], data[f'{cedula}']['peso'], data[f'{cedula}']['estatura'])
        cliente.productos = data[f'{cedula}']['productos']
        return cliente
