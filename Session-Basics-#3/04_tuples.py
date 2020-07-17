## -- Tuples --

# Tuples: immutable lists

# - Define a tuple?
			  #0  #1
# dimensions = (100,50)
			  #-2 #-1	
# print(type(dimensions))

# print(dir(dimensions))

# print(dimensions[-1])
# print(dimensions[-2])

# How do we prove immutability?

# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 150

# - Looping through a tuple

# dimensions = (200,50,150,200,250)

# # for dimension in dimensions:
# # 	print(dimension)

# # what about slicing?

# for dimension in dimensions[:3]:
# 	print(dimension)

# - Writing over a tuple

# dimensions = (200,50)
# print("Original dimensions:")
# for dimension in dimensions:
# 	print(dimension)

# dimensions = (400,100)
# print("\nModified dimensions:")
# for dimension in dimensions:
# 	print(dimension)


