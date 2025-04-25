#1
car = 'bmw'
print(car == 'bmw') #True

print(car != 'bmw') #False

#2
name = 'Leonir'
print(name.lower() == 'leonir') #True

print(name.lower() == 'Leonir') #False

#3
age = 22
print(age == 22) #True

print(age != 22) #False

print(age > 18) #True

print(age < 18) #False

print(age >= 19) #True

print(age <= 19) #False

#4
number = 33
print(number == 33 and number != 31) #True

print(number == 22 or number < 12) #False

#5
names = ['leonir', 'lais', 'lorraine']
print('leonir' in names) #True

print('arthur' in names) #False

#6
motocycles = ['honda', 'yamaha', 'bmw']
print('ducati' not in motocycles) #True

print('honda' not in motocycles) #False