def print_1st_unique(alist):
	for i in range (0,len(alist)):
		if alist.count(alist[i])==1:
			print i
			print alist[i]
			return	#this 'return' will stop the loop/function after the first unique charactor is found, all the unique will be printed w/o this 'retun'
		#return #this 'return' will not disply aything
	#return #w/ or w/o this 'return', all the unique will be printed
	
mylist='it is a beautiful day!'
	
print_1st_unique(mylist)
