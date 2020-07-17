# -- Organizing lists --

# - Sorting a list permanently

# cars = ['bmw','audi','toyota','ferrari']

# print(cars)

# cars.sort(reverse=False)

# print(cars)

# # in reverse

# cars.sort(reverse=True)

# print(cars)

# - Sorting a list temporarily: sorted

# new_cars = sorted(cars)
# new_cars = sorted(cars, reverse=True)

# print(new_cars)

# print(cars)


# - Print a list in reverse

# cars = ['bmw','audi','toyota','ferrari']

# # print(cars)

# # cars.reverse()

# print(cars)

# # - length of a list: len

# print(len(cars))

# # - getting that last element

# # length_of_cars = len(cars)
# # last_element_index = length_of_cars - 1
# # print(cars[last_element_index])

# print(cars[len(cars)-1])

# print(cars)

# - Index errors

cars = ['bmw','audi','toyota','ferrari']

# IndexError: list index out of range
#print(cars[5])

# IndexError: list index out of range
print(cars[-5])

