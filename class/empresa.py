from persona import Empleado


class Aseguradora:
    def __init__(self, nombre: str, empleados: list["Empleado"] = None):
        if empleados is None:
            empleados = []
        self.empleados = empleados
        self.nombre = nombre

    def calcularGananciaTotal(self) -> float:
        total = 0
        for empleado in self.empleados:
            total += empleado.calcularGanancia()
        return total

    def valorAseguradoTotal(self) -> float:
        total = 0
        for empleado in self.empleados:
            total += empleado.valorAsegurado()
        return total
