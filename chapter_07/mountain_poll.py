responses = {}
# Define uma flag para sinalizar que a pesquisa está ativa
polling_active = True

while polling_active:
    # Solicita o nome e a resposta do participante
    name = input("\nWhat is you name? ")
    response = input("which mountain would you like to climb someday? ")

    # Armazena a resposta no dicionário
    responses[name] = response

    # Detecta se mais alguém participará de pesquisa
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# A pesquisa está completa. Mostra os resultados.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")