class User:
    """Exibe um resumo das informações de um usuário."""
    def __init__(self, first_name, last_name, age, city):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.city = city
        self.login_attempts = 0

    def describe_user(self):
        print(f"Nome: {self.first_name.title()} {self.last_name.title()}")
        print(f"Idade: {self.age}")
        print(f"Cidade: {self.city.title()}")

    def greet_user(self):
        print(f"Olá, {self.first_name.title()}! Seja bem vindo(a).\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.login_attempts}")
    
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"{self.login_attempts}")




# Criando intâncias
user_01 = User('carlos', 'silva', 40, 'belo horizonte')
user_02 = User('lorraine', 'souza', 29, 'sao paulo')
user_03 = User('ana', 'souza', 33, 'rio de janeiro')

# Chamando métodos
user_01.describe_user()
user_01.greet_user()

user_02.describe_user()
user_02.greet_user()

user_03.describe_user()
user_03.greet_user()

user_04 = User('leo', 'sales', 32, 'acre')

user_04.increment_login_attempts()
user_04.increment_login_attempts()
user_04.increment_login_attempts()
user_04.increment_login_attempts()

print(f"Esse é o valor atual de login_attempts: {user_04.login_attempts}")

user_04.reset_login_attempts()

print(f"login_attempts resetado com sucesso!")