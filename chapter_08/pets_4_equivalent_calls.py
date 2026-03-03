def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Um cachorro chamado Floquinho
describe_pet('floquinho')
describe_pet(pet_name='floquinho')

# Um hamster chamado Harry
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')