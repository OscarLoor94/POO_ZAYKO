# Defino la clase Libro para representar cada ejemplar en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        # Guardo el autor y el título juntos en una tupla para facilitar su acceso
        self.info = (autor, titulo)
        self.categoria = categoria
        self.isbn = isbn

    def __str__(self):
        # Devuelvo una representación legible del libro
        return f"'{self.info[1]}' de {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Creo la clase Usuario para manejar la información de cada persona registrada
class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []  # Lista para guardar los libros que tiene prestados

    def __str__(self):
        # Representación legible del usuario
        return f"Usuario: {self.nombre} (ID: {self.id_usuario})"


# Esta es la clase principal que gestiona toda la lógica de la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros = {}         # Diccionario para almacenar libros por ISBN
        self.usuarios = {}       # Diccionario para almacenar usuarios por ID
        self.ids_usuarios = set()  # Conjunto para evitar IDs duplicados

    # Metodo para añadir un libro a la biblioteca
    def añadir_libro(self, libro):
        if libro.isbn in self.libros:
            print("El libro ya está en la biblioteca.")
        else:
            self.libros[libro.isbn] = libro
            print(f"Libro añadido: {libro}")

    # Alias del metodo anterior, por si quiero usar otro nombre
    def agregar_libro(self, libro):
        self.añadir_libro(libro)

    # Metodo para quitar un libro, verificando que no esté prestado
    def quitar_libro(self, isbn):
        if isbn in self.libros:
            for usuario in self.usuarios.values():
                if any(libro.isbn == isbn for libro in usuario.libros_prestados):
                    print("No se puede eliminar el libro porque está prestado.")
                    return
            libro = self.libros.pop(isbn)
            print(f"Libro eliminado: {libro}")
        else:
            print("El libro no existe en la biblioteca.")

    # Alias del metodo anterior
    def eliminar_libro(self, isbn):
        self.quitar_libro(isbn)

    # Metodo para registrar un nuevo usuario
    def registrar_usuario(self, usuario):
        if usuario.id_usuario in self.ids_usuarios:
            print("El ID de usuario ya está registrado.")
        else:
            self.usuarios[usuario.id_usuario] = usuario
            self.ids_usuarios.add(usuario.id_usuario)
            print(f"Usuario registrado: {usuario}")

    # Alias del metodo anterior
    def añadir_usuario(self, usuario):
        self.registrar_usuario(usuario)

    # Metodo para dar de baja a un usuario, siempre que no tenga libros prestados
    def dar_baja_usuario(self, id_usuario):
        if id_usuario in self.ids_usuarios:
            usuario = self.usuarios[id_usuario]
            if usuario.libros_prestados:
                print("El usuario tiene libros prestados, no se puede dar de baja.")
                return
            self.ids_usuarios.remove(id_usuario)
            del self.usuarios[id_usuario]
            print(f"Usuario dado de baja: {usuario.nombre}")
        else:
            print("El usuario no está registrado.")

    # Alias del metodo anterior
    def eliminar_usuario(self, id_usuario):
        self.dar_baja_usuario(id_usuario)

    # Metodo para prestar un libro a un usuario
    def prestar_libro(self, isbn, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        if isbn not in self.libros:
            print("Libro no disponible en la biblioteca.")
            return
        usuario = self.usuarios[id_usuario]
        libro = self.libros[isbn]
        # Verifico que el libro no esté prestado a otro usuario
        for u in self.usuarios.values():
            if any(l.isbn == isbn for l in u.libros_prestados):
                print("El libro ya está prestado a otro usuario.")
                return
        usuario.libros_prestados.append(libro)
        print(f"Libro '{libro.info[1]}' prestado a {usuario.nombre}.")

    # Alias del metodo anterior
    def entregar_libro(self, isbn, id_usuario):
        self.prestar_libro(isbn, id_usuario)

    # Metodo para devolver un libro
    def devolver_libro(self, isbn, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return
        usuario = self.usuarios[id_usuario]
        for libro in usuario.libros_prestados:
            if libro.isbn == isbn:
                usuario.libros_prestados.remove(libro)
                print(f"Libro '{libro.info[1]}' devuelto por {usuario.nombre}.")
                return
        print("El usuario no tiene ese libro prestado.")

    # Alias del metodo anterior
    def recibir_libro(self, isbn, id_usuario):
        self.devolver_libro(isbn, id_usuario)

    # Metodo para buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        resultado = []
        valor = valor.lower()  # Normalizo el valor para hacer la búsqueda más flexible
        for libro in self.libros.values():
            autor, titulo = libro.info
            if criterio == "titulo" and valor in titulo.lower():
                resultado.append(libro)
            elif criterio == "autor" and valor in autor.lower():
                resultado.append(libro)
            elif criterio == "categoria" and valor in libro.categoria.lower():
                resultado.append(libro)
        return resultado

    # Alias del metodo anterior
    def buscar_por(self, criterio, valor):
        return self.buscar_libros(criterio, valor)

    # Metodo para listar los libros prestados a un usuario
    def listar_prestados(self, id_usuario):
        if id_usuario not in self.ids_usuarios:
            print("Usuario no registrado.")
            return []
        usuario = self.usuarios[id_usuario]
        return usuario.libros_prestados

    # Alias del metodo anterior
    def mostrar_prestados(self, id_usuario):
        return self.listar_prestados(id_usuario)


# Bloque principal para probar el funcionamiento del sistema
if __name__ == "__main__":
    # Creo una instancia de la biblioteca
    biblioteca = Biblioteca()

    # Creo dos libros con sus respectivos datos
    libro1 = Libro("El viaje inesperado", "Oscar Loor", "Aventura", "1111111111")
    libro2 = Libro("Secretos del alma", "María Bravo", "Misterio", "2222222222")

    # Agrego los libros a la biblioteca
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)

    # Creo dos usuarios
    usuario1 = Usuario("Juan Vasquez", "U001")
    usuario2 = Usuario("Luis Bravo", "U002")

    # Registro los usuarios en la biblioteca
    biblioteca.añadir_usuario(usuario1)
    biblioteca.añadir_usuario(usuario2)

    # Presto un libro a Ana
    biblioteca.entregar_libro("1111111111", "U001")

    # Muestro los libros prestados a Ana
    prestados = biblioteca.mostrar_prestados("U001")
    print("Libros prestados a Ana:")
    for libro in prestados:
        print(libro)

    # Busco libros por autor
    encontrados = biblioteca.buscar_por("autor", "oscar")
    print("Libros encontrados por autor 'oscar':")
    for libro in encontrados:
        print(libro)

    # Ana devuelve el libro
    biblioteca.recibir_libro("1111111111", "U001")

    # Elimino a Ana como usuaria, ya que no tiene libros prestados
    biblioteca.eliminar_usuario("U001")