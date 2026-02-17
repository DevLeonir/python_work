# Cria uma lista vazia para armazenar alienígenas
aliens = []

# Cria 30 alienígenas verdes
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Exibe os primeiros 5 alienígenas
for alien in aliens[:5]:
    print(alien)
print("...")

# Exibe quantos alienígenas foram criados 
print(f"Total number of aliens: {len(aliens)}")