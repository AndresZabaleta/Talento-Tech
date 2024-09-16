# Función que suma dos números
def suma(num1, num2):
    # Retorna la suma de num1 y num2
    return num1 + num2

# Función que resta dos números
def resta(num1, num2):
    # Retorna la resta de num1 menos num2
    return num1 - num2

# Función que multiplica dos números
def multiplicacion(num1, num2):
    # Retorna la multiplicación de num1 por num2
    return num1 * num2

# Función que divide dos números
def division(num1, num2):
    try:
        # Intenta realizar la división de num1 entre num2
        return num1 / num2
    except ZeroDivisionError:
        # Captura la excepción si se intenta dividir entre cero
        print("Error: No se puede dividir entre cero.")
        return None  # Devuelve None si hay un error de división por cero

# Solicita al usuario ingresar el primer número y lo convierte a float
num1 = float(input("Ingresa el primer número: "))
# Solicita al usuario ingresar el segundo número y lo convierte a float
num2 = float(input("Ingresa el segundo número: "))

# Muestra el resultado de la suma llamando a la función suma
print(f"El resultado de la suma es {suma(num1, num2)}")
# Muestra el resultado de la resta llamando a la función resta
print(f"El resultado de la resta es {resta(num1, num2)}")
# Muestra el resultado de la multiplicación llamando a la función multiplicacion
print(f"El resultado de la multiplicación es {multiplicacion(num1, num2)}")

# Llama a la función division y almacena el resultado
resultado_division = division(num1, num2)
# Si el resultado de la división no es None (es decir, no hubo error), lo imprime
if resultado_division is not None:
    print(f"El resultado de la división es {resultado_division}")

