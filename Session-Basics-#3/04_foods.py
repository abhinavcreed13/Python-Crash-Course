# -- copying a list
my_foods = ['pizza','falafel','carrot cake']

# copy via reference
friend_foods = my_foods

# # copy via value
# friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

# 2 exercises
