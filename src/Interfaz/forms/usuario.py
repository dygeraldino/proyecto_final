import tkinter as tk

class Interfaz_usuario:
    def __init__(self):
        self.master = tk.Tk()
        self.master.geometry('400x400')
        self.master.title("Interfaz Usuario")

        # Datos de ejemplo
        datos_usuario = {
            "Nombre": "John Doe",
            "Edad": 30,
            "Cédula": "123456789",
            "Género": "Masculino",
            "Estado Civil": "Soltero",
            "ID": "USR123",
            "Sueldo": 5000,
            "Clientes": ["Cliente1", "Cliente2", "Cliente3"]
        }

        # Mostrar los datos
        for i, (campo, valor) in enumerate(datos_usuario.items()):
            label_campo = tk.Label(self.master, text=campo + ":")
            label_campo.grid(row=i, column=0, sticky=tk.W)
            
            label_valor = tk.Label(self.master, text=str(valor))
            label_valor.grid(row=i, column=1, sticky=tk.W)


