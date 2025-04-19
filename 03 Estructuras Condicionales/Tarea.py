#Ejercicio 1

# Pedir la edad al usuario
edad = int(input("Por favor, ingresa tu edad: "))

# Verificar si es mayor o menor de edad
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")


#Ejercicio 2

#solicitamos al estudiante que ingrese la nota
Nota=int(input("ingrese la nota"))

#Verificamos si la nota  cumple o no los requisitos

if Nota >= 6:
    print("Aprobado")
else:
    print("desaprobado")

#Ejercicio 3

# Solicitar al usuario que ingrese un número
numero = int(input("Por favor, ingrese un número: "))

# Verificar si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#Ejercicio 4

# Solicitar al usuario que ingrese su edad
edad = int(input("Por favor, ingrese su edad: "))

# Determinar la categoría en base a la edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ejercicio 5

# Solicitar al usuario que ingrese una contraseña
contraseña = input("Por favor, ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificar la longitud de la contraseña
if len(contraseña) >= 8 and len(contraseña) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#ejercicio 6

import random
from statistics import mode, median, mean

# Generar una lista de 50 números aleatorios entre 1 y 100
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, la mediana y la media
moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Imprimir los valores calculados
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

# Comparar para determinar el sesgo
if media > mediana > moda:
    print("El sesgo es positivo o a la derecha.")
elif media < mediana < moda:
    print("El sesgo es negativo o a la izquierda.")
else:
    print("No hay sesgo.")

#ejercicio 7

# Solicitar al usuario que ingrese una frase o palabra
entrada = input("Por favor, ingrese una frase o palabra: ")

# Verificar si el último carácter es una vocal
if entrada[-1].lower() in 'aeiouáéíóú':
    entrada += '!'  # Añadir un signo de exclamación al final

# Imprimir el string resultante
print(entrada)

#ejercicio 8

# Solicitar al usuario su nombre
nombre = input("Por favor, ingrese su nombre: ")

# Solicitar al usuario la opción deseada
print("Elija una opción para su nombre:")
print("1. Mayúsculas")
print("2. Minúsculas")
print("3. Primera letra mayúscula")

opcion = input("Ingrese el número de la opción (1, 2 o 3): ")

# Procesar según la opción seleccionada
if opcion == '1':
    # Convertir el nombre a mayúsculas
    nombre_modificado = nombre.upper()
elif opcion == '2':
    # Convertir el nombre a minúsculas
    nombre_modificado = nombre.lower()
elif opcion == '3':
    # Convertir el nombre con la primera letra en mayúscula
    nombre_modificado = nombre.title()
else:
    nombre_modificado = "Opción no válida"

# Imprimir el nombre modificado
print("Nombre resultante:", nombre_modificado)

#ejercicio 9

# Solicitar al usuario la magnitud del terremoto
magnitud = float(input("Por favor, ingrese la magnitud del terremoto: "))

# Clasificar la magnitud según la escala de Richter
if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)"
elif magnitud >= 3 and magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)"
elif magnitud >= 4 and magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)"
elif magnitud >= 5 and magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)"
elif magnitud >= 6 and magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)"
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)"

# Imprimir la clasificación del terremoto
print(f"La magnitud del terremoto es {magnitud}, y se clasifica como: {clasificacion}")

#ejercicio 10

# Solicitar al usuario el hemisferio, mes y día
hemisferio = input("¿En qué hemisferio te encuentras? (N/S): ").strip().upper()
mes = int(input("Ingresa el mes del año (1-12): "))
dia = int(input("Ingresa el día del mes: "))

# Función para determinar la estación en el hemisferio norte
def estacion_norte(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        return "Invierno"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        return "Primavera"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        return "Verano"
    else:
        return "Otoño"

# Función para determinar la estación en el hemisferio sur
def estacion_sur(mes, dia):
    if (mes == 12 and dia >= 21) or (1 <= mes <= 3 and (mes != 3 or dia <= 20)):
        return "Verano"
    elif (mes == 3 and dia >= 21) or (4 <= mes <= 6 and (mes != 6 or dia <= 20)):
        return "Otoño"
    elif (mes == 6 and dia >= 21) or (7 <= mes <= 9 and (mes != 9 or dia <= 20)):
        return "Invierno"
    else:
        return "Primavera"

# Validar y determinar la estación según el hemisferio
if hemisferio == 'N':
    estacion = estacion_norte(mes, dia)
elif hemisferio == 'S':
    estacion = estacion_sur(mes, dia)
else:
    estacion = "Hemisferio no válido"

# Imprimir la estación correspondiente
print(f"La estación actual en el hemisferio {hemisferio} es: {estacion}")

