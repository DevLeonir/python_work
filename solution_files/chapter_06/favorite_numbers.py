favorite_numbers = {
    'lais': [5, 2, 3],
    'leonardo': [3],
    'leonir': [7, 4, 5],
    'andreia': [9, 10],
    'lorraine': [2],
}

for names, numbers in favorite_numbers.items():
    print(f"\n{names.title()} Favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")

#for key, value in favorite_numbers.items():
    #print(f"O número favorito da {key.title()} é {value}")

#print(f"O número favorito da Lais é {favorite_numbers['lais']}.")
#print(f"O número favorito do Leonardo é {favorite_numbers['leonardo']}.")
#print(f"O número favorito da Leonir é {favorite_numbers['leonir']}.")
#print(f"O número favorito da Andreia é {favorite_numbers['andreia']}.")
#print(f"O número favorito da Lorraine é {favorite_numbers['lorraine']}.")