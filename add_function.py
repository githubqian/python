#Three ways to do addition with variable munbers of variables to add

def add (*var):
    total = 0

    for i in var:
        #print i
        total =total + i
        #print sum
    return total


def my_sum (*var):
    return sum(var)


def my_add (*var):
    return reduce((lambda x, y: x + y), var)

        
x = add (100,55,81)
print(x)
#236

y = my_sum (1,10,20,01)
print y
#32

z = my_add (8,10,100)
print z
#118

