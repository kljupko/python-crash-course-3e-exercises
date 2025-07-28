def city_country(city, country):
    formatted = f"{city.title()}, {country.title()}"
    return formatted

output_1 = city_country("santiago", "chile")
output_2 = city_country("reykjavik", "iceland")
output_3 = city_country("buenos aires", "argentina")

print(output_1)
print(output_2)
print(output_3)
