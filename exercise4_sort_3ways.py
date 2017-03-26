#https://wiki.python.org/moin/HowTo/Sorting

def sort(mylist):
	for i in range(0, len(mylist)):
		for j in range (i+1, len(mylist)):
			
			if mylist[j] < mylist[i]:
				tmp=mylist[i]
				mylist[i]=mylist[j]
				mylist[j]=tmp
				
	return mylist
	

list1=['a',1,2,3,4,'d','c','d','b']
list2=[1,3,6,7,9,100,40]
list3=['d','b','c','d','a','x','w','y']

print sort(list1)
print sort(list2)
print sort(list3)
				
				
def sort_2(mylist):
	return sorted(mylist)	#return a new list
	
	
print sort_2(list1)
print sort_2(list2)
print sort_2(list3)	
	

def sort_3(mylist):
	#return mylist.sort()	This function returns None
	mylist.sort()	#modify list in-place
	return mylist
	

print sort_3(list1)
print sort_3(list2)
print sort_3(list3)	