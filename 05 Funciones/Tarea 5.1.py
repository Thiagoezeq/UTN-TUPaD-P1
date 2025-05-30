#Ejercicio 1
multiplos_de_4 = list(range(4, 101, 4))

# Mostrar la lista
print(multiplos_de_4)

#Ejercicio 2
mis_favoritos = ["chocolate", "películas", "guitarra", "montaña", "playa"]
print("El penúltimo elemento es:", mis_favoritos[-2])

#Ejercicio 3
lista_vacia = []

# Agregar tres palabras usando append
lista_vacia.append("sol")
lista_vacia.append("luna")
lista_vacia.append("estrella")

# Imprimir la lista resultante
print("Lista final:", lista_vacia)

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo (índice 1) por "loro"
animales[1] = "loro"

# Reemplazar el último (índice -1) por "oso"
animales[-1] = "oso"

# Imprimir la lista resultante
print("Lista modificada:", animales)

#Ejercicio 6
numeros = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Los dos primeros números son:", numeros[:2])

#Ejercicio 7
# Lista original
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los elementos en las posiciones 1 y 2
autos[1] = "mustang"
autos[2] = "camaro"

# Mostrar la lista modificada
print("Lista modificada:", autos)

#Ejercicio 8
# Crear lista vacía
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("Lista de dobles:", dobles)

#Ejercicio 9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" a la lista del tercer cliente usando append
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente
indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# d) Imprimir la lista resultante por pantalla
print(compras)

#Ejercicio 10
lista_anidada = [
    15,                   # posición 0
    True,                 # posición 1
    [25.5, 57.9, 30.6],   # posición 2, que es una lista con 3 elementos
    False                  # posición 3
]

print(lista_anidada)
