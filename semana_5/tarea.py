def convertir_kilometros_a_millas(kilometros: float) -> float:  #Declaramos una función que va a tener como parametro un valor flotante
    #Convierte kilómetros a millas.""
    return kilometros * 0.621371

def convertir_millas_a_kilometros(millas: float) -> float:  #Declaramos una funcion que va a convertir millas a km
    #Convierte millas a kilómetros.
    return millas / 0.621371

def main():
    # Solicitar al usuario la cantidad de kilómetros
    kilometros_str = input("Ingrese la distancia en kilómetros: ")  # Pedimos al usuario que ingrese los kilometros
    kilometros = float(kilometros_str)  # Convertimos los kilometros a millas en flotante

    # Convertir a millas
    millas = convertir_kilometros_a_millas(kilometros)  #Llamamos a nuestra función y pasamos el parametro
    print(f"{kilometros} kilómetros son {millas:.2f} millas.")  # Imprimimos

    # Solicitar al usuario la cantidad de millas
    millas_str = input("Ingrese la distancia en millas: ")  # Pedimos al usuario que ingrese la distancia de millas
    millas = float(millas_str)  # float

    # Convertir a kilómetros
    kilometros_convertidos = convertir_millas_a_kilometros(millas)
    print(f"{millas} millas son {kilometros_convertidos:.2f} kilómetros.")  # Imprimimos


#Llamos a main para ejecutar
if __name__ == "__main__":
    main()