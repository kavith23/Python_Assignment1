## Write a program to Add, Subtract, Multiply, and Divide 2 numbers
def sum(c,d):
	e = c + d
	return e

def diff(c,d):
	if c>d:
		e = c - d
	else:
		e = d - c
	return e

def mul(c,d):
	e = c * d
	return e
	
def div(c,d):
	e = c/d
	return e

a=int(input("Enter a number for the variable a: "))
b=int(input("Enter a number for the varibale b: "))

print "Sum is {}".format(sum(a,b))
print "Diff is {}".format(diff(a,b))
print "Pdt is {}".format(mul(a,b))
print "Div is {}".format(div(a,b))


	
