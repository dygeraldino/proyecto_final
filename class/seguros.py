from abc import ABC, abstractmethod

class seguro(ABC.abc):
    def __init__(self, precio, cobertura):
        self.precio = precio
        self.cobertura = cobertura

    @abstractmethod
    def calcular_precio(self):
        pass   
    
    def ingresar_datos(self):
        pass

class SOAT(seguro):
    def __init__(self, precio, cobertura, placa, modelo, marca, color):
        super().__init__(precio, cobertura)
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color
    
    def calcular_precio(self):
        SOAT.precio = 501.700
        pass

    def ingresar_datos(self):
        SOAT.cobertura = input("Ingrese la cobertura: ")
        SOAT.placa = input("Ingrese la placa del vehículo: ")
        SOAT.modelo = input("Ingrese el modelo del vehículo: ")
        SOAT.marca = input("Ingrese la marca del vehículo: ")
        SOAT.color = input("Ingrese el color del vehículo: ")
        pass


class vida(seguro):
    def __init__(self, precio, cobertura, edad, sexo, estado_civil):
        super().__init__()
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

    def calcular_precio(self):
        pass
    
    def ingresar_datos(self):
        vida.cobertura = input("Ingrese la cobertura: ")
        vida.edad = input("Ingrese su edad: ")
        vida.sexo = input("Ingrese su sexo: ")
        vida.estado_civil = input("Ingrese su estado civil: ")
        

class hogar(seguro):
    def __init__(self, precio, cobertura, direccion, metros_cuadrados, numero_habitaciones, numero_banos, arriendo):
        super().__init__()
        self.direccion = direccion
        self.metros_cuadrados = metros_cuadrados
        self.numero_habitaciones = numero_habitaciones
        self.numero_banos = numero_banos
        self.arriendo = arriendo

    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        hogar.cobertura = input("Ingrese la cobertura: ")
        hogar.direccion = input("Ingrese la dirección: ")
        hogar.metros_cuadrados = input("Ingrese los metros cuadrados: ")
        hogar.numero_habitaciones = input("Ingrese el número de habitaciones: ")
        hogar.numero_banos = input("Ingrese el número de baños: ")
        hogar.arriendo = input("Ingrese el arriendo (en pesos): ")


class automovil(seguro):
    def __init__(self, precio, cobertura, placa, modelo, marca, color):
        super().__init__()
        self.placa = placa
        self.modelo = modelo
        self.marca = marca
        self.color = color
    
    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        automovil.cobertura = input("Ingrese la cobertura: ")
        automovil.placa = input("Ingrese la placa del vehículo: ")
        automovil.modelo = input("Ingrese el modelo del vehículo: ")
        automovil.marca = input("Ingrese la marca del vehículo: ")
        automovil.color = input("Ingrese el color del vehículo: ")

class desempleo(seguro):
    def __init__(self, precio, cobertura, edad, sexo, estado_civil):
        super().__init__()
        self.edad = edad
        self.sexo = sexo
        self.estado_civil = estado_civil

    def calcular_precio(self):
        pass

    def ingresar_datos(self):
        desempleo.cobertura = input("Ingrese la cobertura: ")
        desempleo.edad = input("Ingrese su edad: ")
        desempleo.sexo = input("Ingrese su sexo: ")
        desempleo.estado_civil = input("Ingrese su estado civil: ")