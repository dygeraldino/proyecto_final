from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
import random
import json

with open(f'src/data/empleados.json', 'r') as file:
    data = json.load(file)


class Aseguradora:
    def __init__(self, nombre: str):
        self.__clientes: List["Cliente"] = []
        self.__empleados: List["Empleado"] = []
        self.nombre = nombre
        self.__id = 9789334298

    @property
    def clientes(self) -> List["Cliente"]:
        return self.__clientes

    @clientes.setter
    def clientes(self, cliente: Cliente) -> None:
        self.__clientes = cliente

    @property
    def empleados(self) -> List["Empleado"]:
        return self.__empleados

    @empleados.setter
    def empleados(self, empleado: Empleado) -> None:
        self.__empleados = empleado

    def GananciaTotal(self) -> float:
        for cliente in self.clientes:
            for producto in cliente.productos:
                total += producto.precio
        return total

    def TotalAsegurado(self) -> float:
        # sumatoria de el valor asegurado de todos los seguros de todos los clientes
        for cliente in self.clientes:
            for producto in cliente.productos:
                total += producto.valor_asegurado
        return total


class Persona(ABC):
    def __init__(self, nombre: str, edad: int, cedula: int, genero: str, estado_civil: str) -> None:
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
        self._genero = genero
        self._estado_civil = estado_civil

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre: str) -> None:
        self._nombre = nombre

    @property
    def edad(self) -> int:
        return self._edad

    @edad.setter
    def edad(self, edad: int) -> None:
        self._edad = edad

    @property
    def cedula(self) -> int:
        return self._cedula

    @cedula.setter
    def cedula(self, cedula: int) -> None:
        self._cedula = cedula

    @property
    def genero(self) -> str:
        return self._genero

    @genero.setter
    def genero(self, genero: str) -> None:
        self._genero = genero

    @property
    def estado_civil(self) -> str:
        return self._estado_civil

    @estado_civil.setter
    def estado_civil(self, estado_civil: str) -> None:
        self._estado_civil = estado_civil


class Cliente(Persona):
    def __init__(self, nombre: str, edad: int, cedula: int, genero: str, estado_civil: str, direccion: str, telefono: str, correo: str, peso: float, estatura: float):
        super().__init__(nombre, edad, cedula, genero, estado_civil)
        self.__direccion = direccion
        self.__telefono = telefono
        self.__correo = correo
        self.__peso = peso
        self.__estatura = estatura
        self.__productos: List["Seguro"] = []

    @property
    def direccion(self) -> str:
        return self.__direccion

    @property
    def telefono(self) -> str:
        return self.__telefono

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def peso(self) -> str:
        return self.__peso

    @property
    def estatura(self) -> str:
        return self.__estatura

    def agregar_producto(self, producto: Seguro) -> None:
        self.__productos.append(producto)


