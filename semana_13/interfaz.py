


class AplicacionPrincipal:  # Defino mi clase principal que manejará toda la aplicación
    def __init__(self, root):  # Creo el constructor que inicializa mi aplicación
        # Configuración de la ventana principal
        self.root = root  # Guardo la referencia a la ventana raíz
        self.root.title("Gestor de Información")  # Establezco el título de mi ventana
        self.root.geometry("500x400")  # Defino el tamaño inicial de mi ventana
        self.root.resizable(True, True)  # Permito que mi ventana pueda cambiar de tamaño

        # Variables para los campos de entrada
        self.var_nombre = tk.StringVar()  # Creo una variable para almacenar el nombre ingresado
        self.var_descripcion = tk.StringVar()  # Creo una variable para almacenar la descripción ingresada

        # Crear el marco principal
        self.marco_principal = ttk.Frame(root, padding="10")  # Creo un marco con padding para contener todos mis widgets
        self.marco_principal.pack(fill=tk.BOTH, expand=True)

        self.crear_seccion_entrada()  # Llamo al metodo que creará la sección para ingresar datos


        self.crear_seccion_visualizacion()  # Llamo al metodo que creará la tabla para mostrar los datos


        self.crear_seccion_botones()  # Llamo al metodo que creará los botones de acción

    def crear_seccion_entrada(self):  # Defino el metodo para crear los campos de entrada
        # Marco para la sección de entrada
        marco_entrada = ttk.LabelFrame(self.marco_principal, text="Ingrese la información", padding="10")  # Creo un marco con título
        marco_entrada.pack(fill=tk.X, pady=10)

        # Etiqueta y campo para el nombre
        ttk.Label(marco_entrada, text="Nombre:").grid(row=0, column=0, sticky=tk.W, pady=5)  # Añado una etiqueta para el nombre
        ttk.Entry(marco_entrada, textvariable=self.var_nombre, width=40).grid(row=0, column=1, pady=5, padx=5)  # Añado un campo de texto para el nombre

        # Etiqueta y campo para la descripción
        ttk.Label(marco_entrada, text="Descripción:").grid(row=1, column=0, sticky=tk.W, pady=5)  # Añado una etiqueta para la descripción
        ttk.Entry(marco_entrada, textvariable=self.var_descripcion, width=40).grid(row=1, column=1, pady=5, padx=5)  # Añado un campo de texto para la descripción

    def crear_seccion_visualizacion(self):  # Defino el metodo para crear la tabla de visualización
        # Marco para la tabla
        marco_tabla = ttk.LabelFrame(self.marco_principal, text="Información guardada", padding="10")  # Creo un marco con título para la tabla
        marco_tabla.pack(fill=tk.BOTH, expand=True, pady=10)

        # Crear la tabla con Treeview
        columnas = ("nombre", "descripcion")  # Defino los nombres internos de las columnas
        self.tabla = ttk.Treeview(marco_tabla, columns=columnas, show="headings")  # Creo una tabla con las columnas definidas
        self.tabla.heading("nombre", text="Nombre")  # Establezco el título visible de la columna nombre
        self.tabla.heading("descripcion", text="Descripción")  # Establezco el título visible de la columna descripción
        self.tabla.column("nombre", width=150)  # Defino el ancho de la columna nombre
        self.tabla.column("descripcion", width=300)  # Defino el ancho de la columna descripción
        self.tabla.pack(fill=tk.BOTH, expand=True)


        scrollbar = ttk.Scrollbar(marco_tabla, orient=tk.VERTICAL, command=self.tabla.yview)  # Creo una barra de desplazamiento vertical
        self.tabla.configure(yscrollcommand=scrollbar.set)  # Conecto la tabla con la barra de desplazamiento
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)  # Coloco la barra de desplazamiento a la derecha

    def crear_seccion_botones(self):  # Defino el metodo para crear los botones
        # Marco para los botones
        marco_botones = ttk.Frame(self.marco_principal)  # Creo un marco para contener los botones
        marco_botones.pack(fill=tk.X, pady=10)

        # Botón para agregar información
        btn_agregar = ttk.Button(marco_botones, text="Agregar", command=self.agregar_informacion)  # Creo un botón para agregar datos
        btn_agregar.pack(side=tk.LEFT, padx=5)  # Coloco el botón a la izquierda con espacio horizontal

        # Botón para limpiar campos
        btn_limpiar = ttk.Button(marco_botones, text="Limpiar", command=self.limpiar_campos)  # Creo un botón para limpiar los campos
        btn_limpiar.pack(side=tk.LEFT, padx=5)  # Coloco el botón a la izquierda del anterior

        # Botón para eliminar elemento seleccionado
        btn_eliminar = ttk.Button(marco_botones, text="Eliminar seleccionado", command=self.eliminar_seleccionado)  # Creo un botón para eliminar elementos
        btn_eliminar.pack(side=tk.LEFT, padx=5)  # Coloco el botón a la izquierda de los anteriores

    def agregar_informacion(self):  # Defino el metodo para agregar información a la tabla
        # Obtener los valores de los campos
        nombre = self.var_nombre.get().strip()  # Obtengo el nombre ingresado y elimino espacios
        descripcion = self.var_descripcion.get().strip()  # Obtengo la descripción ingresada y elimino espacios

        # Validar que los campos no estén vacíos
        if nombre == "" or descripcion == "":  # Verifico si alguno de los campos está vacío
            messagebox.showwarning("Campos vacíos", "Por favor, complete todos los campos.")  # Muestro un mensaje de advertencia
            return  # Termino la ejecución del metodo si hay campos vacíos

        # Agregar a la tabla
        self.tabla.insert("", tk.END, values=(nombre, descripcion))  # Inserto los valores en la tabla al final

        # Limpiar los campos después de agregar
        self.limpiar_campos()  # Llamo al metodo para limpiar los campos después de agregar

    def limpiar_campos(self):  # Defino el metodo para limpiar

        self.var_nombre.set("")  # Limpio el campo de nombre
        self.var_descripcion.set("")  # Limpio el campo de descripción

    def eliminar_seleccionado(self):  # Defino el metodo para eliminar
        # Obtener el elemento seleccionado
        seleccionado = self.tabla.selection()  # Obtengo el elemento que el usuario ha seleccionado

        # Si hay un elemento seleccionado, eliminarlo
        if seleccionado:  # Verifico si hay algún elemento seleccionado
            self.tabla.delete(seleccionado)  # Elimino el elemento seleccionado de la tabla
        else:  # Si no hay elemento seleccionado
            messagebox.showinfo("Selección", "No hay elemento seleccionado para eliminar.")  # Muestro un mensaje informativo


# Función principal para iniciar la aplicación
def main():  # Defino la función principal que inicia mi aplicación
    root = tk.Tk()  # Creo la ventana raíz de mi aplicación
    app = AplicacionPrincipal(root)  # Creo una instancia de mi aplicación
    root.mainloop()  # Inicio el bucle principal de eventos


if __name__ == "__main__":  # Verifico si este archivo se está ejecutando directamente
    main()  # Llamo a la función principal para iniciar la aplicación