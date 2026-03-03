def make_pizza(size, *toppings):
    """Sintetiza a pizza que estamos prestes a fazer"""
    print(f"\nMaking a {size}-inch pizza whith the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrroms', 'green peppers', 'extra cheese')