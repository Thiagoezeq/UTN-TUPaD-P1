# Ejercicio 1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Solicitar número al usuario
limite = int(input("Ingresá un número: "))
for i in range(1, limite + 1):
    print(f"{i}! = {factorial(i)}")

# Ejercicio 2
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("¿Hasta qué posición querés ver la serie de Fibonacci?: "))
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

# Ejercicio 3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

base = int(input("Base: "))
exponente = int(input("Exponente: "))
print(f"{base}^{exponente} = {potencia(base, exponente)}")

# Ejercicio 4
def decimal_a_binario(n):
    if n == 0:
        return ''
    return decimal_a_binario(n // 2) + str(n % 2)

numero = int(input("Ingresá un número decimal: "))
binario = decimal_a_binario(numero)
# Si el número es 0, hay que imprimir "0"
print(f"Binario: {binario if binario != '' else '0'}")

# Ejercicio 5
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input("Ingresá una palabra: ").lower()
print("¿Es palíndromo?", es_palindromo(texto))

# Ejercicio 6
def suma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + suma_digitos(n // 10)

numero = int(input("Ingresá un número: "))
print("Suma de los dígitos:", suma_digitos(numero))

# Ejercicio 7
def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

nivel = int(input("Bloques en el nivel más bajo: "))
print("Total de bloques necesarios:", contar_bloques(nivel))

# Ejercicio 8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    coincidencia = 1 if numero % 10 == digito else 0
    return coincidencia + contar_digito(numero // 10, digito)

n = int(input("Ingresá un número: "))
d = int(input("¿Qué dígito querés contar?: "))
print(f"El dígito {d} aparece {contar_digito(n, d)} veces.")


