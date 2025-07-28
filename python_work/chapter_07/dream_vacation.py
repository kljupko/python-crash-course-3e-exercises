responses = {}

print("Hey everyone! We're polling people to see what the most desireable "
      "vacation spots are.\nWho wants to go first?")

polling_active = True

while polling_active:
    name = input("\nYes, you! Tell us, what is your name? ")
    spot = input(f"And where would your dream vacation be, {name.title()}? ")

    responses[name] = spot
    
    prompt = "\nThat's wonderful, thank you very much."
    prompt += "\nAnyone else? (yes / no) "
    repeat = input(prompt)
    if repeat.lower() == "no":
        polling_active = False
        print("Thank you everyone!")


print("\n\nHere are the results of our poll:")
for name, spot in responses.items():
    print(f"{name.title()}'s dream vacation would be {spot.title()}.")

print("\n\nThat's all. Until next time!")
