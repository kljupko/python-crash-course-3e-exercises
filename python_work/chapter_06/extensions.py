cities = {
    "paris": {
        "country": "france",
        "population": "2.1 million",
        "fact": "Paris is known as the City of Light."
    },
    "tokyo": {
        "country": "japan",
        "population": "14 million",
        "fact": "Tokyo is the most populous metropolitan area in the world."
    },
    "sydney": {
        "country": "australia",
        "population": "5.3 million",
        "fact": "Sydney is famous for its Opera house and Harbour bridge."
    }
}


cities["paris"]["famous_food"] = "croissant"
cities["paris"]["language"] = "french"

cities["tokyo"]["famous_food"] = "sushi"
cities["tokyo"]["language"] = "japanese"

cities["sydney"]["famous_food"] = "meat pie"
cities["sydney"]["language"] = "english"

for city, info in cities.items():
    print(f"\n{city.title()}:")
    print(f"  - Country: {info['country'].title()}")
    print(f"  - Population: {info['population']}")
    print(f"  - Language: {info['language'].title()}")
    print(f"  - Famous Food: {info['famous_food'].title()}")
    print(f"  - Fact: {info['fact']}")

