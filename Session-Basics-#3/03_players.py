# --- Working with Part of a list

# -- slicing a list
			#0			#1		#2			#3		#4
players = ['charles','martina','micheal','florence','eli']
			#-5			#-4		#-3			#-2		#-1
# players[start:end+1] = [start..end]
# print(players[1:4])

# players[:end+1] = [beginning of list...end]
# print(players[:4])

# players[start:] = [start....end of list]
# print(players[2:])

# tricky
# players[-start:] = [-start...end of list] 
# last three players
# print(players[-3:])

# players[:-end+1] = [beginning of list...end]
# top 2 players
# print(players[:-3])

# -- loop through a slice

# print("Here are the first three players on my team:")
# for player in players[:3]:
# 	print(player)

# print(dir(players))




