rivers = {
        "nile": "egypt",
        "amazon": "brazil",
        "mississippi": "mississippi",
        }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nThe rivers:")
for river in rivers:
    print(river.title())

print("\nThe countries:")
for country in rivers.values():
    print(country.title())
