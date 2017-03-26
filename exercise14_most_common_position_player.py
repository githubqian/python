"""There is a file containing a listing of Basketball Players, position and their strongest statistic they record during games.

Positions = [PG, SG, SF, PF, C]
Stats = [PTS, AST, DRB, ORB, STL, BLK]

For example, the file players.txt contains these four lines:
PG - James Tyler - STL
PF - Harold Ennis - DRB
C - Hal Monroe - BLK
SF - Gerry Valdez - PTS
PF - Ferris Samuel - STL

Write a script or program that scans the file and returns the most common position amongst the players listed.

For example, if you run your program
./most_common_positions players.txt
it would print the position, most common:
PF

In the case that there are two positions which have an equal amount of players listed, return both positions.

------------"""


def find_most_common_position():
	position_list = []
	position_and_count_dict = {}
	pg_count = 0
	pf_count = 0
	c_count = 0
	sf_count = 0
	pf_count = 0
	
	with open("players.txt", "r") as fh:
		for line in fh:
			position_list.append(line[0:0+2])
		
	for position in position_list:
		position_count = position_list.count(position)
		position_and_count_dict.update({position:position_count})
	#key, value = max(position_and_count_dict.iteritems(), key=lambda x:x[1])	#only return one max
	tmp_list = [key for key,val in position_and_count_dict.iteritems() if val == max(position_and_count_dict.values())]
	#The above would cover the case that there are more that one positions which have an equal/most number of players listed, return all these positions.
	return str(tmp_list).strip('[]').replace("'",'')

		
print find_most_common_position()
