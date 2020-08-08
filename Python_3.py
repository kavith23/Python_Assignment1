# Write a program to find given number is odd or Even

a=int(input("Enter a number for the variable a: "))

if a <= 0:
	print "Try some other integer"
elif a%2 == 0:
	print "{} is even".format(a)
else:
	print "{} is odd".format(a)
