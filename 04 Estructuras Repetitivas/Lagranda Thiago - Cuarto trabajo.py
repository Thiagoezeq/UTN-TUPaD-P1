# Ejercicio 1

for numero in range(0, 101):
    print(numero)

#ejercicio 2

numero = int(input("Ingrese un número entero: "))

# Convertimos el número a positivo en caso de que sea negativo
numero_abs = abs(numero)

# Convertimos a string y contamos los caracteres
cantidad_digitos = len(str(numero_abs))

print(f"El número tiene {cantidad_digitos} dígito(s).")

#ejercicio 3

# Solicitar los dos valores al usuario
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))

# Determinar el menor y el mayor para manejar cualquier orden de entrada
menor = min(inicio, fin)
mayor = max(inicio, fin)

# Sumar los valores entre los dos números, excluyéndolos
suma = 0
for numero in range(menor + 1, mayor):
    suma += numero

print(f"La suma de los números entre {inicio} y {fin}, excluyéndolos, es: {suma}")

#ejercicio 4

suma_total = 0

while True:
    numero = int(input("Ingrese un número entero (0 para terminar): "))
    if numero == 0:
        break
    suma_total += numero

print(f"La suma total de los números ingresados es: {suma_total}")

#ejercicio 5

import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0
acertado = False

print("¡Adivina el número secreto entre 0 y 9!")

while not acertado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1
    
    if intento == numero_secreto:
        acertado = True
        print(f"¡Correcto! Adivinaste el número en {intentos} intento(s).")
    else:
        print("Incorrecto. Intenta de nuevo.")

#ejercicio 6

for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

#ejercicio 7

# Solicitar al usuario un número entero positivo
numero = int(input("Ingrese un número entero positivo: "))

# Verificar que el número sea positivo
if numero >= 0:
    suma = 0
    for i in range(0, numero + 1):
        suma += i
    print(f"La suma de los números desde 0 hasta {numero} es: {suma}")
else:
    print("Por favor, ingrese un número entero positivo.")

#ejercicio 8

# Puedes cambiar esta variable para probar con menos números
cantidad_numeros = 100

# Contadores
pares = 0
impares = 0
positivos = 0
negativos = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    numero = int(input("Número: "))
    
    # Par o impar
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    # Positivo o negativo
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

# Mostrar resultados
print("\n--- Resultados ---")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#ejercicio 9

# Cambia este valor si deseas probar con menos números
cantidad_numeros = 100

suma_total = 0

print(f"Ingrese {cantidad_numeros} números enteros:")

for _ in range(cantidad_numeros):
    numero = int(input("Número: "))
    suma_total += numero

media = suma_total / cantidad_numeros

print(f"\nLa media de los {cantidad_numeros} números ingresados es: {media}")

#ejercicio 10

numero = input("Ingrese un número entero: ")

# Verificar si es negativo para conservar el signo
if numero.startswith('-'):
    numero_invertido = '-' + numero[:0:-1]
else:
    numero_invertido = numero[::-1]

print(f"El número invertido es: {numero_invertido}")