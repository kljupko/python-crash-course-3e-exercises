sandwich_orders = ['chicken', 'ham', 'veggie']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"The {sandwich} sandwich is ready for pickup!")
    finished_sandwiches.append(sandwich)

print("\nLet's see, here...")
for sandwich in finished_sandwiches:
    print(f"We're done with the {sandwich} sandwich.")
