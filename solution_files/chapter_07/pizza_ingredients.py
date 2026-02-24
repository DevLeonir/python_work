ingredientes = []

prompt = "\nDigite os ingredientes que deseja na pizza:"
prompt += "\nDigite 'quit' para finalizar o pedido "

active = True
while active:
    message = input(prompt)
    if message != 'quit':
        ingredientes.append(message)
        print(f"\nO ingrediente '{ingredientes[-1]}', foi adicionado na sua pizza!")
    else:
        print(f"\nSua pizza está pronta!")
        print(f"\tIngredientes: {ingredientes}")
        break