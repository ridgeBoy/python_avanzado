print("Ejercicio 1")
def Factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * Factorial(numero-1)


factorial = int(input("Número a calcular el factorial: "))
print("Resultado: " + str(Factorial(factorial)))
print(" ")
print("Ejercicio 2")
def mcd(numero1, numero2):
    if numero2 == 0:
        return numero1
    elif numero1 == 0:
        return numero2
    else:
        if numero1 > numero2:
            return mcd(numero1 - numero2, numero2)
        else:
            return mcd(numero1, numero2 - numero1)

numeroleido1 = int(input("Primer numero para calcular el MCD: "))
numeroleido2 = int(input("Segundo numero para calcular el MCD: "))
print("Resultado MCD: " + str(mcd(numeroleido1, numeroleido2)))
print(" ")
print("Ejercicio 3")
def potencia (base, exponente):
    if exponente <= 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("Base de la potencia: "))
exponente = int(input("Exponente de la potencia: "))
print("Resultado: " + str(potencia(base, exponente)))
print(" ")
print("Ejercicio 4")
def SumarVector(vector, elemento):
    if elemento == 0:
        return vector[elemento]
    else:
        return SumarVector(vector, elemento -1) + vector[elemento]

vectorenteros = [1,2,3,4,5,6,7,8,9]

print("vector de enteros: ", vectorenteros)
elementosasumar = int(input("¿Cuantos elementos quieres sumar? (0 - " + str(len(vectorenteros)) +") : "))

if (elementosasumar > 0) & (elementosasumar <= len(vectorenteros)):
    print("resultado: ", SumarVector(vectorenteros, elementosasumar-1))
else:
    print("ERROR: el número de elementos a sumar es incorrecto")