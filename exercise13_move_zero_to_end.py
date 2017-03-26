def move_zeros_to_end(a_list):

    cnt = 0
    while 0 in a_list:
	#for 0 doesn't work
        a_list.remove(0)
		#a_list.pop(0) makes all value 0
        cnt += 1

    return a_list + [0]*cnt
	

list=[0,1,5,0,0,10,8,9,0,0,11,12,0]
print move_zeros_to_end(list)