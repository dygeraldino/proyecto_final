from persona import persona, cliente, empleado
from seguros import SOAT, vida, hogar, seguro, desempleo, automovil

class aseguradora:
    def __init__(self, nombre: str, empleados: list["Empleados"] = []):
        self.empleados = empleados
        self.nombre = nombre

    def calcularGananciaTotal(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.calcularGanancia()
        return total

    def valorAseguradoTotal(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.valorAsegurado()
        return total
    
