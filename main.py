def addmultiplenumbers(numbers):
    resultado = 0

    for number in range(len(numbers)):
        resultado = resultado + numbers[number]

    return resultado

def multiplymultiplenumbers(numbers):
    resultado = 1

    for number in range(len(numbers)):
        resultado = resultado * numbers[number]

    return resultado


def isiteven(num):
    resultado = False
    if num % 1 == 0 and num % 2 == 0:
      resultado = True
    else:
       resultado = False

    return resultado

def isitaninteger(num):
    resultado = False
    if num % 1 == 0:
      resultado = True
    else:
       resultado = False
    return resultado

def main():
    print("===== CALCULADORA =====")
    print("1. Sumar números")
    print("2. Multiplicar números")
    print("3. Comprobar si un número es entero y par")
    print("4. Comprobar si un número es entero")

    opcion = input("Selecciona una opción: ")

    if opcion == "1" or opcion == "2":

        cantidad = int(input("¿Cuántos números deseas ingresar? "))

        numbers = []

        for i in range(cantidad):
            num = float(input(f"Ingresa el número {i + 1}: "))
            numbers.append(num)

        if opcion == "1":
            resultado = addmultiplenumbers(numbers)
            print("Resultado de la suma:", resultado)

        else:
            resultado = multiplymultiplenumbers(numbers)
            print("Resultado de la multiplicación:", resultado)

    elif opcion == "3":
        num = float(input("Ingresa un número: "))

        resultado = isiteven(num)

        if resultado:
            print("El número es entero y par.")
        else:
            print("El número no es entero y par.")

    elif opcion == "4":
        num = float(input("Ingresa un número: "))

        resultado = isitaninteger(num)

        if resultado:
            print("El número es entero.")
        else:
            print("El número no es entero.")

    else:
        print("Opción no válida.")

if __name__=="__main__":
  main()