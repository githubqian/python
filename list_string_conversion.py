#https://www.hackerrank.com/challenges/python-string-split-and-join
#http://stackoverflow.com/questions/8270092/python-remove-all-whitespace-in-a-string
#http://stackoverflow.com/questions/1876191/explain-python-join



li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print s
#'server=mpilgrim;uid=sa;database=master;pwd=secret'
s.split(";")
#['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s.split(";", 1)
#['server=mpilgrim', 'uid=sa;database=master;pwd=secret']
s.split("=")
#['server', 'mpilgrim;uid', 'sa;database', 'master;pwd', 'secret']
s.split()
#['server=mpilgrim;uid=sa;database=master;pwd=secret']
s = ",".join(li)
print s
#'server=mpilgrim,uid=sa,database=master,pwd=secret'
str(li).strip('[]')
#"'server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret'"

print s.split(",")
print str(li).strip('[]')


my_str = 'Today is Wednesday'
print (my_str)
print (' '.join(my_str))
print (''.join(my_str))
print (my_str.join("-"))
print ("-".join(my_str))
print (my_str.replace(' ',''))
print (my_str.split(" "))
print ("-".join(my_str.split(" ")))
