"""Contains a function to print a city in a country."""


def city_country(city, country, population=""):
    """Returns a formatted string of the city and country."""
    if population:
        formatted = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted = f"{city.title()}, {country.title()}"
    return formatted
