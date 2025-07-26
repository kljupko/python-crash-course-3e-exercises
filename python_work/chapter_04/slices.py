threes = list(range(3, 31, 3))

for number in threes:
    print(number)

print("\nThe first three items in the list are:")
for number in threes[:3]:
    print(number)

print("\nThree items from the middle of the list are:")
for number in threes[4:7]:
    print(number)

print("\nThe last three items in the list are:")
for number in threes[-3:]:
    print(number)
