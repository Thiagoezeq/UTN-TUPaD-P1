#Ejercicio 1

print("Hola mundo")

#Ejercicio 2

print("Hola, ¿Como te llamas?")

#Colocamos el nombre

nombre=input("Ingresar nombre:")

#Saludamos acorde el nombre que coloque

print(f"Hola {nombre}!")

#Ejercicio 3

nombre=input("Ingrese su nombre:")
apellido=input("Ingrese su apellido:")
edad=input("Ingrese su edad:")
país=input("Ingrese su país:")

print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {país}") 

#Ejercicio 4

import math
#Solicitamos el radio del circulo
radio=float(input("Ingrese el radio del circulo:"))
Area=math.pi * radio ** 2 
Perimetro=2 * math.pi * radio 
#Se muestran los resultados
print(f"El area del circulo es {Area:.2f}")
print(f"El perimetro del circulo es {Perimetro:.2f}")

#Ejercicio 5

# Cantidad de segundos
segundos=float(input("Coloque cantidad de segundos:")) 
horas = segundos // 3600
print(f"{segundos} segundos son {horas} hora")

#ejercicio 6
print("Tablas de multiplicar")
numero = int(input("Coloque el número para ver su tabla de multiplicar: "))
for i in range(1, 11):  
    final = numero * i  
    print(f"{numero} x {i} = {final}")  

#Ejercicio 7

print("operaciones aritmeticas")
numero1=int(input("Coloque su número"))
numero2=int(input("Coloque su segundo número"))
suma=numero1+numero2 
resta=numero1-numero2
multiplicación=numero1*numero2
divición=numero1/numero2

print(f"{numero1} + {numero2} = {suma}, {numero1} - {numero2} = {resta}, {numero1} x {numero2} = {multiplicación}, {numero1} / {numero2} = {divición}")

#ejercicio 8

print("Calculo de masa corporal")
Peso=float(input("Coloque su peso:"))
Altura=float(input("Coloque su estatura:"))
IMC= Peso/Altura**2
print(f"Si su peso es {Peso} y su Altura es {Altura}, Su IMC es de {IMC:.2f}")

#ejercicio 9

celsius = float(input("Ingrese la temperatura en grados Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"La temperatura de {celsius} grados Celsius es equivalente a {fahrenheit:.2f} grados Fahrenheit.")

#ejercicio 10 

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))
promedio = (numero1 + numero2 + numero3) / 3
print(f"El promedio de los tres números es: {promedio:.2f}")

