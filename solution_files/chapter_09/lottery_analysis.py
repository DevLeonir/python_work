from random import choice

# Cria tupla com números e letras
lottery = (1, 3, 5, 2, 7, 8, 9, 4, 6, 0, 'a', 'e', 'b', 'c', 'd')

# Seu bilhete
my_ticket = (1, 'a', 3, 'b')

attempts = 0

# Primeiro sorteio
drawn = (choice(lottery),choice(lottery),choice(lottery),choice(lottery))

# Continua até ganhar
while drawn != my_ticket:
    attempts += 1

    drawn = (choice(lottery),choice(lottery),choice(lottery),choice(lottery))


print(f"Seu bilhete: {my_ticket}")
print(f"Bilhete vencedor: {drawn}")
print(f"Total de tentativas: {attempts}")