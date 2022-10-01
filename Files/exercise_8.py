# Exercise 8
# Program Title
print('Programa Calcular Perímetro y Superficie');
# Input Data
print('Ingrese los datos:');
base = float(input('[1] Base: '));
height = float(input('[2] Altura: '));
# Resolution
perimeter = 2 * (base + height);
surface = base * height;
# Results
print(F'El perímetro es {perimeter:.2f} y su superficie es {surface:.2f}');