def city_country(city_name, country_name):
    """Exibe menssagem simples com nome de uma cidade e país"""
    full_location = f"{city_name}, {country_name}"
    return full_location.title()

result = city_country('santiago', 'chile')
print(result)

result = city_country('rio de janeiro', 'brasil')
print(result)

result = city_country('paris', 'frança')
print(result)