# Exercise 3
# Program Title
print('Programa Puntaje Final\nIngrese los siguientes datos:');
# Input Data
correctAnswers = int(input('Respuestas correctas: '));
incorrectAnswers = int(input('Respuestas incorrectas: '));
blankAnswers = int(input('Respuestas blanco:'));
# Resolution
score = correctAnswers * 3 + incorrectAnswers * -1;
# Results
print(F'Puntaje final: {score}');