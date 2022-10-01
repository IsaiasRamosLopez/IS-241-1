# Exercise 6
# Program Title
print('Programa Calcular Distancia Entre Dos Puntos');
# Input Data
print('Ingrese los sigueintes datos');
print('Para el primer punto: ');
x1 = float(input('Coordenada x: '));
y1 = float(input('Coordenada y: '));
print('Para el segundo punto: ');
x2 = float(input('Coordenada x: '));
y2 = float(input('Coordenada y: '));
# Resolution
distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5;
# Results
print(F'Distancia entre los dos puntos: {distance:.2f}');