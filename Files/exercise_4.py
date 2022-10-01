# Exercise 4
# Program Title
print('Programa Puntaje Total');
# Input Data
print('Ingresar Datos:');
gamesWon = int(input('Partidos Ganados: '));
lostMatches = int(input('Partidos Perdidos: '));
tiedMatches = int(input('Partidos Empatados: '));
# Resolution
finalScore = gamesWon * 3 + tiedMatches;
# Results
print('Puntaje Total:', finalScore);
