# sumar dos números
def suma(a, b):
    return a + b

# restar dos números
def resta(a, b):
    return a - b

# multiplicar dos números
def multiplicacion(a, b):
    return a * b

# dividir dos números
def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero."
    return a / b

# Calculadora
def calculadora():
    print("Calculadora Simple")
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    opcion = input("Elige la operación (1/2/3/4): ")

    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if opcion == '1':
        resultado = suma(num1, num2)
    elif opcion == '2':
        resultado = resta(num1, num2)
    elif opcion == '3':
        resultado = multiplicacion(num1, num2)
    elif opcion == '4':
        resultado = division(num1, num2)
    else:
        resultado = "Opción no válida"

    print("Resultado:", resultado)

