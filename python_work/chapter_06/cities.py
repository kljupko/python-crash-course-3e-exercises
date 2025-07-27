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

for city, info in cities.items():
    print(f"\nCity: {city.title()}")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']}")
    print(f"\tFact: {info['fact']}")

