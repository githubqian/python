
def fab_num(n):
	
		if n == 0:
			return 0
		
		elif n == 1:
			return 1

		else:
			return fab_num(n-1) + fab_num(n-2)
			
			
n=10
tenth_value = fab_num(10)
print (tenth_value)			

