pizzas = ["mexicana", "cappriciosa", "quatro fromaggi"]
for pizza in pizzas:
    print(pizza)

for pizza in pizzas:
    print(f"Boy, I really love pizza {pizza}!")

print("Mamma mia, I love-a the pizza pie!")


friend_pizzas = pizzas[:]

pizzas.append("tuna")
friend_pizzas.append("pepperoni")

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
