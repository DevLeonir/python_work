guests = ['lorraine', 'andreia', 'leonir']

# Convida todos para jantar.
print(f"\nHello {guests[0].title()}! do you want to have dinner with me?")

print(f"Hello {guests[1].title()}! do you want to have dinner with me?")

print(f"Hello {guests[2].title()}! do you want to have dinner with me?")

print(f"{guests[2].title()} won't have dinner ")

# Modifica a lista 'leonir' por 'leonardo'.
guests[2] = 'leonardo'

# Convida todos para jantar com a lita alterada.
print(f"\nHello {guests[0].title()}! do you want to have dinner with me?")

print(f"Hello {guests[1].title()}! do you want to have dinner with me?")

print(f"Hello {guests[2].title()}! do you want to have dinner with me?")

# Informa que encontrou uma mesa maior.
print(f"\nI found a bigger table.")

# Adiciona um novo convidado no inicio da lista.
guests.insert(0, 'lais')

# Adiciona um novo convidado no meio da lista.
guests.insert(2, 'sandra')

# Adiciona um novo convidado no final da lista.
guests.append('adilson')

print(f"\nHello {guests[0].title()}! do you want to have dinner with me?")

print(f"Hello {guests[1].title()}! do you want to have dinner with me?")

print(f"Hello {guests[2].title()}! do you want to have dinner with me?")

print(f"Hello {guests[3].title()}! do you want to have dinner with me?")

print(f"Hello {guests[4].title()}! do you want to have dinner with me?")

print(f"Hello {guests[5].title()}! do you want to have dinner with me?")

# Informa que pode convidar apenas duas pessoas.
print(f"\nI can only invite two people.")
#print(guests)

# remove e informa que lamenta não poder convidar para jantar.
name = guests.pop()
print(f"{name} I'm sorry I couldn't invite you to dinner")
#print(guests)

name = guests.pop()
print(f"{name} I'm sorry I couldn't invite you to dinner")
#print(guests)

name = guests.pop()
print(f"{name} I'm sorry I couldn't invite you to dinner")
#print(guests)

name = guests.pop()
print(f"{name} I'm sorry I couldn't invite you to dinner")
#print(guests)

# Convida as ultimas duas pessoas restantes para jantar
print(f"\nHello {guests[0].title()}! do you want to have dinner with me?")

print(f"Hello {guests[1].title()}! do you want to have dinner with me?")

# Remove os ultimos dois nomes da lista.
del(guests[0])
#print(guests)
del(guests[0])

# Exibe a lista para ter certeza de que está vazia.
print(guests)