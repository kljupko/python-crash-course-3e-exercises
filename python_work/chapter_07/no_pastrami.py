sandwich_orders = [
        'chicken', 'pastrami', 'ham',
        'veggie', 'pastrami', 'pastrami'
        ]
finished_sandwiches = []

print("ATTENTION EVERYONE! PASTRAMI'S OUT!\n")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"The {sandwich} sandwich is ready for pickup!")
    finished_sandwiches.append(sandwich)

print("\nLet's see, here...")
for sandwich in finished_sandwiches:
    print(f"We're done with the {sandwich} sandwich.")
