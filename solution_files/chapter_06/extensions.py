aliens = {
    'alien_0': {
        'color': 'green',
        'points': 5,
    },

    'alien_1': {
        'color': 'yellow',
        'points': 10,
    },

    'alien_2': {
        'color': 'red',
        'points': 15,
    },
}

for aliens_name, aliens_info in aliens.items():
    print(f"\n{aliens_name}:")
    color = aliens_info['color']
    points = aliens_info['points']

    print(f"\tColor: {color.title()}")
    print(f"\tPoints: {points}")


# First version

#alien_0 = {'color': 'green','points': 5,}

#alien_1 = {'color': 'yellow','points': 10,}

#alien_2 = {'color': 'red','points': 15,}

#aliens = [alien_0, alien_1, alien_2]

#for alien in aliens:
#    print(alien)