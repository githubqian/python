 
 
def delete_element(mylist):
	i = len(mylist)
	del mylist[i-2]
	return mylist
	
	
	
mylist = [1,3,5,7,9]
mylist2 = ['one','two','three','four','five']
print (delete_element(mylist))
print (delete_element(mylist2))