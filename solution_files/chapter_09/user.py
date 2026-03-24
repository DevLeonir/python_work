# user.py
class User:
    """Exibe um resumo das informações de um usuário."""
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city

    def describe_user(self):
        print(f"Nome: {self.first_name.title()} {self.last_name.title()}")
        print(f"Idade: {self.age}")
        print(f"Cidade: {self.city.title()}")

    def greet_user(self):
        print(f"Olá, {self.first_name.title()}! Seja bem vindo(a).\n")