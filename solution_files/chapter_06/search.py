favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

search = ['jen', 'leonir', 'edward', 'andreia']

for name in search:
    if name in favorite_languages:
        print(f"{name.title()}, Obrigado pela resposta.")
    else:
        print(f"{name.title()}, Você está convidado a participar da pesquisa.")