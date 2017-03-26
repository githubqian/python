import pdb

def sort_list(mylist):
#this function actally change the mylist to mysortedlist, the original mylist doesn't eist anymore

	mysortedlist = []

	for i in range (0, len(mylist)):

		for j in range (1+i, len(mylist)):
			max = mylist[i]
			if mylist[j] > max:
				max = mylist[j]
				mylist[j] = mylist[i]
				mylist[i] = max
				
		mysortedlist.append(mylist[i])
	
	#print(mylist)
	#print(mysortedlist)
	#mylist and mysortedlist are the same
	
	return mysortedlist
				
mylist = [1,4,6,8,10,100,56,78,90,43,33,20,11,5,6]
print(mylist)

my_sorted_mylist = list(sort_list(mylist))	#make a copy
my_sorted_mylist_2 = sort_list(mylist)		#asign list referent 
print(my_sorted_mylist)
print(my_sorted_mylist_2)