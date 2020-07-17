## -- Lists operations --

# motorcyles = ['honda','yamaha','suzuki']

# # <class 'list'>
# print(motorcyles)

# print(dir(motorcyles))

# - modify list
# Mutable: list items can be modified

# motorcyles[0] = 'ducati'

# print(motorcyles)

# IndexError: list assignment index out of range
# motorcyles[3] = 'ducati2'

# - Adding elements in a list

# TypeError: append() takes exactly one argument 
# motorcyles.append('ducati')

# print(motorcyles)

# - adding multiple elements
# blank list
# motorcyles = []

# motorcyles.append('honda')
# motorcyles.append('yamaha')
# motorcyles.append('suzuki')

# print(motorcyles)

# - adding elements via insert

# motorcyles = ['honda','yamaha','suzuki']

# #print(dir(motorcyles))
# print(motorcyles)

# #motorcyles.insert(1,'ducati')
# motorcyles.insert(2,'ducati')

# print(motorcyles)

# - Removing elements

# motorcyles = ['honda','yamaha','suzuki']

# print(motorcyles)

# - del keyword

# del motorcyles[2]

# print(motorcyles)

# - pop function

# popped_motorcycle = motorcyles.pop(0)

# print(popped_motorcycle)
# print(motorcyles)

# first_owned = motorcyles.pop(0)

# print("The first motorcyle I owned was a "+first_owned.title()+".")

# - remove function

# motorcyles.remove('honda')

# print(motorcyles)

motorcyles = ['honda','yamaha','suzuki','honda','yamaha']

print(motorcyles)

motorcyles.remove('honda')

print(motorcyles)

motorcyles.remove('honda')

print(motorcyles)



