import pdb

def sort_list(mylist):

	mylist_copy = mylist 
	#The assignment just copies the reference to the list, not the actual list, so both mylist_copy and mylist refer to the same list after the assignment. So when modifying mylist_copy, every time mylist changes as well. There are several ways to copy a list http://stackoverflow.com/questions/2612802/how-to-clone-or-copy-a-list
	
	mylist_copy_2 = list(mylist) #this actaully copy the list, ?

	mysortedlist = []

	for i in range (0, len(mylist_copy_2)):

		for j in range (1+i, len(mylist_copy_2)):
			max = mylist_copy_2[i]
			if mylist_copy_2[j] > max:
				max = mylist_copy_2[j]
				mylist_copy_2[j] = mylist_copy_2[i]
				mylist_copy_2[i] = max
				
		mysortedlist.append(mylist_copy_2[i])
	
	print(mylist)
	print(mylist_copy)
	print(mylist_copy_2)
	print(mysortedlist)
	#return mysortedlist
	return
				
mylist = [1,4,6,8,10,100,56,78,90,43,33,20,11,5,6]
print(mylist)

sort_list(mylist)