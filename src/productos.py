import tkinter as tk
import util.generic as utl
from tkinter import ttk


class Interfaz_productos:
    def __init__(self, cliente):
        self.cliente = cliente
        self.master = tk.Tk()
        self.master.geometry('800x500')
        self.master.title("Info Productos")
        self.master.config(bg='#B4DEFF')
        self.master.resizable(width=0, height=0)
        utl.centrar_ventana(self.master, 800, 500)
