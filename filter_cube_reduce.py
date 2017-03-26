#http://www.python-course.eu/lambda.php

def f(x):
       return x % 2 != 0 and x % 3 != 0
x=filter(f, range(2, 25))
print x
#[5, 7, 11, 13, 17, 19, 23]


def cube(x):
    return x*x*x
y=map(cube, range(1, 11))
print y
#[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


def add(x,y):
    return x+y
z=reduce(add, range(1, 11))
print z
#55
