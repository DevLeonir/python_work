class Restaurant:
    """Exibe três mensagens diferentes com o nome do 
    restaurante e o tipo de culinária."""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nRestaurante: {self.restaurant_name.title()}")
        print(f"Tipo de comida: {self.cusine_type.title()}")
    
    def open_restaurant(self):
        print("O restaurante está aberto!")

restaurant_01 = Restaurant('Sabor Mineiro', 'Brasileira')
restaurant_01.describe_restaurant()
restaurant_01.open_restaurant()

restaurant_02 = Restaurant('Bella Massa', 'Italiana')
restaurant_02.describe_restaurant()
restaurant_02.open_restaurant()

restaurante_03 = Restaurant('Sushi Ian', 'Japonesa')
restaurante_03.describe_restaurant()
restaurante_03.open_restaurant()