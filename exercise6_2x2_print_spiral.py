def print_spiral (alist):

	for i in range (0,1):
		for j in range (0,2):

			print alist[i][j]
			
	for i in range (1,2):
		for j in range (1,-1,-1):
		
			print alist[i][j]
			
	return
			
			
			
mylist=[[1,2],[4,5]]
print_spiral(mylist)			