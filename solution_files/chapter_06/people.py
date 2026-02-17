people = {
    'leo': {
        'first_name': 'leonir',
        'last_name': 'kochenborger',
        'age': 29,
        'city': 'congonhas',
    },

    'loh': {
        'first_name': 'lorraine',
        'last_name': 'ribeiro',
        'age': 30,
        'city': 'congonhas',
    },

    'lis': {
        'first_name': 'lais',
        'last_name': 'oliveira',
        'age': 32,
        'city': 'congonhas',
    },

}

for username, user_info in people.items():
    print(f"\nUsername: {username.title()}")
    full_name = f"{user_info['first_name']} {user_info['last_name']}"
    age = user_info['age']
    city = user_info['city']

    print(f"\tFullname: {full_name.title()}")
    print(f"\tAge: {age}")
    print(f"\tCity: {city.title()}")

#full_name = f"{people['first_name']} {people['last_name']}".title()
#city = people['city'].title()

#print(f"{full_name} tem {people['age']} anos, mora em {city}.")