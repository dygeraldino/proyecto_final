import pytest
from json_controller import *
from typing import List


#Verificar que se añada un empleado correctamente de json_controller
#Cuando se corre despues de la primera vez toca cambiar el número de cedula porque ese empleado ya existe
#Hay que sumar 1 en el medoto test_total_empleados
def test_add_empleado():
    empleado=Empleado('Juan Perez', 30, 1223456789, 'M', 'Soltero', 5000, 'juan@example.com')
    assert add_empleado(empleado) == True

#Verificar que se añada un cliente correctamente de json_controller
def test_add_cliente():
    cliente= Cliente('Maria Lopez', 25, 987654321, 'F', 'Casada', 'Calle 123', '555-1234', 'maria@example.com', 60, 170)
    #Cedula de empleado ya registrado previamente	
    empleado=1989372798
    assert add_cliente(cliente, empleado) == True

#Verificar que convierta el diccionario cliente en un objeto de clase Cliente sin productos
def test_transform_cliente():
    #Cedula de cliente ya registrado previamente
    cliente=7865432
    cliente_obtenido = transform_cliente(cliente)
    assert cliente_obtenido.cedula == cliente

#Verificar que se añada un producto correctamente de json_controller
def test_add_producto():
    empleado=Empleado('Juan Perez', 30, 123456789, 'M', 'Soltero', 5000, 'juan@example.com')
    #Información de un cliente ya registrado previamente
    cliente= Cliente('Ana Torres Medina', 32, 7865432, 'F', 'Soltera', 'Carrera 15 #30-45', '3101234567', 'anatm@gmail.com', 65.5, 1.7)
    seguro = Seguro(60000, cliente, 'Vida')
    assert add_producto(seguro, empleado.cedula) == True

#Verificar que se tome un empleado correctamende de json_controller
def test_get_empleado():
    #Cedula de empleado ya registrado previamente	
    empleado=1989372798
    empleado_obtenido = get_empleado(empleado)
    assert empleado_obtenido.cedula == empleado

#Verificar que se tome un cliente correctamende de json_controller
@pytest.fixture
def test_get_cliente():
    #cedula de un cliente ya registrado previamente
    cliente=7865432
    cliente_obtenido = get_cliente(cliente)
    assert cliente_obtenido.cedula == cliente

#Verificar que nos de el total de empleados correctamente de json_controller
#Cuando se corre despues de la primera vez toca cambiar el número de cedula porque ese empleado ya existe
#Hay que sumar 1 
def test_total_empleados():
    empleados_totales = total_empleados()
    assert len(empleados_totales) == 8

#Verificar que nos de el total de clientes correctamente de json_controller
def test_total_clientes():
    clientes_totales = total_clientes()
    assert len(clientes_totales) == 20

#Verificar que se añada un correo correctamente de json_controller
def test_add_correo():
    correo_prueba = "correo3@example.com"
    resultado = add_correo(correo_prueba)
    assert resultado is True

#Verificar que se cree un json correctamente de json_controller
def test_create_json():
    name = "test_file"
    create_json(name)
    with open(f'src/data/{name}.json', 'r') as file:
        data = file.read()
    assert data == "{}"

#Crear aseguradora para la prueba   
@pytest.fixture
def aseguradora():
    return Aseguradora("Mi Aseguradora")

#Verificar que se agregue un cliente correctamente de classes
def test_agregar_cliente(aseguradora: Aseguradora):
    cliente = Cliente("Juan Perez", 30, 123456789, "Masculino", "Soltero", "Calle 123", "1234567890", "juan@example.com", 70.5, 1.75)
    aseguradora.clientes.append(cliente)
    assert len(aseguradora.clientes) == 1
    assert aseguradora.clientes[0] == cliente

#Verificar que se agregue un empleado correctamente de classes
def test_agregar_empleado(aseguradora: Aseguradora):
    empleado = Empleado("Ana Lopez", 25, 987654321, "Femenino", "Casada", 2500.0, "ana@example.com")
    aseguradora.empleados.append(empleado)
    assert len(aseguradora.empleados) == 1
    assert aseguradora.empleados[0] == empleado


#Crear empleado para la prueba
@pytest.fixture
def empleado():
    return Empleado("Juan", 30, "123456789", "Masculino", "Soltero", 2000, "juan@example.com")

#Comprobar que se cree un empleado correctamente para la prueba
def test_empleado_instantiation(empleado: Empleado):
    assert empleado.nombre == "Juan"
    assert empleado.edad == 30
    assert empleado.cedula == "123456789"
    assert empleado.genero == "Masculino"
    assert empleado.estado_civil == "Soltero"
    assert empleado.sueldo == 2000
    assert empleado.correo == "juan@example.com"
    assert empleado.clientes == []

#Comprobar que se añada un cliente a un empleado correctamente
def test_add_cliente(empleado: Empleado):
    cliente = Cliente("Ana", 25, "987654321", "Femenino", "Casada", "Calle 123", "555-1234", "ana@example.com", 60, 160)
    empleado.clientes.append(cliente)
    assert len(empleado.clientes) == 1
    assert empleado.clientes[0] == cliente

#Comprobar que nos de la ganancia total corectamente de classes
def test_GananciaTotal(aseguradora: Aseguradora):
    cliente1 = Cliente("Juan", 30, 123456789, "Masculino", "Soltero", "Calle 123", "1234567890", "juan@example.com", 70.5, 1.75)
    cliente2 = Cliente("Maria", 35, 987654321, "Femenino", "Casada", "Avenida 456", "9876543210", "maria@example.com", 65.0, 1.60)
    
    seguro1 = Vida(1000000, cliente1)
    seguro2 = Hogar(2000000, cliente1, "Calle 123", 100.0, 3, 2, 1500000)
    seguro3 = Automovil(3000000, cliente2, "ABC123", "Sedan", "Toyota", "Rojo")
    
    aseguradora.clientes.append(cliente1)
    aseguradora.clientes.append(cliente2)
    
    assert aseguradora.GananciaTotal() == 6000000

#Comprobar que nos de el total asegurado correctamente de classes
def test_TotalAsegurado():
    aseguradora = Aseguradora("Mi Aseguradora")
    
    # Crear clientes de prueba
    cliente1 = Cliente("Juan", 30, 123456789, "M", "Soltero", "Calle 123", "1234567890", "juan@example.com", 70.5, 1.75)
    cliente2 = Cliente("María", 35, 987654321, "F", "Casada", "Calle 456", "0987654321", "maria@example.com", 65.2, 1.68)
    
    # Crear seguros de prueba
    seguro1 = Seguro(1000000, cliente1, "Vida")
    seguro1.valor_asegurado = 500000
    seguro2 = Seguro(2500000, cliente1, "Automovil")
    seguro2.valor_asegurado = 1500000
    seguro3 = Seguro(1500000, cliente2, "Hogar")
    seguro3.valor_asegurado = 1200000
    
    # Agregar clientes a la aseguradora
    aseguradora.clientes.append(cliente1)
    aseguradora.clientes.append(cliente2)
    
    # Calcular el total asegurado
    total_asegurado = aseguradora.TotalAsegurado()
    
    # Verificar que el total asegurado sea el esperado
    assert total_asegurado == 3200000

