sandwich_orders = ['hambúrger', 'pastrami', 'hot-dog', 'pastrami', 'sanduíche natural', 'pastrami', 'x-tudo', 'pastrami', 'bauru']
finished_sandwiches = []

print("Estamos sem o lanche Pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"Seu lanche {current_sandwiches.title()} está pronto!")
    finished_sandwiches.append(current_sandwiches)

print("\n--- Finished Sandwiches ---")

for number, sandwich in enumerate(finished_sandwiches):
    print(f"{number}. {sandwich.title()}")