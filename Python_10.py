# Using assignment operators, perform following operations
# Addition, Substraction, Multiplication, Division, Modulus, Exponent and Floor division operations

def sum(a, b):
	a += b
	return a

def sub(a, b):
	a -= b
	return a

def mul(a, b):
	a *= b
	return a

def div(a, b):
	a /= b
	return a

def mod(a, b):
	a %= b
	return a

def exp(a, b):
	a **= b
	return a

def floor(a, b):
	a //= b
	return a
	
a = int(input("Enter a: "))
b = int(input("Enter b: "))


print "The sum of two numbers is ", sum(a, b)
print "The sub of two numbers is ", sub(a, b)
print "The mul of two numbers is ", mul(a, b)
print "The div of two numbers is ", div(a, b)
print "The mod of two numbers is ", mod(a, b)
print "The exp of two numbers is ", exp(a, b)
print "The floor of two numbers is ", floor(a, b)
