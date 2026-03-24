class Car:
    """Simples tentatiuva de representar um carro"""

    def __init__(self, make, model, yer):
        """Inicializa os atributos para descrever um carro"""
        self.make = make
        self.model = model
        self.yer = yer
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Retorna um nome descritivo, formatado e elegante"""
        long_name = f"{self.yer} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Exibe uma frase mostrando a quilometragem do carro"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, milage):
        """Define a leitura do hôdometro para o valor fornecido"""
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Adiciona a quantidade fornecida á leitura do hôdometro"""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Tanque está cheio"""
        print("Tank is full!")


class EletricCar(Car):
    """Representa aspectos de um carro, específico para um veículo elétrico"""

    def __init__(self, make, model, yer):
        """Inicializa os atributos da classe-pai
        em seguida inicia os atributso especificos
          para um carro elétrico."""
        super().__init__(make, model, yer)
        self.battery_size = 40

    def describe_battery(self):
        """Exibe uma frase descrevendo o tamanho da bateria"""
        print(f"This car has a {self.battery_size}-kwh battery.")
    
    def fill_gas_tank(self):
        """Carros elétricos não têm tanques ded gasolina"""
        print("This car doesn't have a gas tank!")

my_leaf = EletricCar('nissam', 'lef', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()