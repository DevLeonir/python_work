my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for pizza in my_foods:
    print(pizza.title())

print("\nMy friend's favorite foods are:")
for pizza in friend_foods:
    print(pizza.title())