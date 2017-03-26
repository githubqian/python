#numrows = len(input)
#numcols = len(input[0])

import pdb
from copy import copy, deepcopy
#reference http://stackoverflow.com/questions/9439480/from-import-vs-import


def sort_multiD_list(mymultidlist):

	mymultidlist_copy = deepcopy(mymultidlist)
	#for multidementional list, list(multidementional_list), copy(multidementional list) all are only references, but actual copy, only deepcopy is a real copy
	
	
	#mysorted_mymultidlist = [[] for i in range(3)]
	#not sure how to define a unfixed length empty multidementional_list, not really used in python
	
	for x in range (0, len(mymultidlist_copy)):			#x is for rownum

		for i in range (0, len(mymultidlist_copy[0])):

			for j in range (1+i, len(mymultidlist_copy[0])):
				max = mymultidlist_copy[x][i]
				if mymultidlist_copy[x][j] > max:
					max = mymultidlist_copy[x][j]
					mymultidlist_copy[x][j] = mymultidlist_copy[x][i]
					mymultidlist_copy[x][i] = max
					
			#mysorted_mymultidlist.append(mymultidlist_copy[x][i])
			
			
	for y in range (0, len(mymultidlist_copy[0])):		#y is for colnum
		for i in range (0, len(mymultidlist_copy)):

			for j in range (1+i, len(mymultidlist_copy)):
				max = mymultidlist_copy[i][y]
				if mymultidlist_copy[j][y] > max:
					max = mymultidlist_copy[j][y]
					mymultidlist_copy[j][y] = mymultidlist_copy[i][y]
					mymultidlist_copy[i][y] = max
					
			#mysorted_mymultidlist.append(mymultidlist_copy[i][y])	
	
		
	
	print(mymultidlist)
	print(mymultidlist_copy)
	#print(mysorted_mymultidlist)
	
	return mymultidlist_copy
				
mylist1 = [1,4,6,8,10,100,56,78,90,43,33,20,11,5,6]
mylist2 = [11,4,6,8,10,100,56,78,90,43,33,20,11,56,66]
mylist3 = [11,44,66,88,10,100,56,78,90,43,33,20,11,5,6]
multidimentionallist = [mylist1,mylist2,mylist3]
print(multidimentionallist)


x = sort_multiD_list(multidimentionallist)
print(x)