# Exercise 10
import math;
# Program Title
print('Programa Calcular Área y Volumen del Cilindro');
# Input Data
radius = float(input('Ingrese el radio: '));
height = float(input('Ingrese la altura: '));
# Resolution
area = 2 * math.pi * radius * (radius + height);
volume = math.pi * radius ** 2 * height;
# Results
print(F'El rea es {area:.2f} y el volumen es {volume:.2f}');