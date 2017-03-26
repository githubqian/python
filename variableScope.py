#!/usr/bin/python

total = 0

def add():
  global total
  total = 1+3
  print "total inside function: ", total

add()

print "total oustside function: ", total

#------------------------

mylist = [10,20,30]
myvar = 10

def changeme(mylist,myvar):
  mylist.append([1,2,3])
  myvar = 20

changeme(mylist,myvar)
print mylist
print myvar


#-------------------------

def test1():
  myvar = 99
  print myvar

test1()
