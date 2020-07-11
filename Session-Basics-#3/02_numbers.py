## --- Making Numerical lists

# num_list = [1,2,3,4,5]
# print(num_list)

# print(type(num_list))

# -- range() function
# range(start,end+1): [start...end]
# for value in range(1,6):
# 	print(value)

# -- use range() to make a list of numbers
# boxing + unboxing
# boxing
# numbers = list(range(1,6))
# print(numbers)

# for value in numbers:
# 	print(value)


# boxing
# num = 1
# str_num = str(num)
# message = "Hello I'm "+str(num)
# print(message)

# print(type(num))
# print(type(str_num))

# # unboxing
# print(int(str_num))

# - even numbers from 1 to 10
# even_numbers = list(range(2,11,2))
# print(even_numbers)

# - print squares from 1 to 10
# squares = []
# for value in range(1,11):
# 	squares.append(value**2)

# print(squares)

# -- Simple statistics using numerical lists
#digits = [1,2,3,4,5,6,7,8,9,0]
# digits = list(range(1,10))
# digits.append(0)

# #digits.insert(len(digits),0)
# print(digits)

# print(min(digits))

# print(max(digits))

# print(sum(digits))

# -- list comprehensions

# - squares from 1 to 10
# squares = []
# for value in range(1,11):
# 	squares.append(value**2)

squares = [value**2 for value in range(1,11)]

print(squares)
