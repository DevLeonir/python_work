def build_person(first_name, last_name):
    """Retorna um dicionário de informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('leonir', 'kochenborger')
print(musician)