pet_1 = {
    "animal": "dog",
    "owner": "alice"
}

pet_2 = {
    "animal": "cat",
    "owner": "bob"
}

pet_3 = {
    "animal": "parrot",
    "owner": "carol"
}

pet_4 = {
    "animal": "hamster",
    "owner": "dave"
}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print(f"The {pet['animal']} is owned by {pet['owner'].title()}.")

