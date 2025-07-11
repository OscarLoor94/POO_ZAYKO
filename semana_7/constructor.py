"""crearemos una clase llamada Contador que simplemente cuenta hasta un número específico y
muestra un mensaje al ser destruida.
"""

class Contador:  #Creamos una clase llamada contador
    def __init__(self, limite):
        """Creamos un constructor que inicializa el límite del contador,"""
        self.limite = limite
        self.contador = 0  #Inciamos el contador en 0
        print(f"Contador iniciado hasta {self.limite}.")  #Imprimimos un mensaje que nos va aindicar hasta que numero recorre

    def contar(self): #Creamos un metodo para contar
        while self.contador < self.limite:  #Utilizamos el bucle while y mientras el contador sea menor al limite entra
            print(self.contador) #Imrpimimos
            self.contador += 1  #Summamos en 1 el contador

    def __del__(self):  #Creamos el destructor que muestra un mensaje al destruir la instancia.
        print(f"Contador destruido después de contar hasta {self.contador}.")  #Imprimimos

# Crear una instancia de la clase Contador y damos parametros
mi_contador = Contador(5)

# Contar hasta el límite
mi_contador.contar()  #Utilizamos nuestra instancia y nos va imprimir el contador el cual inica desde 0 hasta 5

# Eliminar la instancia para activar el destructor
del mi_contador