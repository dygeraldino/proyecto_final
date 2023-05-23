import json
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from forms.seguros import Interfaz_seguros
from forms.usuario import Interfaz_usuario
import util.generic as utl

import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

class Interfaz:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('800x500')

        # Crear el título
        title = tk.Label(self.master, text="Seguridad garantizada", font=('Times', 30), fg="#666a88")
        title.grid(row=0, column=0, columnspan=2, pady=20)

        # Crear botones
        buttonUsuario = tk.Button(self.master, text="Usuario", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=self.abrir_interfaz_usuario)
        
        buttonSeguros = tk.Button(self.master, text="Seguros", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=self.abrir_interfaz_seguros)
        
        
        # Colocar botones
        buttonUsuario.grid(row=1, column=0, padx=20, pady=20)
        buttonSeguros.grid(row=1, column=1, padx=20, pady=20)

        # Configurar las proporciones de las filas y columnas
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.master.mainloop()
    
    def abrir_interfaz_usuario(self):
        self.master.destroy()  # Cerrar la interfaz actual
        interfaz_usuario = Interfaz_usuario()  # Abrir la nueva interfaz

    def abrir_interfaz_seguros(self):
        self.master.destroy()  # Cerrar la interfaz actual
        interfaz_seguros = Interfaz_seguros()  # Abrir la nueva interfaz
    
    


