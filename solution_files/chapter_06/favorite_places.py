favorite_places = {
    'lais': ['tokyo', 'new york', 'london'],
    'leonardo': ['paris'],
    'leonir': ['rio de janeiro', 'sao paulo'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")