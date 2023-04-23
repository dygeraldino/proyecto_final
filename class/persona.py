from seguros import Seguro
class Persona:
    def __init__(self, nombre: str, edad: int, cedula: int,genero: str, estado_civil: str) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        self.genero = genero
        self.estado_civil = estado_civil


class Cliente(Persona):
    def __init__(self, nombre: str, edad: int, cedula: int, direccion: str, telefono: int, correo: str,peso: float, altura: float,producto:list["Seguro"]):
        super().__init__(nombre, edad, cedula)
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.peso=peso
        self.altura=altura
        self.producto=producto


class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, cedula: int, id:int, sueldo: float):
        super().__init__(nombre, edad, cedula)
        self.id=id
        self.sueldo = sueldo

    @property
    def comision(self) -> float:
        pass

    @property
    def valor_asegurado(self) -> float:
        pass
