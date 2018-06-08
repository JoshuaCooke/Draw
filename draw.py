#draw
import numpy as np

teams = str(input("enter list of players/teams seperated by a comma (,)"))
list_team = teams.split(",")
# generated a list of the players/teams 

if len(list_team)%2 != 0:
	list_team.append("bye")
a = len(list_team)
#ensured that the number of teams is even, if it was odd added pseudo player "bye" to allow matchups
# if player is matched with bye they get a bye (ie automatically progress to the next round)

np.random.shuffle(list_team)
list_team = np.array(list_team)
list_team = list_team.reshape(int(a/2),2)

print("fixture list")
for i in list_team:
	print(i[0], "vs", i[1])
#prints the fixture list (the list of pairs)