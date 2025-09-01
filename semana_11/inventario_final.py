import json
import os


class Item:  # Creamos nuestra clase Item
    def __init__(self, id_item, nombre, cantidad, precio):  # Constructor con atributos
        self.id_item = id_item
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_id(self):
        return self.id_item

    def get_nombre(self):
        return self.nombre

    def get_cantidad(self):
        return self.cantidad

    def get_precio(self):
        return self.precio

    def set_cantidad(self, cantidad):  # metodo para la cantidad
        self.cantidad = cantidad

    def set_precio(self, precio):  # metodo precio
        self.precio = precio

    def to_dict(self):
        """Convierte el objeto Item a un diccionario para serialización JSON"""
        return {
            "id_item": self.id_item,
            "nombre": self.nombre,
            "cantidad": self.cantidad,
            "precio": self.precio
        }


class Inventario:

    def __init__(self):
        self.items = {}  # Usamos un diccionario en lugar de una lista para acceso más rápido por ID
        self.archivo = "inventarios.json"  # Nombre del archivo donde se almacenarán los datos
        self.cargar_archivo()  # Cargamos los datos del archivo al inicializar

    # Creamos el metodo para el archivo json
    def guardar_archivo(self):
        try:
            # Convertimos todos los items a diccionarios
            items_dict = [item.to_dict() for item in self.items.values()]

            # Guardamos en formato JSON con indentación para mejor legibilidad
            with open(self.archivo, "w") as f:
                json.dump(items_dict, f, indent=4)

            print(f"Cambios guardados en archivo: {os.path.abspath(self.archivo)}")
        except Exception as e:
            print(f"Error al guardar en archivo: {str(e)}")

    # metodo json
    def cargar_archivo(self):
        try:
            with open(self.archivo, "r") as f:  # Abrimos el archivo en modo lectura
                datos_json = json.load(f)  # Cargamos los datos JSON del archivo
                for dato in datos_json:  # Iteramos a través de cada elemento en el JSON
                    # Creamos un nuevo objeto Item con los datos leídos
                    item = Item(
                        dato["id_item"],  # ID del producto
                        dato["nombre"],   # Nombre del producto
                        int(dato["cantidad"]),  # Convertimos cantidad a entero
                        float(dato["precio"])   # Convertimos precio a flotante
                    )
                    self.items[item.get_id()] = item  # Almacenamos el item usando su ID como clave para búsqueda O(1)
            print(f"Inventario cargado del archivo: {len(self.items)} productos.")  # Mostramos cuántos productos se cargaron
        except FileNotFoundError:  # Capturamos error si el archivo no existe
            print("Archivo JSON no encontrado. Se creará uno nuevo al guardar.")
        except json.JSONDecodeError:
            print(f"Error: El archivo {self.archivo} no tiene un formato JSON válido.")
        except Exception as e:  # Capturamos cualquier otro tipo de error
            print(f"Error al cargar el archivo: {str(e)}")  # Mostramos el mensaje de error

    def aña_item(self, item):
        if item.get_id() in self.items:  # Verificamos si el ID ya existe (búsqueda O(1) en diccionario)
            print("Error: El ID ya existe.")  # Mensaje de error
            return
        self.items[item.get_id()] = item  # Agregamos el nuevo item usando su ID como clave
        self.guardar_archivo()  # Guardamos los cambios
        print("Producto añadido.")  # Mensaje de éxito

    def el_item(self, id_item):
        if id_item in self.items:  # Verificamos si el ID existe (búsqueda O(1) en diccionario)
            del self.items[id_item]  # Eliminamos el item del diccionario
            self.guardar_archivo()  # Guardamos los cambios
            print("Producto eliminado.")  # Mensaje de éxito
            return
        print("Error: Producto no encontrado.")  # Mensaje de error

    def act_item(self, id_item, cantidad=None, precio=None):
        if id_item in self.items:  # Verificamos si el ID existe (búsqueda O(1) en diccionario)
            if cantidad is not None:  # Si la cantidad no es None
                self.items[id_item].set_cantidad(cantidad)  # Actualizamos la cantidad
            if precio is not None:  # Si el precio no es None
                self.items[id_item].set_precio(precio)  # Actualizamos el precio
            self.guardar_archivo()  # Guardamos los cambios
            print("Producto actualizado exitosamente.")  # Mensaje de éxito
            return
        print("Error: Producto no encontrado.")  # Mensaje de error

    def bus_item(self, nombre):
        result = []  # Lista para los resultados
        for item in self.items.values():  # Iteramos sobre los valores del diccionario
            if nombre.lower() in item.get_nombre().lower():  # Verificamos si el nombre está contenido
                result.append(item)  # Añadimos el item a los resultados
        return result  # Retornamos la lista de resultados

    def most_items(self):
        if len(self.items) == 0:
            print("No hay productos en el inventario.")
        else:
            print("\nLista de productos:")
            print("-" * 60)
            print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio ($)':<10}")
            print("-" * 60)
            for item in self.items.values():  # Iteramos sobre los valores del diccionario
                print(f"{item.get_id():<10} {item.get_nombre():<20} {item.get_cantidad():<10} {item.get_precio():<10.2f}")
            print("-" * 60)


def mostrar():
    inventario = Inventario()
    while True:  # Bucle para el menú
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar todos los productos")
        print("6. Salir")

        try: # Comienza el bloque de manejo de errores
            opcion = input("Seleccione una opción: ") #Pedimos al usuario que ingrese una opcion

            if opcion == '1':  # Añadir producto
                id_item = input("Ingrese ID del producto: ")
                nombre = input("Ingrese nombre del producto: ")
                cantidad = int(input("Ingrese cantidad: "))
                precio = float(input("Ingrese precio: "))
                item = Item(id_item, nombre, cantidad, precio)  #
                inventario.aña_item(item)

            elif opcion == '2':  # Eliminar producto
                id_item = input("Ingrese ID del producto a eliminar: ")
                inventario.el_item(id_item)

            elif opcion == '3':  # Actualizar producto
                id_item = input("Ingrese ID del item a actualizar: ")
                cantidad = input("Ingrese nueva cantidad : ")
                precio = input("Ingrese nuevo precio : ")
                inventario.act_item(id_item, int(cantidad) if cantidad else None,
                                            float(precio) if precio else None)


            elif opcion == '4':  # Buscar producto

                nombre = input("Ingrese nombre del item a buscar: ")

                resultados = inventario.bus_item(nombre)

                if resultados:  # Si hay resultados

                    print("\nResultados de la búsqueda:")

                    print("-" * 60)

                    print(f"{'ID':<10} {'Nombre':<20} {'Cantidad':<10} {'Precio ($)':<10}")

                    print("-" * 60)

                    for i in resultados:  # Iteramos sobre los resultados

                        print(f"{i.get_id():<10} {i.get_nombre():<20} {i.get_cantidad():<10} {i.get_precio():<10.2f}")

                    print("-" * 60)

                else:

                    print("No se encontraron productos.")  # Mensaje de no encontrado

            elif opcion == '5':  # Mostrar items
                inventario.most_items()

            elif opcion == '6':  # Salir
                print("Saliendo.")
                break  # Salimos del bucle

        except ValueError:   # Verificamos si hay error al convertir números
            print("Error: Por favor ingrese números válidos para cantidad y precio.")  #Imprimimos un mensaje de qu eingrese
        except Exception as e: #Colcoamos otro except para ver si hay cualquier otro tipo de error
            print(f"Error: {str(e)}")  #Imprimimos que hay un error



prod = mostrar()
print(prod)