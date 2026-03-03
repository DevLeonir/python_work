def describe_pet(pet_name, animal_type='dog'):
    """Exibe as informações sobre um animal de estimação"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

#describe_pet(pet_name='floquinho')
#describe_pet(pet_name='harry', animal_type='hamster')
describe_pet('floquinho')
