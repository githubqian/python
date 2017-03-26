#http://stackoverflow.com/questions/931092/reverse-a-string-in-python

def reverse_string (my_string):

	#return (my_string[::-1])		//works
	reversed_string = my_string[::-1]
	return reversed_string
	
	
	
def reverse_string_2 (my_string):
	
	#return (''.join(reversed(my_string)))		//works	
	reversed_string = ''.join(reversed(my_string))
	return reversed_string
	
	
	
str = 'I am learning Python!'	
x = reverse_string(str)
y = reverse_string_2(str)
print x
print y