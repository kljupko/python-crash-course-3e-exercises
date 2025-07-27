prompt = "Welcome! How old are you?"
prompt += "\n(Type 'done' when you're finished.) "

while True:
    age_input = input(prompt)

    if age_input.lower() == 'done':
        print("\nThanks for visiting. Enjoy the show!")
        break

    age = int(age_input)

    if age < 3:
        print("You're good to go — it's free for the little ones!\n")
    elif age <= 12:
        print("That'll be $10 for the ticket.\n")
    else:
        print("Standard ticket — that'll be $15.\n")

