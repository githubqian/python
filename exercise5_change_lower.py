def change_lower(mylist):
	lower_list=[]
	for item in mylist:
		lower_list.append(item.lower())
		
	return lower_list
	
mylist=['a','b','A','B','C','D']
mylist2=['I','Think','SO','tOo']
print change_lower(mylist)
print change_lower(mylist2)