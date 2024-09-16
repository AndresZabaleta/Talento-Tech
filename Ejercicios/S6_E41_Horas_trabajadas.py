def calcular_sueldo():
    # Definir una función llamada calcular_sueldo
    horas = int(input("Ingrese el número de horas trabajadas: "))
    # Solicitar al usuario que ingrese el número de horas trabajadas, convertirlo a entero y almacenarlo en la variable 'horas'
    valor_hora = float(input("Ingrese el valor de la hora de trabajo: "))
    # Solicitar al usuario que ingrese el valor de la hora de trabajo, convertirlo a flotante y almacenarlo en la variable 'valor_hora'
    print(f"El pago que le corresponde es: {horas * valor_hora}")
    # Calcular el pago multiplicando las horas trabajadas por el valor de la hora y mostrar el resultado

calcular_sueldo()
# Llamar a la función calcular_sueldo para ejecutar el código