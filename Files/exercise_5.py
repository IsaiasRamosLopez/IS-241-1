# Exercise 5
import math
# Program Title
print('Programa Calcular Número de Micro Discos');
# Input Data
storage = float(input('Ingrese tamaño del almacenamiento: '));
# Resolution
numberDiscs = (storage * 1024) / 1.44;
# Results
print(F'Número de discos necesarios: {math.ceil(numberDiscs)}');
