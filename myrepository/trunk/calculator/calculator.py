#!/usr/bin/python

class Calculator(object):

    def add(self, x, y):
        number_types = (int, long, float, complex)

        if isinstance(x, number_types) and isinstance(y, number_types):
            return x + y
        else: 
            raise ValueError

    def subtract(self, x, y):
	number_types = (int, long, float, complex)
	
	if isinstance(x,number_types) and isinstance(y, number_types):	
	    return x - y
	else:
	    raise ValueError
    def multiply(self, x, y):
	number_types = (int, long, float, complex)
	
	if isinstance(x, number_types) and isinstance(y, number_types):
	   return x * y 
	else:
	    raise ValueError 
    def divide(self, x, y):
	number_types = (int, long, float, complex)
	
	if isinstance(x, number_types) and isinstance(y, number_types):
	   return x / y
	else: 
	    raise ValueError

#if __name__ == '__main__':
 #   print "hello" 
  #  pass
