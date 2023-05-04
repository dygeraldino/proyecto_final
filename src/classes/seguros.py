from __future__ import annotations
from typing import List, Optional
from abc import ABC, abstractmethod
from persona import Cliente


class Seguro(ABC):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente) -> None:
        self._precio = precio
        self._valor_asegurado = 0
        self._cobertura = cobertura
        self._cliente = cliente

    @property
    def precio(self) -> float:
        return self.__precio

    @precio.setter
    def precio(self, precio: float) -> None:
        self.__precio = precio

    @property
    def valor_asegurado(self) -> float:
        return self.__valor_asegurado

    @valor_asegurado.setter
    def valor_asegurado(self, valor_asegurado: float) -> None:
        self.__valor_asegurado = valor_asegurado

    @property
    def cobertura(self) -> str:
        return self.__cobertura

    @cobertura.setter
    def cobertura(self, cobertura: str) -> None:
        self.__cobertura = cobertura

    @property
    def cliente(self) -> Cliente:
        return self.__cliente


class SOAT(Seguro):
    def __init__(self, cobertura: str, cliente: Cliente, placa: str, modelo: str, marca: str, color: str) -> None:
        super().__init__(501700, cobertura, cliente)
        self.__precio = 501700
        self.__cobertura = cobertura
        self.__cliente = cliente
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__color = color


class Vida(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente):
        super().__init__(precio, cobertura, cliente)
        self.__precio = precio
        self.__cobertura = cobertura
        self.__cliente = cliente


class Hogar(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente, direccion: str, metros_cuadrados: float, numero_habitaciones: int, numero_banos: int, arriendo: float):
        super().__init__(precio, cobertura, cliente)
        self.__precio = precio
        self.__cobertura = cobertura
        self.__cliente = cliente
        self.__direccion = direccion
        self.__metros_cuadrados = metros_cuadrados
        self.__numero_habitaciones = numero_habitaciones
        self.__numero_banos = numero_banos
        self.__arriendo = arriendo


class Automovil(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente, placa: str, modelo: str, marca: str, color: str):
        super().__init__(precio, cobertura, cliente)
        self.__precio = precio
        self.__cobertura = cobertura
        self.__cliente = cliente
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__color = color


class Desempleo(Seguro):
    def __init__(self, precio: float, cobertura: str, cliente: Cliente):
        super().__init__(precio, cobertura, cliente)
        self.__precio = precio
        self.__cobertura = cobertura
        self.__cliente = cliente
