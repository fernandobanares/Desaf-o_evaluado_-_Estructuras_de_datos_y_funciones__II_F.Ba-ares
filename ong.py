import math

def calcular_factorial(i):
    factorial = math.factorial(i)
    return factorial

def calcular_producto(lista):
    productoria = 1
    for numero in lista:
        productoria *= numero
    return productoria

def calcular(x, y, z):
    if type(x) == int:
        print(f"El factorial de {x} es {calcular_factorial(x)}")
    elif type(x) == list:
        print(f"La productoria de {x} es {calcular_producto(x)}")
        
    if type(y) == int:
        print(f"El factorial de {y} es {calcular_factorial(y)}")
    elif type(y) == list:
        print(f"La productoria de {y} es {calcular_producto(y)}")
        
    if type(z) == int:
        print(f"El factorial de {z} es {calcular_factorial(z)}")
    elif type(z) == list:
        print(f"La productoria de {z} es {calcular_producto(z)}")

calcular([1, 2, 3], 4, 2)
