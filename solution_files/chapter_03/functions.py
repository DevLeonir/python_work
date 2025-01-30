countries = ['canadá', 'itália', 'brasil', 'frança']

# Exibe a quantidade de países que contem na lista.
num_countries = len(countries)
print(num_countries)

# Exibe a lista em ordem alfabética.
sorted_countries = sorted(countries)
print(sorted_countries)

# Adiciona Portugal no final da lista.
countries.append('portugal')
print(countries)

# Remove Itália da lista.
countries.remove('itália')
print(countries)

# Remove Canadá da lista.
popped_countries = countries.pop(0)
print(countries)
print(popped_countries) # Exibe o país que foi removido.

# Altera a lista em ordem alfabética.
countries.sort()
print(countries)

# Altera a ordem da lista.
countries.reverse()
print(countries)