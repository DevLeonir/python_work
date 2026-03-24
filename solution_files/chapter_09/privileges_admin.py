# privileges_admin.py
from  user import User

class Privileges:
    """Representa privilégios de um administrador."""
    def __init__(self):
        self.privileges = [
            'pode adicionar postagem',
            'pode deletar postagem',
            'pode banir usuário'
            ]
    
    def show_privileges(self):
        print("Privilegios de um Administrador:")
        for privileges in self.privileges:
            print(f"- {privileges}")

class Admin(User):
    """Exibe um conjunto de privilegios de um administrador"""
    def __init__(self, first_name, last_name, age, city):
        super().__init__(first_name, last_name, age, city)
        self.privileges = Privileges()