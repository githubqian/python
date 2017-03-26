def find_most_common_position_2():
	with open("players.txt", "r") as fh:
		for line in fh:
			print line[0]+line[1]

			
find_most_common_position_2()