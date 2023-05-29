import tkinter as tk
from tkinter import ttk, messagebox
from classes import *
from json_controller import *
import util.generic as utl


def volver(nueva_ventana, email_empleado):
    nueva_ventana.destroy()
    from seguros import Interfaz_seguros
    inter = Interfaz_seguros(email_empleado)


def abrir_ventana_parametros(tipo_, email_empleado):

    # Crear una nueva ventana
    nueva_ventana = tk.Tk()
    nueva_ventana.title(f'Seguro de {tipo_}')
    nueva_ventana.geometry('1050x500')
    nueva_ventana.config(bg='#E6F0FF')
    nueva_ventana.resizable(width=0, height=0)
    utl.centrar_ventana(nueva_ventana, 1050, 500)

    label_titulo = tk.Label(nueva_ventana, text=f"Ingreso de datos del cliente ({tipo_}): ", font=(
        'Times', 18), fg="#000000", bg='#E6F0FF')
    label_titulo.grid(row=0, column=0, columnspan=2, pady=10)

    # Función para guardar los datos ingresados y cerrar la ventana
    def guardar_datos(tipo_):
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
        valor_asegurado = float(entry_valor_asegurado.get())

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

        cliente.productos.append(seguro)
        empleados = total_empleados()
        for empleado in empleados:
            if empleado.correo == email_empleado:
                empleado_cedula = empleado.cedula
        try:
            add_cliente(cliente, empleado_cedula)
            add_producto(seguro, empleado_cedula)
            messagebox.showinfo(message="Cliente agregado exitosamente",
                                title="Cliente")
        except ClienteException as ex:
            messagebox.showerror(
                message=f"{ex.__class__.__name__}: {ex}", title="Error")

    # Etiquetas y cuadros de texto para los datos del cliente
    label_nombre = tk.Label(nueva_ventana, text="Nombre:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_nombre.grid(row=1, column=1, sticky="e")
    entry_nombre = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_nombre.grid(row=1, column=2)

    label_edad = tk.Label(nueva_ventana, text="Edad:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_edad.grid(row=2, column=1, sticky="e")
    entry_edad = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_edad.grid(row=2, column=2)

    label_cedula = tk.Label(nueva_ventana, text="Cédula:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_cedula.grid(row=3, column=1, sticky="e")
    entry_cedula = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_cedula.grid(row=3, column=2)

    label_genero = tk.Label(nueva_ventana, text="Género:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_genero.grid(row=4, column=1, sticky="e")
    entry_genero = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_genero.grid(row=4, column=2)

    label_estado_civil = tk.Label(nueva_ventana, text="Estado Civil:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_estado_civil.grid(row=5, column=1, sticky="e")
    entry_estado_civil = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_estado_civil.grid(row=5, column=2)

    label_direccion1 = tk.Label(nueva_ventana, text="Dirección:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_direccion1.grid(row=6, column=1, sticky="e")
    entry_direccion1 = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_direccion1.grid(row=6, column=2)

    label_telefono = tk.Label(nueva_ventana, text="Teléfono:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_telefono.grid(row=7, column=1, sticky="e")
    entry_telefono = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_telefono.grid(row=7, column=2)

    label_correo = tk.Label(nueva_ventana, text="Correo:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_correo.grid(row=8, column=1, sticky="e")
    entry_correo = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_correo.grid(row=8, column=2)

    label_peso = tk.Label(nueva_ventana, text="Peso:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_peso.grid(row=9, column=1, sticky="e")
    entry_peso = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_peso.grid(row=9, column=2)

    label_estatura = tk.Label(nueva_ventana, text="Estatura:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_estatura.grid(row=10, column=1, sticky="e")
    entry_estatura = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_estatura.grid(row=10, column=2)

    # Lógica para mostrar los campos de entrada necesarios para los parámetros del seguro
    if tipo_ == "SOAT":
        label_placa = tk.Label(nueva_ventana, text="Placa:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_placa.grid(row=1, column=3, sticky="e")
        entry_placa = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_placa.grid(row=1, column=4)

        label_modelo = tk.Label(nueva_ventana, text="Modelo:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_modelo.grid(row=2, column=3, sticky="e")
        entry_modelo = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_modelo.grid(row=2, column=4)

        label_marca = tk.Label(nueva_ventana, text="Marca:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_marca.grid(row=3, column=3, sticky="e")
        entry_marca = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_marca.grid(row=3, column=4)

        label_color = tk.Label(nueva_ventana, text="Color:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_color.grid(row=4, column=3, sticky="e")
        entry_color = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_color.grid(row=4, column=4)
    elif tipo_ == "Vida":
        label_precio = tk.Label(nueva_ventana, text="Precio:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_precio.grid(row=1, column=3, sticky="e")
        entry_precio = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_precio.grid(row=1, column=4)

    elif tipo_ == "Hogar":
        label_precio = tk.Label(nueva_ventana, text="Precio:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_precio.grid(row=1, column=3, sticky="e")
        entry_precio = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_precio.grid(row=1, column=4)

        label_direccion = tk.Label(
            nueva_ventana, text="Dirección de la casa:", font=(
                'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_direccion.grid(row=2, column=3, sticky="e")
        entry_direccion = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_direccion.grid(row=2, column=4)

        label_metros_cuadrados = tk.Label(
            nueva_ventana, text="Metros Cuadrados:", font=(
                'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_metros_cuadrados.grid(row=3, column=3, sticky="e")
        entry_metros_cuadrados = tk.Entry(
            nueva_ventana, font=('Times', 12), width=30)
        entry_metros_cuadrados.grid(row=3, column=4)

        label_numero_habitaciones = tk.Label(
            nueva_ventana, text="Número de Habitaciones:", font=(
                'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_numero_habitaciones.grid(row=4, column=3, sticky="e")
        entry_numero_habitaciones = tk.Entry(
            nueva_ventana, font=('Times', 12), width=30)
        entry_numero_habitaciones.grid(row=4, column=4)

        label_numero_banos = tk.Label(nueva_ventana, text="Número de Baños:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_numero_banos.grid(row=5, column=3, sticky="e")
        entry_numero_banos = tk.Entry(
            nueva_ventana, font=('Times', 12), width=30)
        entry_numero_banos.grid(row=5, column=4)

        label_valor = tk.Label(nueva_ventana, text="Valor:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_valor.grid(row=6, column=3, sticky="e")
        entry_valor = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_valor.grid(row=6, column=4)
    elif tipo_ == "Automovil":
        label_precio = tk.Label(nueva_ventana, text="Precio:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_precio.grid(row=1, column=3, sticky="e")
        entry_precio = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_precio.grid(row=1, column=4)

        label_placa = tk.Label(nueva_ventana, text="Placa:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_placa.grid(row=2, column=3, sticky="e")
        entry_placa = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_placa.grid(row=2, column=4)

        label_modelo = tk.Label(nueva_ventana, text="Modelo:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_modelo.grid(row=3, column=3, sticky="e")
        entry_modelo = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_modelo.grid(row=3, column=4)

        label_marca = tk.Label(nueva_ventana, text="Marca:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_marca.grid(row=4, column=3, sticky="e")
        entry_marca = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_marca.grid(row=4, column=4)

        label_color = tk.Label(nueva_ventana, text="Color:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_color.grid(row=5, column=3, sticky="e")
        entry_color = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_color.grid(row=5, column=4)
    elif tipo_ == "Desempleo":
        label_precio = tk.Label(nueva_ventana, text="Precio:", font=(
            'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
        label_precio.grid(row=1, column=3, sticky="e")
        entry_precio = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
        entry_precio.grid(row=1, column=4)

    label_valor_asegurado = tk.Label(nueva_ventana, text="Valor asegurado:", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_valor_asegurado.grid(row=7, column=3, sticky="e")
    entry_valor_asegurado = tk.Entry(
        nueva_ventana, font=('Times', 12), width=30)
    entry_valor_asegurado.grid(row=7, column=4)

    # Botón para guardar los datos ingresados
    boton_guardar = tk.Button(
        nueva_ventana, text="Guardar", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=lambda: guardar_datos(tipo_))
    boton_guardar.grid(row=11, column=2, columnspan=1,
                       pady=15, padx=10, sticky="nsew")
    boton_volver = tk.Button(
        nueva_ventana, text="Volver", font=(
            'Times', 15), bg='#f63a3a', bd=0, fg="#fff", command=lambda: volver(nueva_ventana, email_empleado))
    boton_volver.grid(row=12, column=2, columnspan=1,
                      pady=15, padx=10, sticky="nsew")

    # Iniciar el bucle principal de la ventana
    nueva_ventana.mainloop()
