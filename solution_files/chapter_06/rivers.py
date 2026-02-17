rivers = {
    'nilo': 'egito',
    'amazonas': 'brasil',
    'yangtzé': 'china',
}

for key, value in rivers.items():
    print(f"O {key.title()} atravessa o {value.title()}.")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())