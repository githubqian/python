#!/usr/bin/python

def test(self, *var):
  for v in var:
    print v
    self.add(v)
  #x = var
  #x.append([10])

test(1,2,3)
