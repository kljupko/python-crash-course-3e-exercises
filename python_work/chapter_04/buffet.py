offer = ("hamburger", "french fries", "ham sandwitch", "salad", "cupcake")

for item in offer:
    print(item)

# if uncommented, the code below results in a type error
#offer[0] = "cheeseburger"

offer = ("cheeseburger", "french fries", "ham sandwitch", "salad", "donut")
print("\nNew offer:")
for item in offer:
    print(item)
