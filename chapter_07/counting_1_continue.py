current_number = 0

while current_number < 10:
    current_number += 1
    
    if current_number % 2 == 0:
        continue # se for par, pula o restante do código e volta para o início do loop
    
    print(current_number)