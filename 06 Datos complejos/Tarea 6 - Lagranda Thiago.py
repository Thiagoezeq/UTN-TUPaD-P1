# Ejercicio 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregamos frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Ejercicio 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Ejercicio 3
lista_frutas = list(precios_frutas.keys())
print(lista_frutas)

# Ejercicio 4
agenda = {}

for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    agenda[nombre] = telefono

consulta = input("Ingrese el nombre para buscar el número: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# Ejercicio 5
frase = input("Ingresá una frase: ")

palabras = frase.lower().split()
palabras_unicas = set(palabras)

# Diccionario de conteo
conteo = {}
for palabra in palabras:
    conteo[palabra] = conteo.get(palabra, 0) + 1

print("Palabras únicas:", palabras_unicas)
print("Frecuencia por palabra:", conteo)

# Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {nombre}: {promedio:.2f}")

# Ejercicio 7
parcial1 = {"Ana", "Juan", "Carlos", "Luisa"}
parcial2 = {"Carlos", "Luisa", "Pedro", "María"}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Ejercicio 8
stock = {
    "Leche": 10,
    "Pan": 20,
    "Huevos": 30
}

producto = input("Ingrese el producto para consultar o actualizar: ")

if producto in stock:
    agregar = int(input("Producto ya existe. ¿Cuántas unidades agregar?: "))
    stock[producto] += agregar
else:
    nuevo_stock = int(input("Producto nuevo. ¿Cuántas unidades tiene?: "))
    stock[producto] = nuevo_stock

print("Stock actualizado:", stock)

# Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "14:00"): "Clases",
    ("Viernes", "18:00"): "Gimnasio"
}

dia = input("Ingrese el día: ")
hora = input("Ingrese la hora: ")

evento = agenda.get((dia, hora), "No hay actividad registrada.")
print("Actividad:", evento)

# Ejercicio 10
paises = {
    "Argentina": "Buenos Aires",
    "Brasil": "Brasilia",
    "Francia": "París",
    "Italia": "Roma"
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
