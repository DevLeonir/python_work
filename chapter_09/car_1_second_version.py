"""Classe que pode ser usada para representar um carro"""

class Car:
    """Simples tentativa de reprensentar um carro"""

    def __init__(self, make, model, yer):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.yer = yer
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado elegantemente"""
        long_name = f"{self.yer} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro,
        em milhas"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Define a leitura do hodômetro para o valor fornecido.
        Rejeita a alteração se houver tentativas de reverter o hodômetro.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an adometer!")

    def increment_odometer(self, miles):
        """Adiciona a quantidade 
        fornecida á leitura do hodômetro
        """
        self.odometer_reading += miles

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