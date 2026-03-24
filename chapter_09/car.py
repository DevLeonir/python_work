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