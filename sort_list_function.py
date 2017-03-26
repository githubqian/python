import pdb

def sort_list(mylist):

	mysortedlist = []

	for i in range (0, len(mylist)):

		for j in range (1+i, len(mylist)):
			max = mylist[i]
			if mylist[j] > max:
				max = mylist[j]
				mylist[j] = mylist[i]
				mylist[i] = max
				
		mysortedlist.append(mylist[i])
	
	print(mysortedlist)
	return
				
mylist = [1,4,6,8,10,100,56,78,90,43,33,20,11,5,6]
print(mylist)

sort_list(mylist)	




