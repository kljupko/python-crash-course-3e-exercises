favorite_numbers = {
    "john": [1, 7],
    "jane": [2, 4, 8],
    "lucy": [3],
    "steve": [4, 6],
    "vanessa": [5, 10, 15],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number(s):")
    for number in numbers:
        print(f"\t{number}")

