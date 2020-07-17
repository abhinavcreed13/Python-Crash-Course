## -- conditional tests --

# simple if example
# !!indentation!!

# - checking for equality (==)

# cars = ['audi','bmw','ferrari','toyota']

# if car is bmw, print title otherwise print uppercase
# for car in cars:
# 	if car == 'bmw':
# 		print(car.title())
# 	else:
# 		print(car.upper())

# - Ignoring case when checking for equality

# cars = ['audi','BMW','ferrari','toyota']

# if car is bmw, print title otherwise print uppercase
# for car in cars:
# 	if car.lower() == 'bmw':
# 		print(car.title())
# 	else:
# 		print(car.upper())

# - Checking for inequality (!=)

# requested_topping = 'extra cheese'

# if requested_topping != 'extra cheese':
# 	print("Hold the extra cheese!")

# - Numerical comparisons

# age = 18

# bool_val = True
# bool_val = False
# print(type(bool_val))

# bool_val = 'true' #<class 'str'>
# print(type(bool_val))

# print(age==18)

# print(age > 18)

# print(age < 18)

# print(age >= 18)

# print(age <= 18)

# print(age != 18)

# toppings1 = 'Eushrooms'

# toppings2 = 'extra cheese'

# toppings = ['mushrooms','extra cheese']

# toppings.sort()
# print(toppings)

# # print(toppings1==toppings2)

# print(toppings1 > toppings2)

# # unicodes /ASCII codes
# print(ord('E'))
# print(ord('e'))

# print(toppings1 < toppings2)

# print(toppings1 >= toppings2)

# print(toppings1 <= toppings2)

# print(toppings1 != toppings2)


# - Checking multiple conditions

# age_0 = 22

# age_1 = 18

# if first age is greater than 21 and second age is also greater than 21
# then do something

# AND works = logic gate AND
# A   B   Result
# F   F    F
# F   T    F
# T   F    F
# T   T    T

# both conditions are true then only entire condition is true

# and - operator
# if ((age_0 >= 21) and (age_1 >= 21)):
# 	print("It passed")
# else:
# 	print("Not passed")

# or - operator

# OR works = logic gate OR
# A   B   Result
# F   F    F
# F   T    T
# T   F    T
# T   T    T

# if any of the condition is true then entire condition is true

# if ((age_0 >= 21) or (age_1 >= 21)):
# 	print("It passed")
# else:
# 	print("Not passed")

# mixing and/or

# age_0 = 22

# age_1 = 18

# age_2 = 23

# if (((age_0 >= 21) and (age_1 >= 21)) or (age_2 >= 24)):
# 	print("It passed")
# else:
# 	print("Not passed")

# - Checking value is in a list

# requested_toppings = ['mushrooms','onions','tomatoes']

# if 'mushrooms' in requested_toppings:
# 	print("Mushrooms requested")
# else:
# 	print("mushrooms not requested")

# - Checking value is not in a list

# not in - operators

# requested_toppings = ['mushrooms','onions','tomatoes']

# if 'mushrooms' not in requested_toppings:
# 	print("Mushrooms requested")
# else:
# 	print("mushrooms not requested")

# banned_users = ['andrew','andrian','david']

# user = 'andrian'

# if user not in banned_users:
# 	print(user.title()+", you can post a response if you wish.")

# - Boolean expressions

# !! boxing/unboxing !! - !! Type casting !!
# game_active = bool('tRUe')

# game_active = int(True)

# print(type(game_active))

# print(game_active)

# print(list(range(1,10)))






