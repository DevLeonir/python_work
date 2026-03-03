def build_person(first_name, last_name, age=None):
    """Retorna um dicionário de informações sobre uma pessoa"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('leonir', 'kochenborger', age=29)
print(musician)