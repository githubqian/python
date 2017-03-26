def fib(n):
#start with 0 as the first number
		if (n==0):
			return 0
			
		if (n==1):
			return 1
			
		else:
			return fib(n-1)+fib(n-2)
	

y=map(fib, range(0,11))
print y
#print all fibonacci numbers for postions in the range
#note: no indentation here
	
print fib(5)
#print the 5th fibonacci number

def fib_2(n):
#start with 1 as the first number
		if (n==1):
			return 1
			
		if (n==2):
			return 1
			
		else:
			return fib(n-1)+fib(n-2)
	

z=map(fib, range(1,11))
print z
