def city_country(city_name, country_name):
    """Display city and in which country it is"""
    place = f"\n{city_name.title()}, {country_name.title()}"
    return place
favorite_place = city_country('vienna','austria')
going_to = city_country('zurich','switzerland')
print(favorite_place)
print(going_to)