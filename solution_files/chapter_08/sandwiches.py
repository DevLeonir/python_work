def make_sanwiches(*toppings):
    """ Exibe um resumo do sandíche que esta sendo solicitado"""
    print("Montando sanduíche com:")

    for topping in toppings:
        print(f"- {topping}")

make_sanwiches("Pão")
make_sanwiches("Pão", "Carne")
make_sanwiches("Pão", "Carne", "Queijo")