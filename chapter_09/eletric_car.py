"""Conjunto de classes que pode ser usado para representar carros elétricos"""

from car import Car

class Battery:
    """Simples tentativa de modelar uma bateria para um carro elétrico"""
    def __init__(self, battery_size=40):
        """Inicializa os atributos da bateria"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def get_range(self):
        """Exibe frase sobre a distancia que o carro percorre com esta bateria"""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")


class EletricCar(Car):
    """Representa aspectos de um carro, específico para um veículo elétrico"""

    def __init__(self, make, model, yer):
        """Inicializa os atributos da classe-pai
        em seguida inicia os atributso especificos
          para um carro elétrico."""
        super().__init__(make, model, yer)
        self.battery = Battery()