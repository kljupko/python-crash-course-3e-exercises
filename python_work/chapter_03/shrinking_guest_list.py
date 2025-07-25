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

print("\nUnfortunately, the table will not be available in time for the event, so fewer guests will be able to attend.")

removed = guests.pop(0)
print(f"Dear {removed.title()}, unfortunately, we will not be able to host you this time due to logistical issues. Apologies for the inconvenience.")
removed = guests.pop(1)
print(f"Dear {removed.title()}, unfortunately, we will not be able to host you this time due to logistical issues. Apologies for the inconvenience.")
removed = guests.pop(1)
print(f"Dear {removed.title()}, unfortunately, we will not be able to host you this time due to logistical issues. Apologies for the inconvenience.")
removed = guests.pop(2)
print(f"Dear {removed.title()}, unfortunately, we will not be able to host you this time due to logistical issues. Apologies for the inconvenience.")

print(f"\nDear {guests[0].title()}, you are still invited to the dinner party at...")
print(f"Dear {guests[1].title()}, you are still invited to the dinner party at...")

del guests[0]
del guests[0]

print(guests)
