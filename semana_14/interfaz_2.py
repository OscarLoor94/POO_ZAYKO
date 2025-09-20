# Importo tkinter como tk para crear mi interfaz gráfica de usuario
import tkinter as tk
# Importo ttk para usar widgets con estilo mejorado y messagebox para mostrar mensajes al usuario
from tkinter import ttk, messagebox


# Defino mi clase principal para la aplicación de agenda
class AgendaApp:
    # Inicializo mi aplicación con el metodo constructor
    def __init__(self, root):
        # Guardo la ventana raíz como un atributo de mi clase
        self.root = root
        # Establezco el título de mi ventana principal
        self.root.title("Agenda Personal")
        # Configuro el tamaño inicial de mi ventana
        self.root.geometry("600x600")

        # Creo mi Treeview para mostrar los eventos en formato de tabla
        self.tree = ttk.Treeview(root, columns=("Fecha", "Hora", "Descripción"), show="headings")
        # Configuro el encabezado de la columna Fecha
        self.tree.heading("Fecha", text="Fecha")
        # Configuro el encabezado de la columna Hora
        self.tree.heading("Hora", text="Hora")
        # Configuro el encabezado de la columna Descripción
        self.tree.heading("Descripción", text="Descripción")

        self.tree.pack(fill=tk.BOTH, expand=True, pady=10)

        # Creo una etiqueta para el campo de entrada de fecha
        tk.Label(root, text="Fecha (YYYY-MM-DD):").pack(pady=5)
        # Creo el campo de entrada para la fecha
        self.date_entry = tk.Entry(root)
        # Coloco el campo de entrada debajo de su etiqueta
        self.date_entry.pack(pady=5)

        # Creo una etiqueta para el campo de entrada de hora
        tk.Label(root, text="Hora (HH:MM):").pack(pady=5)
        # Creo el campo de entrada para la hora
        self.time_entry = tk.Entry(root)
        # Coloco el campo de entrada debajo de su etiqueta
        self.time_entry.pack(pady=5)

        # Creo una etiqueta para el campo de entrada de descripción
        tk.Label(root, text="Descripción:").pack(pady=5)
        # Creo el campo de entrada para la descripción
        self.desc_entry = tk.Entry(root)
        # Coloco el campo de entrada debajo de su etiqueta
        self.desc_entry.pack(pady=5)

        # Creo el botón para agregar eventos y lo vinculo con su función correspondiente
        tk.Button(root, text="Agregar Evento", command=self.agregar_evento).pack(side=tk.LEFT, padx=10, pady=10)
        # Creo el botón para eliminar eventos y lo vinculo con su función correspondiente
        tk.Button(root, text="Eliminar Seleccionado", command=self.eliminar_evento).pack(side=tk.LEFT, padx=10, pady=10)
        # Creo el botón para salir de la aplicación
        tk.Button(root, text="Salir", command=root.quit).pack(side=tk.RIGHT, padx=10, pady=10)

    # Defino el metodo para agregar un evento a mi agenda
    def agregar_evento(self):
        # Obtengo la fecha ingresada por el usuario
        fecha = self.date_entry.get()
        # Obtengo la hora ingresada por el usuario
        hora = self.time_entry.get()
        # Obtengo la descripción ingresada por el usuario
        descripcion = self.desc_entry.get()

        # Verifico que todos los campos tengan información
        if not fecha or not hora or not descripcion:
            # Si falta algún dato, muestro un mensaje de advertencia
            messagebox.showwarning("Campos Vacíos", "Por favor, llena todos los campos.")
            # Salgo de la función sin agregar nada
            return


        self.tree.insert("", tk.END, values=(fecha, hora, descripcion))
        # Limpio los campos de entrada para facilitar el ingreso de un nuevo evento
        self.limpiar_campos()

    # Defino el metodo para eliminar eventos seleccionados
    def eliminar_evento(self):
        # Obtengo los elementos seleccionados en mi Treeview
        selected_item = self.tree.selection()
        # Verifico si hay algún elemento seleccionado
        if not selected_item:
            # Si no hay nada seleccionado, muestro una advertencia
            messagebox.showwarning("Selecciona Evento", "Por favor, selecciona un evento para eliminar.")
            # Salgo de la función sin eliminar nada
            return

        # Recorro todos los elementos seleccionados
        for item in selected_item:
            # Elimino cada elemento de mi Treeview
            self.tree.delete(item)

    # Defino un metodo para limpiar los campos de entrada
    def limpiar_campos(self):
        # Elimino la fecha
        self.date_entry.delete(0, tk.END)
        # Elimino el campo de hora
        self.time_entry.delete(0, tk.END)
        # Elimino el campo de descripción
        self.desc_entry.delete(0, tk.END)


# Si este archivo se ejecuta directamente (no como módulo)
if __name__ == "__main__":
    # Creo la ventana principal de mi aplicación
    root = tk.Tk()
    # Inicializo mi aplicación con la ventana principal
    app = AgendaApp(root)
    # Inicio el bucle principal de eventos para que mi aplicación responda a las interacciones
    root.mainloop()
