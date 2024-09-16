# Título: Función que calcula la media de tres números
def calcular_media():
    print("Hola, vamos a calcular la media de 3 números")

    while True:  # Bucle para manejar errores sin usar recursividad
        try:
            numero_uno = float(input("Ingresa el primer número: "))
            numero_dos = float(input("Ingresa el segundo número: "))
            numero_tres = float(input("Ingresa el tercer número: "))
        except ValueError:
            print("Debes ingresar un número válido. Intenta de nuevo.")
        else:
            media = (numero_uno + numero_dos + numero_tres) / 3
            print(f"La media de los tres números es: {media}")
            break  # Salir del bucle si todo es correcto


calcular_media()
