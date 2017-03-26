def sort(mylist):
    less = []
    equal = []
    greater = []

    if len(mylist) > 1:
        pivot = mylist[0]
        for x in mylist:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
# Note that you want equal ^^^^^ not pivot
    else:  # You need to hande the part at the end of the recursion - when you only have one element in your array, just return the list.
		return mylist
		

mylist = [12,4,5,6,7,3,1,15, 26,37,54,8,9]		
x = sort(mylist)
print x
		
		