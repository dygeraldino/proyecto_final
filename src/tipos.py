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
    def guardar_producto(tipo_):
        try:
            cedula = int(entry_cedula.get())
            clientes = total_clientes()
            i = -1
            indice = -1
            for cliente in clientes:
                i += 1
                if cliente.cedula == cedula:
                    indice = i
            if indice == -1:
                raise ClienteException(
                    "No se encontró el cliente con cédula " + str(cedula) + " por favor, registrelo")
            else:
                valor_asegurado = float(entry_valor_asegurado.get())
                if valor_asegurado < 20000000 or valor_asegurado > 500000000:
                    raise ClienteException(
                        "El valor asegurado debe ser mayor a 20 millones y menor de 500 millones")
        except ValueError:
            messagebox.showerror(
                message=f"Recuerde que la edad y la cedula son números naturales \nPor otra parte el precio, la estatura y el valor asegurado son reales positivos", title="Error de valor")
            return False
        except ClienteException as ex:
            messagebox.showerror(
                message=f"{ex.__class__.__name__}: {ex}", title="Error")
            return False

        # Crear objeto Cliente con los datos ingresados
        cliente = clientes[indice]

        # Dependiendo del tipo de seguro, obtener los valores adicionales
        if tipo_ == "SOAT":
            try:
                placa = entry_placa.get()
                if len(placa) == 0:
                    raise ProductoException(
                        "La placa del vehículo no puede estar vacía")
                if len(placa) != 6:
                    raise ProductoException(
                        "La placa del vehículo debe tener 6 caracteres")
                modelo = entry_modelo.get()
                if len(modelo) == 0:
                    raise ProductoException(
                        "El modelo del vehículo no puede estar vacío")
                marca = entry_marca.get()
                if len(marca) == 0:
                    raise ProductoException(
                        "La marca del vehículo no puede estar vacía")
                color = entry_color.get()
                if len(color) == 0:
                    raise ProductoException(
                        "El color del vehículo no puede estar vacío")
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = SOAT(cliente, placa, modelo, marca, color)
        elif tipo_ == "Vida":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Vida(precio, cliente)
        elif tipo_ == "Hogar":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
                direccion = entry_direccion.get()
                if len(direccion) == 0:
                    raise ClienteException(
                        "La dirección de la casa no puede estar vacía")
                metros_cuadrados = float(entry_metros_cuadrados.get())
                if metros_cuadrados < 0:
                    raise ProductoException(
                        "Los metros cuadrados deben ser un número real positivo")
                numero_habitaciones = int(entry_numero_habitaciones.get())
                if numero_habitaciones < 0:
                    raise ProductoException(
                        "El número de habitaciones debe ser mayor o igual a 0")
                numero_banos = int(entry_numero_banos.get())
                if numero_banos < 0:
                    raise ProductoException(
                        "El número de baños debe ser mayor o igual a 0")
                valor = float(entry_valor.get())
                if valor < 0:
                    raise ProductoException(
                        "El valor de la casa debe ser un número real positivo")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio, los metros cuadrados, el número de habitaciones (entero), el número de baños (entero) y el valor de la casa deben ser números reales positivos", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Hogar(precio, cliente, direccion, metros_cuadrados,
                           numero_habitaciones, numero_banos, valor)
        elif tipo_ == "Automovil":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
                placa = entry_placa.get()
                if len(placa) == 0:
                    raise ProductoException(
                        "La placa del vehículo no puede estar vacía")
                if len(placa) != 6:
                    raise ProductoException(
                        "La placa del vehículo debe tener 6 caracteres")
                modelo = entry_modelo.get()
                if len(modelo) == 0:
                    raise ProductoException(
                        "El modelo del vehículo no puede estar vacío")
                marca = entry_marca.get()
                if len(marca) == 0:
                    raise ProductoException(
                        "La marca del vehículo no puede estar vacía")
                color = entry_color.get()
                if len(color) == 0:
                    raise ProductoException(
                        "El color del vehículo no puede estar vacío")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Automovil(precio, cliente, placa, modelo, marca, color)
        elif tipo_ == "Desempleo":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Desempleo(precio, cliente)

        seguro.valor_asegurado = valor_asegurado
        cliente.productos.append(seguro)
        empleados = total_empleados()
        for empleado in empleados:
            if empleado.correo == email_empleado:
                empleado_cedula = empleado.cedula
        try:
            add_producto(seguro, empleado_cedula)
            messagebox.showinfo(message="Producto agregado exitosamente",
                                title="Vendido")
        except ClienteException as ex:
            messagebox.showerror(
                message=f"{ex.__class__.__name__}: {ex}", title="Error")

    def guardar_datos(tipo_):
        # Obtener los valores ingresados por el usuario
        try:
            nombre = entry_nombre.get()
            if len(nombre) == 0:
                raise ClienteException("El nombre no puede estar vacío")
            edad = int(entry_edad.get())
            if edad < 18:
                raise ClienteException(
                    f"Los menores de edad no pueden comprar un seguro de {tipo_}")
            cedula = int(entry_cedula.get())
            if cedula < 1000000:
                raise ClienteException(
                    "La cédula debe ser un número natural de al menos 7 dígitos")
            genero = entry_genero.get()
            if genero not in ["M", "F"]:
                raise ClienteException(
                    "El género debe ser M (Masculino) o F (Femenino)")
            estado_civil = entry_estado_civil.get()
            if estado_civil not in ["Soltero", "Casado", "Viudo", "Divorciado"]:
                raise ClienteException(
                    "El estado civil debe ser Soltero, Casado, Viudo o Divorciado")
            direccion1 = entry_direccion1.get()
            if len(direccion1) == 0:
                raise ClienteException("La dirección no puede estar vacía")
            telefono = entry_telefono.get()
            if len(telefono) == 0:
                raise ClienteException("El teléfono no puede estar vacío")
            correo = entry_correo.get()
            if len(correo) == 0:
                raise ClienteException("El correo no puede estar vacío")
            peso = float(entry_peso.get())
            if peso < 0 or peso > 500:
                raise ClienteException(
                    "El peso debe ser un número real positivo menor a 500 kilogramos")
            estatura = float(entry_estatura.get())
            if estatura < 0 or estatura > 3:
                raise ClienteException(
                    "La estatura debe ser un número real positivo menor a 3 metros")
            valor_asegurado = float(entry_valor_asegurado.get())
            if valor_asegurado < 20000000 or valor_asegurado > 500000000:
                raise ClienteException(
                    "El valor asegurado debe ser mayor a 20 millones y menor de 500 millones")
        except ValueError:
            messagebox.showerror(
                message=f"Recuerde que la edad y la cedula son números naturales \nPor otra parte el precio, la estatura y el valor asegurado son reales positivos", title="Error de valor")
            return False
        except ClienteException as ex:
            messagebox.showerror(
                message=f"{ex.__class__.__name__}: {ex}", title="Error")
            return False

        # Crear objeto Cliente con los datos ingresados
        cliente = Cliente(nombre, edad, cedula, genero, estado_civil,
                          direccion1, telefono, correo, peso, estatura)

        # Dependiendo del tipo de seguro, obtener los valores adicionales
        if tipo_ == "SOAT":
            try:
                placa = entry_placa.get()
                if len(placa) == 0:
                    raise ProductoException(
                        "La placa del vehículo no puede estar vacía")
                if len(placa) != 6:
                    raise ProductoException(
                        "La placa del vehículo debe tener 6 caracteres")
                modelo = entry_modelo.get()
                if len(modelo) == 0:
                    raise ProductoException(
                        "El modelo del vehículo no puede estar vacío")
                marca = entry_marca.get()
                if len(marca) == 0:
                    raise ProductoException(
                        "La marca del vehículo no puede estar vacía")
                color = entry_color.get()
                if len(color) == 0:
                    raise ProductoException(
                        "El color del vehículo no puede estar vacío")
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = SOAT(cliente, placa, modelo, marca, color)
        elif tipo_ == "Vida":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Vida(precio, cliente)
        elif tipo_ == "Hogar":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
                direccion = entry_direccion.get()
                if len(direccion) == 0:
                    raise ClienteException(
                        "La dirección de la casa no puede estar vacía")
                metros_cuadrados = float(entry_metros_cuadrados.get())
                if metros_cuadrados < 0:
                    raise ProductoException(
                        "Los metros cuadrados deben ser un número real positivo")
                numero_habitaciones = int(entry_numero_habitaciones.get())
                if numero_habitaciones < 0:
                    raise ProductoException(
                        "El número de habitaciones debe ser mayor o igual a 0")
                numero_banos = int(entry_numero_banos.get())
                if numero_banos < 0:
                    raise ProductoException(
                        "El número de baños debe ser mayor o igual a 0")
                valor = float(entry_valor.get())
                if valor < 0:
                    raise ProductoException(
                        "El valor de la casa debe ser un número real positivo")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio, los metros cuadrados, el número de habitaciones (entero), el número de baños (entero) y el valor de la casa deben ser números reales positivos", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Hogar(precio, cliente, direccion, metros_cuadrados,
                           numero_habitaciones, numero_banos, valor)
        elif tipo_ == "Automovil":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
                placa = entry_placa.get()
                if len(placa) == 0:
                    raise ProductoException(
                        "La placa del vehículo no puede estar vacía")
                if len(placa) != 6:
                    raise ProductoException(
                        "La placa del vehículo debe tener 6 caracteres")
                modelo = entry_modelo.get()
                if len(modelo) == 0:
                    raise ProductoException(
                        "El modelo del vehículo no puede estar vacío")
                marca = entry_marca.get()
                if len(marca) == 0:
                    raise ProductoException(
                        "La marca del vehículo no puede estar vacía")
                color = entry_color.get()
                if len(color) == 0:
                    raise ProductoException(
                        "El color del vehículo no puede estar vacío")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Automovil(precio, cliente, placa, modelo, marca, color)
        elif tipo_ == "Desempleo":
            try:
                precio = float(entry_precio.get())
                if precio < 100000 or precio > 3000000:
                    raise ProductoException(
                        "El precio (cuota mensual) debe ser mayor a 100 mil y menor a 3 millones")
            except ValueError:
                messagebox.showerror(
                    message=f"Recuerde que el precio debe ser un número real positivo", title="Error de valor")
                return False
            except ProductoException as ex:
                messagebox.showerror(
                    message=f"{ex.__class__.__name__}: {ex}", title="Error")
                return False
            seguro = Desempleo(precio, cliente)

        seguro.valor_asegurado = valor_asegurado
        cliente.productos.append(seguro)
        empleados = total_empleados()
        for empleado in empleados:
            if empleado.correo == email_empleado:
                empleado_cedula = empleado.cedula
        try:
            add_cliente(cliente, empleado_cedula)
            add_producto(seguro, empleado_cedula)
            messagebox.showinfo(message="Cliente agregado exitosamente",
                                title="Vendido")
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

    label_genero = tk.Label(nueva_ventana, text="Género (M o F):", font=(
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

    label_peso = tk.Label(nueva_ventana, text="Peso (kg):", font=(
        'Times', 14), fg="#666a88", bg='#E6F0FF', anchor="w")
    label_peso.grid(row=9, column=1, sticky="e")
    entry_peso = tk.Entry(nueva_ventana, font=('Times', 12), width=30)
    entry_peso.grid(row=9, column=2)

    label_estatura = tk.Label(nueva_ventana, text="Estatura (m):", font=(
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
        nueva_ventana, text="Registrar y vender", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=lambda: guardar_datos(tipo_))
    boton_guardar.grid(row=11, column=2, columnspan=1,
                       pady=10, padx=10, sticky="nsew")
    boton_producto = tk.Button(
        nueva_ventana, text="Vender producto", font=(
            'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=lambda: guardar_producto(tipo_))
    boton_producto.grid(row=12, column=2, columnspan=1,
                        pady=10, padx=10, sticky="nsew")
    boton_volver = tk.Button(
        nueva_ventana, text="Volver", font=(
            'Times', 15), bg='#f63a3a', bd=0, fg="#fff", command=lambda: volver(nueva_ventana, email_empleado))
    boton_volver.grid(row=13, column=2, columnspan=1,
                      pady=10, padx=10, sticky="nsew")

    # Iniciar el bucle principal de la ventana
    nueva_ventana.mainloop()
