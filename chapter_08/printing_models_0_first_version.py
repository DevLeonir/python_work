# Começa com alguns designs que precisam ser impressos.
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simula a impressão de cada design, até que não reste nenhum
# Passa cada design para completed_models após impressão
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f"Printing model: {current_design}")
    completed_models.append(current_design)

# Exibe todos os modelos concluídos
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)