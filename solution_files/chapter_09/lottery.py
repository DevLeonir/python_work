from random import choice

# Cria tupla com números e letras
lottery = (1, 3, 5, 2, 7, 8, 9, 4, 6, 0, 'a', 'e', 'b', 'c', 'd')

# Sorteia 4 valores
for _ in range(4):
    print(choice(lottery))

print("Qualquer bilhete que corresponda a esses 4 valores ganha o prêmio!")