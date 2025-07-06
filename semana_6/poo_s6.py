class Empleado:
    def __init__(self, nombre):
        self._nombre = nombre  # Atributo protegido (convención en Python)

    def get_nombre(self):
        return self._nombre

    def trabajar(self):
        print(f"{self._nombre} está realizando tareas generales.")


class Desarrollador(Empleado):
    def __init__(self, nombre):
        super().__init__(nombre)

    def trabajar(self):
        print(f"{self.get_nombre()} está programando en Java.")


def main():
    e = Empleado("Ana")            # Instancia de la clase base
    d = Desarrollador("Darwin")   # Instancia de la clase derivada

    e.trabajar()  # Llamada al metodo de la clase base
    d.trabajar()  # Llamada al metodo sobrescrito (polimorfismo)

    # Acceso al nombre mediante encapsulación
    print("Nombre del desarrollador:", d.get_nombre())


if __name__ == "__main__":
    main()