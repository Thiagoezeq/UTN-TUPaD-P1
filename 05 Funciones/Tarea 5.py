#Ejercicio 1
# Definición de la función
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Programa principal
imprimir_hola_mundo()

#Ejercicio 2
# Definición de la función
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Programa principal
nombre_ingresado = input("Ingrese su nombre: ")
saludo = saludar_usuario(nombre_ingresado)
print(saludo)

#Ejercicio 3
# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

# Programa principal
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

# Llamada a la función con los datos ingresados
informacion_personal(nombre, apellido, edad, residencia)

#Ejercico 4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"Área del círculo: {area:.2f}")
print(f"Perímetro del círculo: {perimetro:.2f}")

#Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"Equivale a {horas:.2f} horas.")

#Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)

#Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Infinito (división por cero)"
    return (suma, resta, multiplicacion, division)

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

resultados = operaciones_basicas(a, b)
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")

#Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Su IMC es: {imc:.2f}")

#Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return celsius * 9/5 + 32

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius:.2f}°C equivalen a {fahrenheit:.2f}°F")

#Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

promedio = calcular_promedio(a, b, c)
print(f"El promedio es: {promedio:.2f}")
