class Persona:
    def __init__(self, nombre: str, edad: int, cedula: int) -> None:
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula


class Cliente(Persona):
    def __init__(self, nombre: str, edad: int, cedula: int, direccion: str, telefono: str, correo: str, peso: float, estatura: float):
        super().__init__(nombre, edad, cedula)
        self.direccion = direccion
        self.telefono = telefono
        self.correo = correo
        self.peso = peso
        self.estatura = estatura


class Empleado(Persona):
    def __init__(self, nombre: str, edad: int, cedula: int, sueldo: float, comision: float):
        super().__init__(nombre, edad, cedula)
        self.sueldo = sueldo
        self.comision = comision

    @property
    def ganancia(self) -> float:
        return self.sueldo + self.comision

    @property
    def valor_asegurado(self) -> float:
        return 0.0
