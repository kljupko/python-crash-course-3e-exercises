colors = ["red", "green", "blue"]
bike = "honda"

print("Is bike == 'honda'? I predict True.")
print(bike == 'honda')

print("\nIs bike == 'ducati'? I predict False.")
print(bike == 'ducati')

print("\nIs bike.upper() == 'HONDA'? I predict True.")
print(bike.upper() == 'HONDA')

print("\nIs bike.title() != 'Honda'? I predict False.")
print(bike.title() != 'Honda')

print("\nIs 'red' in colors? I predict True.")
print('red' in colors)

print("\nIs 'white' in colors? I predict False.")
print('white' in colors)

print("\nIs 'grey' not in colors? I predict True.")
print('grey' not in colors)

print("\nIs 'blue' not in colors? I predict False.")
print('blue' not in colors)

print("\nIs bike == 'honda' or 'brown' in colors? I predict True.")
print(bike == 'honda' or 'brown' in colors)

print("\nIs 'brown' in colors and 'green' in colors? I predict False.")
print('brown' in colors and 'green' in colors)
