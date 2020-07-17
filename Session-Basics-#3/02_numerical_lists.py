## -- Numerical lists --

# range(): generate a list of numbers

# range(min,max+1)
# for value in range(1,6):
# 	print(value)

# - make a list of numbers

# boxing/unboxing
# age = 10

# # boxing int to str
# str_age = str(age)

# # unboxing
# age = int(str_age)

# print("You age is "+str(age))

# list of 1 to 5
# <class 'range'>
# print(type(range(1,6)))

# # <class 'list'>
# numbers = list(range(1,11))
# print(numbers)

# - print even numbers from 1 to 10

# print(list(range(2,11,2)))

# - print squares from 1 to 10

# squares = []
# for value in range(1,11):
# 	#square = value**2
# 	squares.append(value**2)

# print(squares)

# - statistics: min, max, sum

# digits = [1,2,3,4,5,6,7,8,9,10]

# print(min(digits))

# print(max(digits))

# print(sum(digits))

# - List comprehensions

squares = []
for value in range(1,11):
	#square = value**2
	squares.append(value**2)

# print(squares)

squares = [ value**2 for value in range(1,11) ]
print(squares)





