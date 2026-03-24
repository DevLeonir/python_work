# Importando múltiplas classes de um módulo
from car_1_second_version import Car, EletricCar

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Importando um módulo inteiro
import car_1_second_version

my_mustang = car_1_second_version.Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = car_1_second_version.EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Importando todas as classes de um módulo
from car_1_second_version import *

# Importando um módulo para um módulo
from car import Car
from eletric_car import EletricCar
my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())

my_leaf = EletricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Usando aliases
from eletric_car import EletricCar as EC
my_leaf = EC('nissan', 'leaf', 2024)

# Associando um alias a um módulo
import eletric_car as ec
my_leaf = ec.EletricCar('nissan', 'leaf', 2024)
