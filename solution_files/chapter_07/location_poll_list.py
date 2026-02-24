prompt = "Se pudesse visitar qualquer lugar do mundo, para onde iria? "
lugares = []

polling_active = True

while polling_active:
    lugar = input(prompt)

    lugares.append(lugar)

    repeat = input("Deseja continuar a pesquisa ? (sim/ nao)")

    if repeat.lower() == 'nao':
        polling_active = False
        print("\nObrigado pelas respostas!")

print("\n--- Resultado da pesquisa ---")

for lugar in lugares:
    print(f"Você gostaria de visitar {lugar.title()}.")