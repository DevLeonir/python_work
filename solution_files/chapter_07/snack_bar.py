sandwich_orders = ['hambúrger', 'hot-dog', 'sanduíche natural', 'x-tudo', 'bauru']
finished_sandwiches = []

while sandwich_orders:
    current_sandwiches = sandwich_orders.pop()
    print(f"Seu lanche {current_sandwiches.title()} está pronto!")
    finished_sandwiches.append(current_sandwiches)

print("\n--- Finished Sandwiches ---")

for number, sandwich in enumerate(finished_sandwiches):
    print(f"{number}. {sandwich.title()}")