# --- Looping through lists ---

magicians = ['alice','david','carolina']

# for loop
# syntax: for <variable> in <list>

# for magician in magicians:
# 	print(magician)

# for every magician in the list of magicians, print the magician name

# -- A closer look at looping

# print(item)

# for item in magicians:
# 	print(item)

# print(item)

# -- doing more work within a for loop

# indendation: 1 tab = 4 spaces

# for magician in magicians:
#     print(magician.title()+", that was a great trick!")
#     print("I can't wait to see your next trick, "+magician.title()+".\n")

# -- doing something after a loop

magicians.append('micheal')
    
for magician in magicians:
    print(magician.title()+", that was a great trick!")
    print("I can't wait to see your next trick, "+magician.title()+".\n")

print("Thank you, everyone. That was a great magic show!")    

# --- Avoiding Indentation Errors ---



