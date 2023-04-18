from abc import ABC, abstractmethod


class Seguro(ABC):
    def __init__(self, precio: float, cobertura: str):
        self.precio = precio
        self.cobertura = cobertura

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
    def __init__(self, precio: float, cobertura: str, placa: str, modelo: str, marca: str, color: str) -> None:
        super().__init__(precio, cobertura)
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
    def __init__(self, precio: float, cobertura: str, edad: int, sexo: str, estado_civil: str):
        super().__init__(precio, cobertura)
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

    def calcular_precio(self) -> float:
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        self.edad = input("Ingrese su edad: ")
        self.sexo = input("Ingrese su sexo: ")
        self.estado_civil = input("Ingrese su estado civil: ")


class Hogar(Seguro):
    def __init__(self, precio: float, cobertura: str, direccion: str, metros_cuadrados: float, numero_habitaciones: int, numero_banos: int, arriendo: float):
        super().__init__(precio, cobertura)
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.numero_habitaciones = numero_habitaciones
        self.numero_banos = numero_banos
        self.arriendo = arriendo

    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        self.direccion = input("Ingrese la dirección: ")
        self.metros_cuadrados = input("Ingrese los metros cuadrados: ")
        self.numero_habitaciones = input(
            "Ingrese el número de habitaciones: ")
        self.numero_banos = input("Ingrese el número de baños: ")
        self.arriendo = input("Ingrese el arriendo (en pesos): ")


class Automovil(Seguro):
    def __init__(self, precio: float, cobertura: str, placa: str, modelo: str, marca: str, color: str):
        super().__init__(precio, cobertura)
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
    def __init__(self, precio, cobertura, edad, sexo, estado_civil):
        super().__init__(precio, cobertura)
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        self.cobertura = input("Ingrese la cobertura: ")
        self.edad = input("Ingrese su edad: ")
        self.sexo = input("Ingrese su sexo: ")
        self.estado_civil = input("Ingrese su estado civil: ")
