import sys

precios = {'Notebook': 700000,
           'Teclado': 25000,
           'Mouse': 12000,
           'Monitor': 250000,
           'Escritorio': 135000,
           'Tarjeta de Video': 1500000}

umbral = float(sys.argv[1])

if len(sys.argv) > 2:
    umbral_segundo = str(sys.argv[2]).lower()
else:
    umbral_segundo = "mayor" 
    
def filtrar_precios():
    resultado = {}
    if umbral_segundo == "menor":
        for k, v in precios.items():
            if v < umbral:
                resultado[k] = v
    elif umbral_segundo == "mayor":
        for k, v in precios.items():
            if v > umbral:
                resultado[k] = v
    else:
        raise ValueError("Lo sentimos, no es una operación válida.")
    
    return resultado

mayores_o_menores = filtrar_precios()
print(f"Los productos filtrados son: {', '.join(mayores_o_menores.keys())}")