class Empleado(Persona):
    ID = 1000006

    def __init__(self, nombre: str, edad: int, cedula: int, genero: str, estado_civil: str, sueldo: float, correo: str):
        super().__init__(nombre, edad, cedula, genero, estado_civil)
        self.__sueldo = sueldo
        self.__comision = 0
        self.__correo = correo
        self.__clientes: List["Cliente"] = []
        self.__id = Empleado.ID
        Empleado.ID += 1
        for empleado in data.keys():
            if data[f'{empleado}']['id'] == self.__id:
                self.__id = Empleado.ID
                Empleado.ID += 1

    @property
    def sueldo(self) -> float:
        return self.__sueldo

    @sueldo.setter
    def sueldo(self, sueldo: float) -> None:
        self.__sueldo = sueldo

    @property
    def comision(self) -> float:
        return self.__comision

    @comision.setter
    def comision(self, comision: float) -> None:
        self.__comision = comision

    @property
    def correo(self) -> str:
        return self.__correo

    @property
    def clientes(self) -> List["Cliente"]:
        return self.__clientes

    @clientes.setter
    def clientes(self, cliente: Cliente) -> None:
        self.__clientes = cliente

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    def calcular_comision(self) -> None:
        comision = 0
        for cliente in self.clientes:
            for producto in cliente.__productos:
                if producto.precio <= 3000000 or producto.precio >= 1000000:
                    comision += producto.precio*0.05
                else:
                    comision += producto.precio*0.05 + \
                        ((1000000 - producto.precio)//100000)*0.005
                    comision += producto.precio*0.05 + ((1000000 - producto.precio)//100000)*0.005
        self.__comision = comision


class Seguro(ABC):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente, tipo: str) -> None:
        self._precio = precio
        self._valor_asegurado = 0
        self._cobertura = cobertura
        self._cliente = cliente
        cliente.agregar_producto(self)
        self._tipo = tipo
        self._id = 100*random.randint(0, 99)+100000*random.randint(0, 99)

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, precio: float) -> None:
        self._precio = precio

    @property
    def valor_asegurado(self) -> float:
        return self._valor_asegurado

    @valor_asegurado.setter
    def valor_asegurado(self, valor_asegurado: float) -> None:
        self._valor_asegurado = valor_asegurado

    @property
    def cobertura(self) -> str:
        return self._cobertura

    @cobertura.setter
    def cobertura(self, cobertura: str) -> None:
        self._cobertura = cobertura

    @property
    def cliente(self) -> Cliente:
        return self._cliente

    @cliente.setter
    def cliente(self, cliente: Cliente) -> None:
        self._cliente = cliente

    @property
    def id(self) -> int:
        return self._id

    @property
    def tipo(self) -> str:
        return self._tipo

    @tipo.setter
    def tipo(self, tipo: str) -> None:
        self._tipo = tipo


class SOAT(Seguro):
    def __init__(self, cobertura: str, cliente: Cliente, placa: str, modelo: str, marca: str, color: str) -> None:
        super().__init__(501700, cobertura, cliente, "SOAT")
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__color = color

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: str) -> None:
        self.__placa = placa

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self.__modelo = modelo

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color


class Vida(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente):
        super().__init__(precio, cobertura, cliente, "Vida")


class Hogar(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente, direccion: str, metros_cuadrados: float, numero_habitaciones: int, numero_banos: int, valor: float):
        super().__init__(precio, cobertura, cliente, "Hogar")
        self.__direccion = direccion
        self.__metros_cuadrados = metros_cuadrados
        self.__numero_habitaciones = numero_habitaciones
        self.__numero_banos = numero_banos
        self.__valor = valor

    @property
    def direccion(self) -> str:
        return self.__direccion

    @direccion.setter
    def direccion(self, direccion: str) -> None:
        self.__direccion = direccion

    @property
    def metros_cuadrados(self) -> float:
        return self.__metros_cuadrados

    @metros_cuadrados.setter
    def metros_cuadrados(self, metros_cuadrados: float) -> None:
        self.__metros_cuadrados = metros_cuadrados

    @property
    def numero_habitaciones(self) -> int:
        return self.__numero_habitaciones

    @numero_habitaciones.setter
    def numero_habitaciones(self, numero_habitaciones: int) -> None:
        self.__numero_habitaciones = numero_habitaciones

    @property
    def numero_banos(self) -> int:
        return self.__numero_banos

    @numero_banos.setter
    def numero_banos(self, numero_banos: int) -> None:
        self.__numero_banos = numero_banos

    @property
    def valor(self) -> float:
        return self.__valor

    @valor.setter
    def valor(self, valor: float) -> None:
        self.__valor = valor


class Automovil(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente, placa: str, modelo: str, marca: str, color: str):
        super().__init__(precio, cobertura, cliente, "Automovil")
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__color = color

    @property
    def placa(self) -> str:
        return self.__placa

    @placa.setter
    def placa(self, placa: str) -> None:
        self.__placa = placa

    @property
    def marca(self) -> str:
        return self.__marca

    @marca.setter
    def marca(self, marca: str) -> None:
        self.__marca = marca

    @property
    def modelo(self) -> str:
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo: str) -> None:
        self.__modelo = modelo

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, color: str) -> None:
        self.__color = color


class Desempleo(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente):
        super().__init__(precio, cobertura, cliente, "Desempleo")
