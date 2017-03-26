def find_most_common_position():
	position_list = []
	position_and_count_dict = {}
	
	with open("players.txt", "r") as fh:
		for line in fh:
			position_list.append(line[0:0+2])
		
	for position in position_list:
		position_count = position_list.count(position)
		position_and_count_dict.update({position:position_count})

	most_common_position_key = [key for key,val in position_and_count_dict.iteritems() if val == max(position_and_count_dict.values())]
	# The above would cover the case that there are more that one positions which have an equal/most number of players listed, return all these positions.
	return str(most_common_position_key).strip('[]').replace("'",'')
	
	
# The above is sent to Ron T. It uses file operation, substring, list, dictionary, for loop, list comprehension and iterator, string conversion and manipulation. Proud of myself!

print find_most_common_position()