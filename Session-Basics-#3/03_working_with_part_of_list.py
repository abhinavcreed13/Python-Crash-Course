## -- Working with a part of list
			#0        #1        #2        #3		#4
# players = ['charles','martina','micheal','florence','eli']
			#-5      #-4       #-3        #-2       #-1
# print(players)

# - slicing

# print(players[0:3])

# print(type(players[1:4]))

# nice tricks

# top 3 players
# trick 1
# [:end] -> [start of the list...end - 1]
# print(players[:4])

# trick 2
# [start:] -> [start...end of the list]
# print(players[2:])

# trick 3
# print(players[:-2])

# - looping through a slice

# players = ['charles','martina','micheal','florence','eli']

# print("Here are the first three players on my team:")

# for player in players[:3]:
# 	print(player.title())

# - copying a list

my_foods = ['pizza','falafel','carrot cake']

# copy via reference
# friend_foods = my_foods

# [:] -> [start of list...end of list]
# copy via value
friend_foods = my_foods[:]

print("My favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)

my_foods.append('cannoli')

friend_foods.append('ice cream')

print("\nMy favourite foods are:")
print(my_foods)

print("\nMy friend's favourite foods are:")
print(friend_foods)




