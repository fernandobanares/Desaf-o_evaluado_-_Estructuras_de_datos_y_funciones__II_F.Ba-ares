import sys

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

umbral = float(sys.argv[1])

productos = []

def mayor_a():
    resultado = {}
    for k, v in precios.items():
        if v > umbral:
            resultado[k] = v
            return resultado

resultado = mayor_a()
print(resultado)