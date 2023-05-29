import tkinter as tk
import util.generic as utl
from tipos import abrir_ventana_parametros


class Interfaz_seguros:
    def __init__(self, empleado):
        self.empleado = empleado
        self.master = tk.Tk()
        self.master.geometry('800x500')
        utl.centrar_ventana(self.master, 800, 500)

        # Crear el título
        title_frame = tk.Frame(self.master, bg="#3a7ff6")
        title_frame.grid(row=0, column=0, columnspan=2, pady=20, sticky="we")
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_rowconfigure(0, weight=1)

        title = tk.Label(title_frame, text="Seguros", font=(
            'Times', 30), fg="#fff", bg="#3a7ff6")
        title.grid(row=0, column=0, padx=20, pady=10)

        # Crear botones
        buttonSOAT = tk.Button(self.master, text="SOAT", font=(
            'Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("SOAT"))
        buttonHogar = tk.Button(self.master, text="Hogar", font=(
            'Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Hogar"))
        buttonAutomovil = tk.Button(self.master, text="Automovil", font=(
            'Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Automovil"))
        buttonVida = tk.Button(self.master, text="Vida", font=(
            'Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Vida"))
        buttonDesempleo = tk.Button(self.master, text="Desempleo", font=(
            'Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Desempleo"))
        buttonVolver = tk.Button(self.master, text="Volver", font=(
            'Times', 22), bg="#f63a3a", fg="#fff", command=lambda: self.volver())

        # Colocar botones
        buttonSOAT.grid(row=1, column=0, padx=20, pady=20)
        buttonHogar.grid(row=1, column=1, padx=20, pady=20)
        buttonAutomovil.grid(row=2, column=0, padx=20, pady=20)
        buttonVida.grid(row=2, column=1, padx=20, pady=20)
        buttonDesempleo.grid(row=3, column=0, padx=20, pady=20)
        buttonVolver.grid(row=3, column=1, padx=20, pady=20)

        # Configurar las proporciones de las filas y columnas
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_rowconfigure(1, weight=1)
        self.master.grid_rowconfigure(2, weight=1)
        self.master.grid_rowconfigure(3, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(1, weight=1)

        self.master.mainloop()

    def abrir_interfaz_tipos(self, tipo_):
        self.master.destroy()  # Cerrar la interfaz actual
        interfaz_tipos = abrir_ventana_parametros(tipo_, self.empleado)

    def volver(self):
        self.master.destroy()
        from interfaz import Interfaz
        inter = Interfaz(self.empleado)
