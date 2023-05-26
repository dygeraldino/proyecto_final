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

        # Crear el Treeview
        self.treeview = ttk.Treeview(self.master, columns=(
            "tipo", "precio", "valor_asegurado", "cobertura"))
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=(
            'Times', 15, 'bold'), foreground='#000000', background='#B4DEFF')
        self.style.configure("Treeview", background="white",
                             fieldbackground="white")
        self.style.map("Treeview", background=[('alternate', '#F5F5F5')])
        self.treeview.heading("#0", text="Seguro")
        self.treeview.heading("tipo", text="Tipo")
        self.treeview.heading("precio", text="Precio")
        self.treeview.heading("valor_asegurado", text="Valor Asegurado")
        self.treeview.heading("cobertura", text="Cobertura")

        # Agregar los seguros a la tabla
        c = 0
        for seguro in self.cliente.productos:
            c += 1
            item_id = self.treeview.insert("", "end", text=c, values=(seguro.tipo, seguro.precio,
                                                                      seguro.valor_asegurado, seguro.cobertura))

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

        self.master.mainloop()
