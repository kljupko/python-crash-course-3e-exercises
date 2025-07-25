guests = ["mr. mike portnoy", "mr. danny carey", "mr. lars ulrich"]

print(f"Dear {guests[0].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[1].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[2].title()}, I would like to extend an invitation to a dinner party at...")

missing = guests[1]

print(f"It appears that {missing.title()} is unable to attend.")

guests[1] = "mr. mike mangini"

print(f"\nDear {guests[0].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[1].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[2].title()}, I would like to extend an invitation to a dinner party at...")

print("\nDear guests, a larger table has been made available, and more guests will be invited.")

guests.insert(0, "mr. tony levin")
guests.insert(2, "mr. justin chancellor")
guests.append("mr. jordan rudess")

print(f"\nDear {guests[0].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[1].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[2].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[3].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[4].title()}, I would like to extend an invitation to a dinner party at...")
print(f"Dear {guests[5].title()}, I would like to extend an invitation to a dinner party at...")

