def build_profile(first, last, **user_info):
    """Cria um dicionário contendo tudo o que sabemos sobre um usuário"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

my_profile = build_profile('leonir', 'kochenborger',
                                location='congonhas',
                                fild='programador',
                                hobby='games')
print(my_profile)