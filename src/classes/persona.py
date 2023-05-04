from __future__ import annotations
from typing import Optional, List
from abc import ABC, abstractmethod
from seguros import *


class Persona(ABC):
    def __init__(self, nombre: str, edad: int, cedula: int, genero: str, estado_civil: str) -> None:
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
        self._genero = genero
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

    def agregar_producto(self, producto: Seguro) -> None:
        self.__productos.append(producto)


class Empleado(Persona):
    ID = 1000000

    def __init__(self, nombre: str, edad: int, cedula: int, genero: str, estado_civil: str, sueldo: float):
        super().__init__(nombre, edad, cedula, genero, estado_civil)
        self.__sueldo = sueldo
        self.__comision = 0
        self.__clientes: List["Cliente"] = []
        self.__id = Empleado.ID
        Empleado.ID += 1

    @property
    def clientes(self) -> List["Cliente"]:
        return self.__clientes

    @clientes.setter
    def clientes(self, cliente: Cliente) -> None:
        self.__clientes = cliente

    def agregar_cliente(self, cliente: Cliente) -> None:
        self.__clientes.append(cliente)

    def calcular_comision(self) -> None:
        pass
