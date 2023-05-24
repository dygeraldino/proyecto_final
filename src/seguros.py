import tkinter as tk
from tipos import abrir_ventana_parametros

class Interfaz_seguros:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('800x500')

        # Crear el título
        title = tk.Label(self.master, text="Seguros", font=('Times', 30), fg="#666a88")
        title.grid(row=0, column=0, columnspan=2, pady=20)

        # Crear botones
        buttonSOAT = tk.Button(self.master, text="SOAT", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("SOAT"))
        buttonHogar = tk.Button(self.master, text="Hogar", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Hogar"))
        buttonAutomovil = tk.Button(self.master, text="Automovil", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Automovil"))
        buttonVida = tk.Button(self.master, text="Vida", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Vida"))
        buttonDesempleo = tk.Button(self.master, text="Desempleo", font=('Times', 22), bg="#3a7ff6", fg="#fff", command=lambda: self.abrir_interfaz_tipos("Desempleo"))

        # Colocar botones
        buttonSOAT.grid(row=1, column=0, padx=20, pady=20)
        buttonHogar.grid(row=1, column=1, padx=20, pady=20)
        buttonAutomovil.grid(row=2, column=0, padx=20, pady=20)
        buttonVida.grid(row=2, column=1, padx=20, pady=20)
        buttonDesempleo.grid(row=3, column=0, padx=20, pady=20)

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
        interfaz_tipos = abrir_ventana_parametros(tipo_)


