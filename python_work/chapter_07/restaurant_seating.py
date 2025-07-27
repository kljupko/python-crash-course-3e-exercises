num_people = input("How many people are in your dinner group? ")
num_people = int(num_people)

if num_people > 8:
    print("You will need to wait until a table is made available.")
else:
    print("Your table is ready. Right this way, please.")
