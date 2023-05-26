import tkinter as tk
from tkinter import ttk, messagebox
from classes import *
from json_controller import *
import util.generic as utl
from clientes import *


class Interfaz_usuario:
    def __init__(self, email_empleado):
        self.email_empleado = email_empleado
        self.master = tk.Tk()
        self.master.geometry('800x500')
        self.master.title("Info Empleado")
        self.master.config(bg='#B4DEFF')
        self.master.resizable(width=0, height=0)
        utl.centrar_ventana(self.master, 800, 500)

        empleados = total_empleados()
        for empleado in empleados:
            if empleado.correo == email_empleado:
                user_empleado = empleado

        label_titulo = tk.Label(self.master, text=f"{user_empleado.correo}: ", font=(
            'Times', 20), fg="#333333", bg='#B4DEFF')
        label_titulo.grid(row=0, column=0, columnspan=2, pady=20)

        label_nombre = tk.Label(self.master, text="Nombre:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_nombre.grid(row=2, column=0, sticky="e")

        label_vnombre = tk.Label(self.master, text=f"{user_empleado.nombre}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vnombre.grid(row=2, column=2, sticky="e")

        label_edad = tk.Label(self.master, text="Edad:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_edad.grid(row=3, column=0, sticky="e")

        label_vedad = tk.Label(self.master, text=f"{user_empleado.edad}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vedad.grid(row=3, column=2, sticky="e")

        label_genero = tk.Label(self.master, text="Género:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_genero.grid(row=4, column=0, sticky="e")

        label_vgenero = tk.Label(self.master, text=f"{user_empleado.genero}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vgenero.grid(row=4, column=2, sticky="e")

        label_estado_civil = tk.Label(self.master, text="Estado Civil:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_estado_civil.grid(row=5, column=0, sticky="e")

        label_vestado_civil = tk.Label(self.master, text=f"{user_empleado.estado_civil}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vestado_civil.grid(row=5, column=2, sticky="e")

        label_sueldo = tk.Label(self.master, text="Sueldo:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_sueldo.grid(row=6, column=0, sticky="e")

        label_vsueldo = tk.Label(self.master, text=f"{user_empleado.sueldo}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vsueldo.grid(row=6, column=2, sticky="e")

        label_correo = tk.Label(self.master, text="Correo:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_correo.grid(row=7, column=0, sticky="e")

        label_vcorreo = tk.Label(self.master, text=f"{user_empleado.correo}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vcorreo.grid(row=7, column=2, sticky="e")

        user_empleado.calcular_comision()

        label_comision = tk.Label(self.master, text="Comisión:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_comision.grid(row=8, column=0, sticky="e")

        label_vcomision = tk.Label(self.master, text=f"{user_empleado.comision}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vcomision.grid(row=8, column=2, sticky="e")

        label_clientes = tk.Label(self.master, text="Clientes:", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_clientes.grid(row=9, column=0, sticky="e")

        label_vclientes = tk.Label(self.master, text=f"{len(user_empleado.clientes)}", font=(
            'Times', 16), fg="#666a88", bg='#B4DEFF', anchor="w")
        label_vclientes.grid(row=9, column=2, sticky="e")

        boton_clientes = tk.Button(
            self.master, text="Clientes", font=(
                'Times', 15), bg='#3a7ff6', bd=0, fg="#fff", command=lambda: self.abrir_interfaz_clientes(user_empleado))
        boton_clientes.grid(row=11, column=1, columnspan=2,
                            pady=15, padx=20, sticky="nsew")

        self.master.mainloop()

    def abrir_interfaz_clientes(self, user_empleado):
        self.master.destroy()  # Cerrar la interfaz actual
        interfaz_clientes = Interfaz_clientes(user_empleado)
