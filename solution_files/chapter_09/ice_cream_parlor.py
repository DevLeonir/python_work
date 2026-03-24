class Restaurant:
    """Exibe uma mensagem com o nome do restaurante
      e o tipo de culinária."""
    def __init__(self, restaurant_name, cuisine_type):

        self.restaurant_name = restaurant_name
        self.cusine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurante: {self.restaurant_name.title()}")
        print(f"Tipo de comida: {self.cusine_type.title()}")
    
    def open_restaurant(self):
        print("O restaurante está aberto!")

class IceCreamStand(Restaurant):
    """Representa uma sorveteria."""
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['morango', 'chocolate', 'uva']
    
    def show_flavors(self):
        print("Sabores disponíveis:")
        for flavors in self.flavors:
            print(f"- {flavors.title()}")

ice = IceCreamStand('Gelato', 'Sorvete')
ice.show_flavors()