from math import pi

def calc_area(base, altura, tipo):
    resultado = None         # Valor inexistente
    if tipo == "R":          # Retangulo
        resultado = base * altura
    elif tipo == "T":        # Triangulo
        resultado = base * altura / 2
    elif tipo == "E":        # Elipse
        resultado = (base / 2) * (altura / 2) * pi
    
    return resultado

print("Retangulo 20x30: ", calc_area(20, 30, "R"))
print("Triangulo 45x32: ", calc_area(45, 32, "T"))
print("Elipse 10x15: ", calc_area(10, 15, "E"))
print("DEsconhecido 12x16: ", calc_area(12, 16, "X"))