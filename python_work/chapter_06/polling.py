favorite_numbers = {
        "john": 1,
        "jane": 2,
        "lucy": 3,
        "steve": 4,
        "vanessa": 5,
        }

print(f"John's favorite number is {favorite_numbers['john']}")
print(f"Jane's favorite number is {favorite_numbers['jane']}")
print(f"Lucy's favorite number is {favorite_numbers['lucy']}")
print(f"Steve's favorite number is {favorite_numbers['steve']}")
print(f"Vanessa's favorite number is {favorite_numbers['vanessa']}")


print("\nRegarding the poll...")
people = ["tom", "stacy", "lucy", "steve", "rob"]

for person in people:
    if person in favorite_numbers:
        print(f"{person.title()}, thank you for taking the poll.")
    else:
        print(f"{person.title()}, please take the poll.")
