print("Enter two numbers to add them together.\n")


while True:
    n1 = input("First number: ")
    n2 = input("Second number: ")

    try:
        x = int(n1) + int(n2)
    except ValueError:
        print("Please use numbers.")
    else:
        print(f"{n1} + {n2} = {x}")
        break
