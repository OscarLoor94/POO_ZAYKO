import tkinter as tk
from tkinter import ttk, messagebox
import json
import os


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("600x450")
        self.root.configure(bg="#f5f5f5")

        # Intentar cargar tareas existentes o iniciar una lista vacía
        self.tasks = []
        self.load_tasks()

        # Configuración principal
        self.create_widgets()
        self.setup_bindings()

    def create_widgets(self):
        # Frame principal
        main_frame = tk.Frame(self.root, bg="#f5f5f5")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Título
        title_label = tk.Label(
            main_frame,
            text="Gestor de Tareas",
            font=("Helvetica", 16, "bold"),
            bg="#f5f5f5",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))

        # Campo de entrada y botón para añadir tareas
        input_frame = tk.Frame(main_frame, bg="#f5f5f5")
        input_frame.pack(fill=tk.X, pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font=("Helvetica", 12),
            bd=2,
            relief=tk.GROOVE,
            width=40
        )
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10), ipady=5)
        self.task_entry.focus()

        add_button = tk.Button(
            input_frame,
            text="Añadir Tarea",
            command=self.add_task,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 10, "bold"),
            bd=0,
            padx=10,
            pady=5
        )
        add_button.pack(side=tk.LEFT)

        # Lista de tareas
        task_list_frame = tk.Frame(main_frame, bg="white", bd=1, relief=tk.SOLID)
        task_list_frame.pack(fill=tk.BOTH, expand=True, pady=10)

        # Scrollbar para la lista
        scrollbar = tk.Scrollbar(task_list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Lista de tareas usando ttk.Treeview
        self.task_list = ttk.Treeview(
            task_list_frame,
            columns=("status"),
            show="tree",
            yscrollcommand=scrollbar.set
        )
        self.task_list.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.task_list.yview)

        # Configuración de columnas
        self.task_list.column("#0", width=500, minwidth=400)
        self.task_list.column("status", width=0, stretch=tk.NO)  # Columna oculta para estado

        # Estilo personalizado para los elementos de la lista
        style = ttk.Style()
        style.configure("Treeview", font=("Helvetica", 11), rowheight=30)

        # Botones de acción
        button_frame = tk.Frame(main_frame, bg="#f5f5f5")
        button_frame.pack(fill=tk.X, pady=10)

        complete_button = tk.Button(
            button_frame,
            text="Marcar como Completada (C)",
            command=self.toggle_complete_task,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 10),
            bd=0,
            padx=10,
            pady=5
        )
        complete_button.pack(side=tk.LEFT, padx=(0, 10))

        delete_button = tk.Button(
            button_frame,
            text="Eliminar Tarea (D)",
            command=self.delete_task,
            bg="#F44336",
            fg="white",
            font=("Helvetica", 10),
            bd=0,
            padx=10,
            pady=5
        )
        delete_button.pack(side=tk.LEFT)

        # Información de atajos
        shortcuts_frame = tk.Frame(main_frame, bg="#f5f5f5")
        shortcuts_frame.pack(fill=tk.X, pady=(20, 0))

        shortcuts_label = tk.Label(
            shortcuts_frame,
            text="Atajos: Enter = Añadir tarea | C = Completar | D = Eliminar | Esc = Salir",
            font=("Helvetica", 9),
            bg="#f5f5f5",
            fg="#666666"
        )
        shortcuts_label.pack()

        # Cargar tareas en la lista
        self.refresh_task_list()

    def setup_bindings(self):
        # Atajos de teclado
        self.root.bind("<Return>", lambda event: self.add_task())
        self.root.bind("<c>", lambda event: self.toggle_complete_task())
        self.root.bind("<C>", lambda event: self.toggle_complete_task())
        self.root.bind("<d>", lambda event: self.delete_task())
        self.root.bind("<D>", lambda event: self.delete_task())
        self.root.bind("<Delete>", lambda event: self.delete_task())
        self.root.bind("<Escape>", lambda event: self.root.destroy())

        # Al cerrar la ventana, guardar las tareas
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def add_task(self):
        task_text = self.task_entry.get().strip()
        if task_text:
            self.tasks.append({"text": task_text, "completed": False})
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
            self.save_tasks()

    def toggle_complete_task(self):
        selected = self.task_list.selection()
        if selected:
            item_id = selected[0]
            item_index = self.task_list.index(item_id)

            # Cambiar el estado de completado
            self.tasks[item_index]["completed"] = not self.tasks[item_index]["completed"]
            self.refresh_task_list()
            self.save_tasks()

    def delete_task(self):
        selected = self.task_list.selection()
        if selected:
            item_id = selected[0]
            item_index = self.task_list.index(item_id)

            # Eliminar la tarea
            del self.tasks[item_index]
            self.refresh_task_list()
            self.save_tasks()

    def refresh_task_list(self):
        # Limpiar la lista actual
        for item in self.task_list.get_children():
            self.task_list.delete(item)

        # Añadir las tareas a la lista
        for i, task in enumerate(self.tasks):
            status_icon = "✓ " if task["completed"] else "• "
            task_text = status_icon + task["text"]

            # Insertar tarea con estilo según su estado
            item_id = self.task_list.insert("", "end", text=task_text, values=(task["completed"]))

            # Aplicar estilo según estado (completado/pendiente)
            if task["completed"]:
                self.task_list.item(item_id, tags=("completed",))
            else:
                self.task_list.item(item_id, tags=("pending",))

        # Configurar etiquetas para estilos
        self.task_list.tag_configure("completed", foreground="#888888", font=("Helvetica", 11, "italic"))
        self.task_list.tag_configure("pending", foreground="#000000", font=("Helvetica", 11))

    def save_tasks(self):
        """Guardar tareas en un archivo JSON"""
        try:
            with open("tasks.json", "w") as file:
                json.dump(self.tasks, file)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron guardar las tareas: {str(e)}")

    def load_tasks(self):
        """Cargar tareas desde un archivo JSON"""
        try:
            if os.path.exists("tasks.json"):
                with open("tasks.json", "r") as file:
                    self.tasks = json.load(file)
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron cargar las tareas: {str(e)}")
            self.tasks = []

    def on_closing(self):
        """Guardar tareas al cerrar la aplicación"""
        self.save_tasks()
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()