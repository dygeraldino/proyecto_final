from __future__ import annotations
from typing import Optional, List
from persona import *


class Aseguradora:
    def __init__(self, nombre: str):
        self.__clientes: List["Cliente"] = []
        self.__empleados: List["Empleado"] = []
        self.nombre = nombre
        self.__id = 9789334298

    def GananciaTotal(self) -> float:
        pass

    def TotalAsegurado(self) -> float:
        pass
