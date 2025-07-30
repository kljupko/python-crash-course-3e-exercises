from city_functions import city_country

def test_city_country():
    """Test if city and country are formatted properly."""
    formatted = city_country("santiago", "chile")
    assert formatted == "Santiago, Chile"

def test_city_country_population():
    """Test if city, country, and population are formatted properly."""
    formatted = city_country("santiago", "chile", 5_000_000)
    assert formatted == "Santiago, Chile - population 5000000"
