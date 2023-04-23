from abc import ABC, abstractmethod
from persona import Persona,Cliente

class Seguro(ABC):
    def __init__(self, mensualidad: float, cobertura: str,valor_asegurado: float,cliente:"Cliente"):
        self.mensualidad = mensualidad
        self.cobertura = cobertura
        self.valor_asegurado = valor_asegurado
        self.cliente=cliente

    @property
    def precio(self) -> float:
        return self._precio

    @property
    def cobertura(self) -> str:
        return self._cobertura

    @abstractmethod
    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        pass


class SOAT(Seguro):
    def __init__(self, mensualidad: float, cobertura: str,valor_asegurado: float,cliente:"Cliente", placa: str, modelo: str, marca: str, color: str) -> None:
        super().__init__(mensualidad, cobertura, valor_asegurado, cliente)
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color

    def calcular_precio(self):
        self.precio = 501700
        return self.precio

    def ingresar_datos(self) -> None:
        self.cobertura = input("Ingrese la cobertura: ")
        self.placa = input("Ingrese la placa del vehículo: ")
        self.modelo = input("Ingrese el modelo del vehículo: ")
        self.marca = input("Ingrese la marca del vehículo: ")
        self.color = input("Ingrese el color del vehículo: ")


class Vida(Seguro):
    def __init__(self, mensualidad: float,valor_asegurado: float,cliente:"Cliente", cobertura: str,beneficiarios:list["Persona"]):
        super().__init__(mensualidad, cobertura, valor_asegurado, cliente)
        self.beneficiarios=beneficiarios

    def calcular_precio(self) -> float:
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        

class Hogar(Seguro):
    def __init__(self, mensualidad: float, cobertura: str,valor_asegurado: float,cliente:"Cliente", direccion: str, area: float, numero_habitaciones: int, lavabo: int, estrato: int):
        super().__init__(mensualidad, cobertura, valor_asegurado, cliente)
        self.direccion = direccion
        self.area =area
        self.numero_habitaciones = numero_habitaciones
        self.labavo = lavabo
        self.estrato=estrato

    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        self.direccion = input("Ingrese la dirección: ")
        self.metros_cuadrados = input("Ingrese los metros cuadrados: ")
        self.numero_habitaciones = input(
            "Ingrese el número de habitaciones: ")
        self.labavo = input("Ingrese el número de baños: ")
        self.estrato = input("Ingrese el estrato: ")


class Automovil(Seguro):
    def __init__(self, mensualidad: float, cobertura: str,valor_asegurado: float,cliente:"Cliente", placa: str, modelo: str, marca: str, color: str):
        super().__init__(mensualidad, cobertura, valor_asegurado, cliente)
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color

    def calcular_precio(self) -> float:
        pass

    def ingresar_datos(self) -> None:
        self.cobertura = input("Ingrese la cobertura: ")
        self.placa = input("Ingrese la placa del vehículo: ")
        self.modelo = input("Ingrese el modelo del vehículo: ")
        self.marca = input("Ingrese la marca del vehículo: ")
        self.color = input("Ingrese el color del vehículo: ")


class Desempleo(Seguro):
    def __init__(self, mensualidad: float, cobertura: str,valor_asegurado: float,cliente:"Cliente",profesion:str,lugar_trabajo:str,sueldo:float):
        super().__init__(mensualidad, cobertura, valor_asegurado, cliente)
        self.profesion=profesion
        self.lugar_trabajo=lugar_trabajo
        self.sueldo=sueldo
   
    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        self.profesion= input ("Ingrese su profesion")
        self.lugar_trabajo= input("Ingrese su lugar de trabajo")
        self.suedo= input("Ingrese su sueldo")

