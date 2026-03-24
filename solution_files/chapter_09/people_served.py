class Restaurant:
    """Exibe uma mensagem com o nome do restaurante
      e o tipo de culinária."""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name.title()}")
        print(f"Tipo de comida: {self.cusine_type.title()}")
    
    def open_restaurant(self):
        print("O restaurante está aberto!")

    def set_number_served(self):
        self.number_served = 20
        print(f"Número de clientes atendidos em um dia: {self.number_served}")

restaurant = Restaurant('Cantinho Mineiro', 'Mineira')
restaurant.describe_restaurant()

print(f"Número de clientes atendidos: {restaurant.number_served}")

restaurant.number_served = 2

print(f"Número de clientes atendidos: {restaurant.number_served}")

restaurant.set_number_served()

