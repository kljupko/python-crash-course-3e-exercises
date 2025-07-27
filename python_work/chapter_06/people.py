person_1 = {
        "name": "john",
        "surname": "doe",
        "age": 30,
        "city": "new york",
        }

person_2 = {
        "name": "jane",
        "surname": "doe",
        "age": 46,
        "city": "phoenix",
        }

person_3 = {
        "name": "martin",
        "surname": "smith",
        "age": 79,
        "city": "salt lake city",
        }


people = [person_1, person_2, person_3]

for person in people:
    print(f"{person['name'].title()} {person['surname'].title()} is a "
          f"{person['age']}-year-old from {person['city'].title()}.")

