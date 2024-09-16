# Función que calcula el Índice de Masa Corporal (IMC)
def indice_masa_corporal(peso, altura):
    # El IMC se calcula dividiendo el peso (kg) entre la altura al cuadrado (m^2)
    return peso / altura**2

# Función que clasifica el IMC basado en las categorías estándar de la OMS
def clasificacion_imc(imc):
    # Clasificación de delgadez severa si el IMC es menor de 16
    if imc < 16:
        return "Infrapeso: Delgadez Severa"
    # Clasificación de delgadez moderada si el IMC está entre 16 y 16.99
    elif imc < 17:
        return "Infrapeso: Delgadez Moderada"
    # Clasificación de delgadez aceptable si el IMC está entre 17 y 18.49
    elif imc < 18.5:
        return "Infrapeso: Delgadez Aceptable"
    # Clasificación de peso normal si el IMC está entre 18.5 y 24.99
    elif imc < 25:
        return "Peso Normal"
    # Clasificación de sobrepeso si el IMC está entre 25 y 29.99
    elif imc < 30:
        return "Sobrepeso"
    # Clasificación de obesidad tipo I si el IMC está entre 30 y 34.99
    elif imc < 35:
        return "Obeso: Tipo I"
    # Clasificación de obesidad tipo II si el IMC está entre 35 y 39.99
    elif imc < 40:
        return "Obeso: Tipo II"
    # Clasificación de obesidad tipo III si el IMC es mayor o igual a 40
    else:
        return "Obeso: Tipo III"

# Función principal que ejecuta el programa
def main():
    # Solicita al usuario su peso y lo convierte en un número de punto flotante
    peso = float(input("Introduce tu peso en kg: "))
    # Solicita al usuario su altura y lo convierte en un número de punto flotante
    altura = float(input("Introduce tu altura en m: "))
    # Calcula el IMC utilizando la función 'indice_masa_corporal'
    imc = indice_masa_corporal(peso, altura)
    # Muestra el IMC calculado, formateado con dos decimales
    print(f"Tu IMC es: {imc:.2f}")
    # Muestra la clasificación del IMC utilizando la función 'clasificacion_imc'
    print(f"Clasificación IMC: {clasificacion_imc(imc)}")

# Verifica si este archivo se está ejecutando directamente, y si es así, llama a la función 'main'
if __name__ == "__main__":
    main()
