def factorial(n):

	if (n==0):
		return n
		
	else:
		f=1
		for i in range(1,n+1):
			f=f*i
		return f
				
print factorial(0)
print factorial(1)
print factorial(5)
print factorial(100)	


def factorial_2(n):
	f=1
	i=1
	while i<=n:
		f=f*i
		i=i+1
	return f
		
print factorial_2(5)


def factorial_3(x):

	if (x==0):
		return x
		
	else:
		f=1
		for i in range(1,x+1):
			f=f*i
		return f
    
z=map(factorial_3, range(1, 11))
#actually mean to gat factorial of a range of numbers, e.g. factorial of 1, 2, 3, ... to 10
print z			