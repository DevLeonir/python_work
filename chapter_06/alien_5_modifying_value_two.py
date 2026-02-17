alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Desloca o alienígena para direita
# Estipula a distância que o alienígena deve percorrer conforme sua velocidade
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # Com isso, o alienígena fica veloz
    x_increment = 3
# A posição nova é a posição antiga mais o incremento
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")