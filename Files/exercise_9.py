# Exercise 9
# Program Title
print('Programa Calcular Total a Pagar');
# Constantes
ltGallon = 3.74;
priceLt = 4.04;
# Input Data
consumption = float(input('Ingrese candtidad Consumida: '));
# Resolution
totalPay = (consumption * priceLt) * ltGallon;
# Results
print(F'Total a Pagar: {totalPay:.2f}');