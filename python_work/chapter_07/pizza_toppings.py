toppings = []

prompt = "Enter the topping you would like."
prompt += "\nEnter 'done' when you're finished. "

while True:
    topping = input(prompt)
    topping = topping.lower()

    if topping == 'done':
        break

    if topping not in toppings:
        toppings.append(topping)
        print(f"Alright, added {topping}. Anything else?\n")
    else:
        print("Already there, boss.\n")

if toppings == []:
    print("\nChanged your mind? No problem.")
else:
    print("\nAlright, making a pizza with:")
    for topping in toppings:
        print(f" - {topping}")
