# Importa a função randint para gerar números aleatórios
from random import randint

class Die:
    """Representa um dado que pode ser jogado com número de lados variáveis."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Retorna um valor aleatório entre 1 e o número de lados do dado."""
        return randint(1, self.sides)

# Criação dos dados
die = Die() # Dados com 6 lados
die10 = Die(10) # Dados com 10 lados
die20 = Die(20) # Dados com 20 lados

# Jogando cada dado 10 vezes
print("Dado com 6 lados:")
for _ in range(10):
    print(die.roll_die())

print("\nDado com 10 lados:")
for _ in range(10):
    print(die10.roll_die())

print("\nDado com 20 lados:")
for _ in range(10):
    print(die20.roll_die())