def check_palindrome(astring):
	for i in range (0, len(astring)/2):
		if (astring[i]==astring[len(astring)-1-i]):
			return True
		else:
			return False
			
			
string1='nurses run'
#not sure why above is a palindrome
string2='kayak'
string3='nottrue'
string4='it is a rainning day'

print check_palindrome(string1)
print check_palindrome(string2)
print check_palindrome(string3)
print check_palindrome(string4)