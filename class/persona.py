class persona:
    def __init__(self, nombre, edad, cedula):
        self.nombre = nombre
        self.edad = edad
        self.cedula = cedula
        

class cliente(persona):
    def __init__(self, nombre, edad, cedula, direccion, telefono, correo, peso, estatura):
        super().__init__(nombre, edad, cedula)
        self.direccion = direccion     
        self.telefono = telefono
        self.correo = correo
        self.peso = peso
        self.estatura = estatura
    
class vendedor(persona):
    def __init__(self, nombre, edad, cedula, sueldo, comision):
        super().__init__(nombre, edad, cedula)
        self.sueldo = sueldo
        self.comision = comision
    
    

