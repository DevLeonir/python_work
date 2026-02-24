prompt = "\nQual é a sua idade?"
resposta = input(prompt)

active = True
while active:
    if resposta == 'quit':
        print("\nAtendimento fechado!")
        break
    
    idade = int(resposta)

    if idade < 3:
        print("\nO ingresso é gratuito!")
        break
    elif 3 <= idade <= 12:
        print("\nO ingresso custa U$10!")
        break
    else:
        print("\nO ingresso custa U$15!")
        break