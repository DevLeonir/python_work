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
        
    def upgrade_battery(self):
        """Atualiza a bateria para 65 kWh se ainda não for."""
        print("\nBateria atualizada para 65-kwh ")
        if self.battery_size < 65:
            self.battery_size = 65
        

class EletricCar(Car):
    """Representa aspectos de um carro, específico para um veículo elétrico"""

    def __init__(self, make, model, yer):
        """Inicializa os atributos da classe-pai
        em seguida inicia os atributso especificos
          para um carro elétrico."""
        super().__init__(make, model, yer)
        self.battery = Battery()

my_leaf = EletricCar('nissam', 'lef', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()