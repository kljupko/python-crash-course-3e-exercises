favorite_places = {
    "alice": ["paris", "kyoto", "new york"],
    "bob": ["grand canyon", "rome"],
    "carol": ["santorini"]
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite place(s):")
    for place in places:
        print(f"\t{place.title()}")

