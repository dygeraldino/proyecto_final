import tkinter as tk
import util.generic as utl
from tkinter import ttk
from productos import *


class Interfaz_clientes:
    def __init__(self, empleado):
        self.empleado = empleado
        self.master = tk.Tk()
        self.master.geometry('800x500')
        self.master.title("Info Clientes")
        self.master.config(bg='#B4DEFF')
        self.master.resizable(width=0, height=0)
        utl.centrar_ventana(self.master, 800, 500)

        # Crear el Treeview
        self.treeview = ttk.Treeview(self.master, columns=(
            "nombre", "edad", "genero", "estado_civil", "direccion", "telefono", "correo", "peso", "estatura", "productos"))
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(
            'Times', 15, 'bold'), foreground='#000000', background='#B4DEFF')
        self.style.configure("Treeview", background="white",
                             fieldbackground="white")
        self.style.map("Treeview", background=[('alternate', '#F5F5F5')])
        self.treeview.heading("#0", text="Cliente")
        self.treeview.heading("nombre", text="Nombre")
        self.treeview.heading("edad", text="Edad")
        self.treeview.heading("genero", text="Género")
        self.treeview.heading("estado_civil", text="Estado Civil")
        self.treeview.heading("direccion", text="Dirección")
        self.treeview.heading("telefono", text="Teléfono")
        self.treeview.heading("correo", text="Correo")
        self.treeview.heading("peso", text="Peso")
        self.treeview.heading("estatura", text="Estatura")
        self.treeview.heading("productos", text="Productos")

        # Agregar los clientes a la tabla
        c = 0
        for cliente in self.empleado.clientes:
            c += 1
            item_id = self.treeview.insert("", "end", text=c, values=(cliente.nombre, cliente.edad, cliente.genero,
                                                                      cliente.estado_civil, cliente.direccion, cliente.telefono, cliente.correo, cliente.peso, cliente.estatura, 0))
            self.treeview.set(item_id, column="productos", value="Ver")

        # Configurar las barras de desplazamiento
        scrollbar_y = ttk.Scrollbar(
            self.master, orient="vertical", command=self.treeview.yview)
        scrollbar_x = ttk.Scrollbar(
            self.master, orient="horizontal", command=self.treeview.xview)
        self.treeview.configure(yscroll=scrollbar_y.set,
                                xscroll=scrollbar_x.set)

        # Ubicar el Treeview y las barras de desplazamiento en la interfaz
        self.treeview.grid(row=0, column=0, sticky="nsew")
        scrollbar_y.grid(row=0, column=1, sticky="ns")
        scrollbar_x.grid(row=1, column=0, sticky="ew")

        # Ajustar el tamaño de las columnas del Treeview
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_rowconfigure(0, weight=1)

        # Asociar función al evento de clic en el botón
        self.treeview.tag_configure("button", background="#B4DEFF")
        self.treeview.bind("<Button-1>", self.on_treeview_click)

        self.master.mainloop()

    def on_treeview_click(self, event):
        region = self.treeview.identify("region", event.x, event.y)
        if region == "cell" or region == "tree":
            item_id = self.treeview.identify_row(event.y)
            column = self.treeview.identify_column(event.x)
            if item_id and column == "#10":  # Columna "productos"
                index = self.treeview.index(item_id)
                cliente = self.empleado.clientes[index]
                self.master.destroy()
                inter = Interfaz_productos(cliente)
