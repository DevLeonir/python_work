pets = {
    'cat': {
        'type': 'felino',
        'owner': 'leonardo',
    },

    'dog': {
        'type': 'canine',
        'owner': 'lais',
    },

    'bird': {
        'type': 'avian',
        'owner': 'leonir',
    },

    'wolf': {
        'type': 'canine',
        'owner': 'lorraine',
    },
}

for animals, info in pets.items():
    print(f"\nAnimals: {animals.title()}")
    type = info['type']
    owner = info['owner']

    print(f"\tType: {type.title()}")
    print(f"\tOwner: {owner.title()}")