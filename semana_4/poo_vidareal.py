class Libro: # defino una nueva clase llamada Libro
    def __init__(self, titulo, autor, isbn):
        #Aquí inicializo cada libro con tres datos: título, autor e ISBN
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Inicialmente, el libro está disponible
    #Creo un metodo para prestar el libro
    def prestar(self):
        if self.disponible: #Si el libro esta disponible lo marco como prestado
            self.disponible = False
            print(f"Libro '{self.titulo}' prestado.")
            return True
        else:
            #Si el libro ya estaba prestado, aviso que no se puede prestar y devuelvo False.
            print(f"Libro '{self.titulo}' no disponible.")
            return False
  #Creo un metodo para devolver el libro
    def devolver(self):
        if not self.disponible: #Si no esta prestado lo marco nuevamente como disponible
            self.disponible = True
            print(f"Libro '{self.titulo}' devuelto.")
        else:
            print(f"Libro '{self.titulo}' ya está disponible.")
   #muestro los datos importantes del libro:
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Disponibilidad: {'Disponible' if self.disponible else 'Prestado'}")


class Usuario: #defino una clase para representar a los usuarios que pueden tomar libros prestados.
    def __init__(self, nombre, id_usuario):  #Creo un constructor
        self.nombre = nombre
        self.id_usuario = id_usuario
        self.libros_prestados = []
    #Creo un metodo para tomar_prestado
    def tomar_prestado(self, libro):
        if libro.prestar(): # Si el libro se presta con éxito lo agrego a la lista de libros
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado '{libro.titulo}'.")
        else:
            print(f"{self.nombre} no pudo tomar prestado '{libro.titulo}'.")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
          libro.devolver()
          self.libros_prestados.remove(libro)
          print(f"{self.nombre} ha devuelto '{libro.titulo}'.")
        else:  #Si no se pudo prestar, lo informo.
          print(f"{self.nombre} no tiene prestado el libro '{libro.titulo}'.")
    #Metodo para mostrar libros prestados
    def mostrar_libros_prestados(self):
        if self.libros_prestados: # Aquí muestro qué libros tiene el usuario:
            print(f"Libros prestados por {self.nombre}:")
            for libro in self.libros_prestados:# Si tiene libros, los muestro uno por uno.
                libro.mostrar_info()
        else:  #Si no tiene ninguno, también lo digo.
            print(f"{self.nombre} no tiene libros prestados.")


libro1 = Libro("El tiempo","Jorge","editarial_cajas")

libro1.prestar()  #Llamo  a mi clase
libro1.mostrar_info() #Muestro la informnacion
libro1.devolver() #