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
#print(guests)

# Adiciona um novo convidado no meio da lista.
guests.insert(2, 'sandra')
#print(guests)

# Adiciona um novo convidado no final da lista.
guests.append('adilson')
#print(guests)

print(f"\nHello {guests[0].title()}! do you want to have dinner with me?")

print(f"Hello {guests[1].title()}! do you want to have dinner with me?")

print(f"Hello {guests[2].title()}! do you want to have dinner with me?")

print(f"Hello {guests[3].title()}! do you want to have dinner with me?")

print(f"Hello {guests[4].title()}! do you want to have dinner with me?")

print(f"Hello {guests[5].title()}! do you want to have dinner with me?")