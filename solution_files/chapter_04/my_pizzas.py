pizzas = ['portuguesa', 'calabresa', 'muçarela', 'margarita']

friend_pizzas = pizzas[:]

pizzas.append('frango com catupiry')

friend_pizzas.append('da casa')

print("Minhas pizzas favoritas são:")
for pizza in pizzas:
    print(pizza.title())

print("\nMinhas pizzas favoritas são:")
for pizza in friend_pizzas:
    print(pizza.title())