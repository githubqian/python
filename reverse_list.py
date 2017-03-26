elements = [1,2,3,4,5,6,7,8]
x = len(elements)
y = elements.__len__()
reverse_elements = []

print '%d' % x
print '%d' % y
print(x)
print(y) 

# method 1
i = x-1
while i >= 0:
	reverse_elements.append(elements[i])
	i = i-1
		
for value in elements:	
	print(value)
	
for value in reverse_elements:	
	print(value)
	
	
fruits = ['apple','orange','pear','strawberry']
reverse_fruits = []
reverse_fruits2 = []

# method 1'
i = len(fruits)-1
while i>=0:
	reverse_fruits.append(fruits[i])
	i-=1

# method 2	
j = len(fruits)-1
for j in range (len(fruits)-1, -1, -1):
	reverse_fruits2.append(fruits[j])
	
for item in fruits:
	print(item)
	
for item in reverse_fruits:
	print(item)

for item in reverse_fruits2:
	print(item)
	
print(elements)
