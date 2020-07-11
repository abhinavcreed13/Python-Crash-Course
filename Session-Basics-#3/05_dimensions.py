# --- tuples ---

# Immutable: once created then cannot be changed afterward
# List? - No (append)
# Immutable list: tuples

# -- define a tuple?

# syntax (value1, value2,...valueN)
			  #0   #1	
dimensions = (200, 50)
			  #-2 #-1
# print(dimensions[0])
# print(dimensions[1])

# print(dimensions[-1])
# print(dimensions[-2])

# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 250

# print(type(dimensions))

# print(dir(dimensions))

# AttributeError: 'tuple' object has no attribute 'append'
# dimensions.append(20)

# -- looping through tuple values
# for dimension in dimensions:
# 	print(dimension)

# -- writing over a tuple
dimensions = (200,50)
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nNew dimensions:")
for dimension in dimensions:
	print(dimension)



