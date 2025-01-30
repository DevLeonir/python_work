locations = ['cristo redentor', 'coliseu', 'pirâmides', 'torre eiffel', 'grand canyon']

# Exibe a lista em ordem original.
print(locations)

# Exibe a lista em ordem alfabética.
print(sorted(locations))
# Mostra que a lista ainda está em ordem original.
print(locations)

# Exibe a lista em ordem alfabética reversa.
print(sorted(locations, reverse=True))
# Demostra que a lista ainda está em ordem original.
print(locations)

# Altera a ordem da lista.
locations.reverse()
print(locations)

# Altera a ordem da lista novamente.
locations.reverse()
print(locations)

# Altera a lista em ordem alfabética.
locations.sort()
print(locations)

# Altera a lista em ordem alfabética reversa.
locations.sort(reverse=True)
print(locations)