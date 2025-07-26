my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for item in my_foods:
    print(item)

print("\nMy friend's favorite foods are:")
for item in friend_foods:
    print(item)
