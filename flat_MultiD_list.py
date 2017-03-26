#http://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python

# for len(alist) = 1600
# A took 14.323 ms
# B took 13.437 ms
# C took 1.135 ms
# where:
# A = reduce(lambda x,y: x+y,l)
# B = sum(l, [])
# C = [item for sublist in l for item in sublist]


def flat_list (mylist):

	a=sum(mylist,[])
	return a					#return sum doesn't work
	
	
def flat_list_2(mylist):
	
	b=reduce(lambda x,y:x+y,mylist)
	return (b)


def flat_list_3(mylist):
	
	c=[item for sublist in mylist for item in sublist]	
	return c
	
	


mylist1 = [[1, 1, 1, 1], [2, 3, 4, 5], [10, 20, 30]]		#2D list
print (flat_list(mylist1))
print (flat_list_2(mylist1))
print (flat_list_3(mylist1))

mylist2 = [[[0, 0, 0], [10, 10, 10], [20, 20, 20]],			#3D list
 [[30, 30, 30], [40, 40, 40], [50, 50, 50]],
 [[10, 30, 40], [50, 60, 70], [80, 90, 100]]]

print (flat_list(mylist2))
print (flat_list_2(mylist2))
print (flat_list_3(mylist2))

print (flat_list(flat_list(mylist2)))
print (flat_list_2(flat_list(mylist2)))
print (flat_list_3(flat_list(mylist2)))