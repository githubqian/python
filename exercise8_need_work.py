def check_anagram (alist, blist):
	if len(alist)!=len(blist):
		return False
		
	elif len(alist)==len(blist):
		for item in alist:
			for i in range (0, len(blist)):
				if blist[i]==item:
					print i
				else:
					return False
		return True

	else:
		return False			
					
alist='abcde'
blist='deacd'
clist='deacb'
dlist='haveit'
print check_anagram(alist,blist)
print check_anagram(blist,alist)
print check_anagram(alist,clist)
print check_anagram(alist,dlist)			