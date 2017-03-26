
def login_count(userloginlist):

	login = {}
	count = 0

	for user in userloginlist:
		count = userloginlist.count(user)
		login.update({user:count})
		
	return login
	
	
my_list = ['a','b','a','b','c','d','e','f','f','d','a','a','a','b','x','y','A','B']
mylist = [1,2,3,4,1,2,56,77]

print (login_count(my_list))
print login_count(mylist)
	