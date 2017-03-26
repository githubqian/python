

def reverse_list(mylist):
	reverse_mylist = []
	i = len(mylist)-1
	for x in range (i, -1, -1):
		reverse_mylist.append(mylist[x])
	print(reverse_mylist)
		
	return
	
#in-place conversion	
def reverse_list_2(mylist):
	#reverse_mylist = []
	tmp = ''
	for x in range (0, int(len(mylist)/2)):			#there seems no different with int() or without int()
		tmp = mylist[x]
		mylist[x] = mylist[len(mylist)-1-x]
		mylist[len(mylist)-1-x] = tmp
		
	return mylist
	
mylist_test_string = ['a','b','c','d','e','f','g']
reverse_list(mylist_test_string)
print (reverse_list(mylist_test_string))			#why there is "None" printed at newline after the reversed string?


mylist_test_number = [1,2,3,4,5,6,7,8,9,10]
reverse_list(mylist_test_number)
print (reverse_list_2(mylist_test_number))