# ------ Basics #2: Lists -------

# Lists allow you to store sets of information in one place, 
# whether you have just a few items or millions of items.

# list is a collection of items in a particular order

# collection of numbers, letters, alphabets, strings
			#0		#1		#2			#3
# bicycles = ['trek','connon','redline','specialized']
# 			#-4		#-3		#-2			#-1
# print(bicycles)

# --- accessing elements
# print(bicycles[0])
# print(bicycles[1])

# print(bicycles[0].title())

# print(type(bicycles[0]))

# index position starts at 1

# print(bicycles[-4])

# --- using individual items
# message = "My first bicycle was a "+bicycles[0].title()+"."
# print(message)

# 3 exercises

# --- List operations

# modifying elements
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# motorcycles[0] = 'ducati'
# print(motorcycles)

# adding elements: append

# get all functions
#print(type(motorcycles))
#print(dir(motorcycles))

# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('ducati')
# print(motorcycles)

# print(dir(motorcycles))

# adding elements: insert
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# motorcycles.insert(0,'ducati')
# print(motorcycles)

# removing elements: del
# del motorcycles[0]
# print(motorcycles)

# del motorcycles[1]
# print(motorcycles)

# print(dir(motorcycles))

# removing elements: pop
# popped_motorcycle = motorcycles.pop()
# print(popped_motorcycle)
# print(motorcycles)

# last_owned = motorcycles.pop()
# print("The last motorcycle I owned was a "+last_owned.title()+".")

# # pop from any position?
# first_owned = motorcycles.pop(0)
# print("The first motocycle I owned was a "+first_owned.title()+".")

# print(motorcycles)

# removing elements by value: remove
# motorcycles = ['honda','yamaha','suzuki']
# print(motorcycles)

# #print(dir(motorcycles))

# # motorcycles.remove('honda')
# # print(motorcycles)

# too_expensive = "suzuki"
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print("\nA "+too_expensive.title()+" is too expensive for me.")

# situation?
motorcycles = ['honda','yamaha','suzuki','yamaha']
print(motorcycles)

motorcycles.remove('yamaha')
print(motorcycles)
