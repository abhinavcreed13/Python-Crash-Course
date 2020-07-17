# -- Looping through list --

magicians = ['alice','dave','carolina']

# for magician in magicians:
# 	print(magician)

# for magician in magicians: 
	
# 	print(magician.title() + ", that was a great trick!")
# 	print("I can't wait to see your next trick, "+ magician.upper()+".\n")
# 	print("Thank you everyone. That was a great magic show!")


# -- Avoiding Indentation Errors

# - Forgetting to indent

magicians = ['alice','dave','carolina']

# IndentationError: expected an indented block
# for magician in magicians:
# print(magician)
# print("Here")

# - Forgetting to indent additional lines

# for magician in magicians:
# 	print(magician)
	
# print("Here")

# - Indenting unnecessarily

# # 1 tab or 4 spaces
# # IndentationError: unindent does not match any outer indentation level
# for magician in magicians:
# 	print(magician)
# 	print(magician.title())

# # IndentationError: unindent does not match any outer indentation level
# for magician in magicians:
# 	print(magician)
# 	print(magician.title())

# - Indenting unnecessarily after a loop

# for magician in magicians: 
	
# 	print(magician.title() + ", that was a great trick!")

# 	print("I can't wait to see your next trick, "+ magician.upper()+".\n")

# 	print("Thank you everyone. That was a great magic show!")

# - Forgetting the colon

# SyntaxError: invalid syntax
for magician in magicians:
	
	print(magician.title() + ", that was a great trick!")

	print("I can't wait to see your next trick, "+ magician.upper()+".\n")

	print("Thank you everyone. That was a great magic show!")



