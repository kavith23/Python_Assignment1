## Write a program to find the biggest of 3 numbers

a=int(input("Enter a number for the variable a: "))
b=int(input("Enter a number for the varibale b: "))
c=int(input("Enter a number for the varibale c: "))

if a>b and a>c:
	print "{} is the biggest of all numbers".format(a)
elif b>a and b>c:
	print "{} is the biggest of all numbers".format(b)
elif c>a and c>b:
	print "{} is the biggest of all numbers".format(c)

