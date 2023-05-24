import tkinter as tk
from classes import *


def abrir_ventana_parametros(tipo_):

    # Crear una nueva ventana
    nueva_ventana = tk.Tk()

    # Función para guardar los datos ingresados y cerrar la ventana
    def guardar_datos():
        # Obtener los valores ingresados por el usuario
        nombre = entry_nombre.get()
        edad = int(entry_edad.get())
        cedula = int(entry_cedula.get())
        genero = entry_genero.get()
        estado_civil = entry_estado_civil.get()
        direccion1 = entry_direccion1.get()
        telefono = entry_telefono.get()
        correo = entry_correo.get()
        peso = float(entry_peso.get())
        estatura = float(entry_estatura.get())

        # Crear objeto Cliente con los datos ingresados
        cliente = Cliente(nombre, edad, cedula, genero, estado_civil,
                          direccion1, telefono, correo, peso, estatura)

        # Dependiendo del tipo de seguro, obtener los valores adicionales
        if tipo_ == "SOAT":
            placa = entry_placa.get()
            modelo = entry_modelo.get()
            marca = entry_marca.get()
            color = entry_color.get()
            seguro = SOAT(cliente, placa, modelo, marca, color)
        elif tipo_ == "Vida":
            precio = float(entry_precio.get())
            seguro = Vida(precio, cliente)
        elif tipo_ == "Hogar":
            precio = float(entry_precio.get())
            direccion = entry_direccion.get()
            metros_cuadrados = float(entry_metros_cuadrados.get())
            numero_habitaciones = int(entry_numero_habitaciones.get())
            numero_banos = int(entry_numero_banos.get())
            valor = float(entry_valor.get())
            seguro = Hogar(precio, cliente, direccion, metros_cuadrados,
                           numero_habitaciones, numero_banos, valor)
        elif tipo_ == "Automovil":
            precio = float(entry_precio.get())
            placa = entry_placa.get()
            modelo = entry_modelo.get()
            marca = entry_marca.get()
            color = entry_color.get()
            seguro = Automovil(precio, cliente, placa, modelo, marca, color)
        elif tipo_ == "Desempleo":
            precio = float(entry_precio.get())
            seguro = Desempleo(precio, cliente)

        # !!! Aqui deberiamos de agregar las funciones que realizan las operaciones con archivos y con objetos del programa

        # Cerrar la nueva ventana
        nueva_ventana.destroy()

    # Etiquetas y cuadros de texto para los datos del cliente
    label_nombre = tk.Label(nueva_ventana, text="Nombre:")
    label_nombre.pack()
    entry_nombre = tk.Entry(nueva_ventana)
    entry_nombre.pack()

    label_edad = tk.Label(nueva_ventana, text="Edad:")
    label_edad.pack()
    entry_edad = tk.Entry(nueva_ventana)
    entry_edad.pack()

    label_cedula = tk.Label(nueva_ventana, text="Cédula:")
    label_cedula.pack()
    entry_cedula = tk.Entry(nueva_ventana)
    entry_cedula.pack()

    label_genero = tk.Label(nueva_ventana, text="Género:")
    label_genero.pack()
    entry_genero = tk.Entry(nueva_ventana)
    entry_genero.pack()

    label_estado_civil = tk.Label(nueva_ventana, text="Estado Civil:")
    label_estado_civil.pack()
    entry_estado_civil = tk.Entry(nueva_ventana)
    entry_estado_civil.pack()

    label_direccion1 = tk.Label(nueva_ventana, text="Dirección:")
    label_direccion1.pack()
    entry_direccion1 = tk.Entry(nueva_ventana)
    entry_direccion1.pack()

    label_telefono = tk.Label(nueva_ventana, text="Teléfono:")
    label_telefono.pack()
    entry_telefono = tk.Entry(nueva_ventana)
    entry_telefono.pack()

    label_correo = tk.Label(nueva_ventana, text="Correo:")
    label_correo.pack()
    entry_correo = tk.Entry(nueva_ventana)
    entry_correo.pack()

    label_peso = tk.Label(nueva_ventana, text="Peso:")
    label_peso.pack()
    entry_peso = tk.Entry(nueva_ventana)
    entry_peso.pack()

    label_estatura = tk.Label(nueva_ventana, text="Estatura:")
    label_estatura.pack()
    entry_estatura = tk.Entry(nueva_ventana)
    entry_estatura.pack()

    # Lógica para mostrar los campos de entrada necesarios para los parámetros del seguro
    if tipo_ == "SOAT":
        label_placa = tk.Label(nueva_ventana, text="Placa:")
        label_placa.pack()
        entry_placa = tk.Entry(nueva_ventana)
        entry_placa.pack()

        label_modelo = tk.Label(nueva_ventana, text="Modelo:")
        label_modelo.pack()
        entry_modelo = tk.Entry(nueva_ventana)
        entry_modelo.pack()

        label_marca = tk.Label(nueva_ventana, text="Marca:")
        label_marca.pack()
        entry_marca = tk.Entry(nueva_ventana)
        entry_marca.pack()

        label_color = tk.Label(nueva_ventana, text="Color:")
        label_color.pack()
        entry_color = tk.Entry(nueva_ventana)
        entry_color.pack()
    elif tipo_ == "Vida":
        label_precio = tk.Label(nueva_ventana, text="Precio:")
        label_precio.pack()
        entry_precio = tk.Entry(nueva_ventana)
        entry_precio.pack()

    elif tipo_ == "Hogar":
        label_precio = tk.Label(nueva_ventana, text="Precio:")
        label_precio.pack()
        entry_precio = tk.Entry(nueva_ventana)
        entry_precio.pack()

        label_direccion = tk.Label(
            nueva_ventana, text="Dirección de la casa:")
        label_direccion.pack()
        entry_direccion = tk.Entry(nueva_ventana)
        entry_direccion.pack()

        label_metros_cuadrados = tk.Label(
            nueva_ventana, text="Metros Cuadrados:")
        label_metros_cuadrados.pack()
        entry_metros_cuadrados = tk.Entry(nueva_ventana)
        entry_metros_cuadrados.pack()

        label_numero_habitaciones = tk.Label(
            nueva_ventana, text="Número de Habitaciones:")
        label_numero_habitaciones.pack()
        entry_numero_habitaciones = tk.Entry(nueva_ventana)
        entry_numero_habitaciones.pack()

        label_numero_banos = tk.Label(nueva_ventana, text="Número de Baños:")
        label_numero_banos.pack()
        entry_numero_banos = tk.Entry(nueva_ventana)
        entry_numero_banos.pack()

        label_valor = tk.Label(nueva_ventana, text="Valor:")
        label_valor.pack()
        entry_valor = tk.Entry(nueva_ventana)
        entry_valor.pack()
    elif tipo_ == "Automovil":
        label_precio = tk.Label(nueva_ventana, text="Precio:")
        label_precio.pack()
        entry_precio = tk.Entry(nueva_ventana)
        entry_precio.pack()

        label_placa = tk.Label(nueva_ventana, text="Placa:")
        label_placa.pack()
        entry_placa = tk.Entry(nueva_ventana)
        entry_placa.pack()

        label_modelo = tk.Label(nueva_ventana, text="Modelo:")
        label_modelo.pack()
        entry_modelo = tk.Entry(nueva_ventana)
        entry_modelo.pack()

        label_marca = tk.Label(nueva_ventana, text="Marca:")
        label_marca.pack()
        entry_marca = tk.Entry(nueva_ventana)
        entry_marca.pack()

        label_color = tk.Label(nueva_ventana, text="Color:")
        label_color.pack()
        entry_color = tk.Entry(nueva_ventana)
        entry_color.pack()
    elif tipo_ == "Desempleo":
        label_precio = tk.Label(nueva_ventana, text="Precio:")
        label_precio.pack()
        entry_precio = tk.Entry(nueva_ventana)
        entry_precio.pack()

    # Botón para guardar los datos ingresados
    boton_guardar = tk.Button(
        nueva_ventana, text="Guardar", command=guardar_datos)
    boton_guardar.pack()
