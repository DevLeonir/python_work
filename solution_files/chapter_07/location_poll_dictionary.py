prompt = "Se pudesse visitar qualquer lugar do mundo, para onde iria? "
lugares = {}

polling_active = True

while polling_active:
    nome = input("Qual é o seu nome? ")
    lugar = input(prompt)

    lugares[nome] = lugar

    repeat = input("Deseja continuar a pesquisa ? (sim/ nao)")

    if repeat.lower() == 'nao':
        polling_active = False
        print("\nObrigado pelas respostas!")

print("\n--- Resultado da pesquisa ---")

for nome, lugar in lugares.items():
    print(f"{nome.title()} gostaria de visitar {lugar.title()}.")