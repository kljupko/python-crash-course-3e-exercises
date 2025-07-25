guests = ["mr. mike portnoy", "mr. danny carey", "mr. lars ulrich"]

print(f"Dear {guests[0].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[1].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[2].title()}, I would like to extend an invitation to a dinner party at...")

missing = guests[1]

print(f"It appears that {missing.title()} is unable to attend.")

guests[1] = "mr. mike mangini"

print(f"Dear {guests[0].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[1].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[2].title()}, I would like to extend an invitation to a dinner party at...")
