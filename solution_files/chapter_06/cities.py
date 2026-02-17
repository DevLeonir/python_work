cities = {
    'toledo': {
        'country': 'brasil.',
        'population': 156000,
        'fact': 'Capital Nacional do Agronegócio.',
    },

    'congonhas': {
        'country': 'brasil.',
        'population': 55000,
        'fact': 'Santuário do Bom Jesus de Matosinhos.',
    },

    'rio de janeiro': {
        'country': 'brasil.',
        'population': 6200000,
        'fact': 'Cristo Redentor, uma das 7 maravilhas do mundo.',
    },
}

for city, info_city in cities.items():
    print(f"\n{city.title()}'s:")
    country = info_city['country']
    population = info_city['population']
    fact = info_city['fact']

    print(f"\tCountry: {country.title()}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {fact.title()}")