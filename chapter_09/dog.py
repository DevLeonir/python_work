class Dog:
    """Simples tentativa de modelar um cachorro"""
    def __init__(self, name, age):
        """Inicializa os atributos de nome e idade"""
        self.name = name
        self.age = age

    def sit(self):
        """Simula um cachorro sentado em resposta a um comando"""
        print(f"{self.name} is now sitting")

    def roll_over(self):
        """Simula um cachorro rolando em resposta a um comando"""
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
you_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

print(f"\nMy dog's name is {you_dog.name}.")
print(f"My dog is {you_dog.age} years old.")
you_dog.sit()
you_dog.roll_over()