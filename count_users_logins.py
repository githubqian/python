# TIME TO CELEBRATE! PROUD OF MYSELF!
# BY QIAN OUYANG 02/09/2017

def user_login_count(userlist):
	login = {}
	count = 0
	
	for x in userlist:
	
		count = userlist.count(x)
		login.update({x:count})
	
	return login
	
		
userlogin = ['a','b','c','d','e','f','g','a','a','c','d','b','e','f','a','a','b','b']
print (user_login_count(userlogin))	
