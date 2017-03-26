

# def uniq(alist):
  # unique_list = []
  # dup_list =[]
  # for x in alist:
    # if x not in unique_list:
		# unique_list.append(x)
	# else:
		# dup_list.append(x)
  # print unique_list
  # print dup_list
  
  # return
  
  
def uniq_2(alist):
	a=set(alist)
	aa=str(a)
	aaa=aa.replace ('set([','')
	aaaa=aaa.replace('])','')
	print a
	#print aa
	#print aaa
	print aaaa
	#print all except the duplicate
	
	b=set(x for x in alist if alist.count(x) >1)
	bb=str(b)
	bbb=bb.replace ('set([','')
	bbbb=bbb.replace('])','')
	print b
	print bbbb
	#print the duplicates
	
	c=set(x for x in alist if alist.count(x) ==1)
	cc=str(c)
	ccc=cc.replace ('set([','')
	cccc=ccc.replace('])','')
	print c
	print cccc
	#print not including the elements that are duplicated
	return
  
   
  
mylist=[1,1,2,3,5,6,7,8,9,10,7,6]
#uniq(mylist)
uniq_2(mylist)

