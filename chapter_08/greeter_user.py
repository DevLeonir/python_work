def greet_users(names):
    """Exibe um simples hello para cada usuário na lista"""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)