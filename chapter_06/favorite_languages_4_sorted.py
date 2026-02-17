favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# A saída mostra todos os nomes ordenados
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")