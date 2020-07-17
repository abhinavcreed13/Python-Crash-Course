# --- Lists----

# int, str : building blocks

# list: data structures
# list is a collection of items in a particular order
# inside a list: numbers, strings, numbers and strings

# -- creating list
			 #0      #1      #2         #3 
bicycles = ['trek','cannon','redline','specialized']
			#-4		 #-3	 #-2		#-1
print(bicycles)

print(type(bicycles))

# print(dir(bicycles))

# -- accessing elements

# index starts with 0
# print(type(bicycles[0]))

# print(bicycles[0].title())

# print(bicycles[2])

# negative indexes
# print(bicycles[-4])

# -- using individual items from a list

message = "My first bicycle was a "+bicycles[0].title()+"."

print(message)






