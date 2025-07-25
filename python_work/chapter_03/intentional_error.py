things = ["a thing", "remove me", "another thing"]
print(things)

# the code below will result in an index error because there is no element at position 3.
print(things[3])
# it is fixed by using the index -1 for getting the last element
# or the index 2 can be used to always get the third element, if it exists
