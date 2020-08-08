# Write a program to generate a Fibonacci series of numbers.
# Starting numbers are 0 and 1,  new number in the series is generated by adding previous two numbers in the series.
# Example : 0, 1, 1, 2, 3, 5, 8,13,21,.....
# a) Number of elements printed in the series should be N numbers, Where N is any +ve integer.
# b) Generate the series until the element in the series is less than Max number.

def fib_series(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	else:
		return (fib_series(n-2)+fib_series(n-1))

n = int(input("Enter the limit: "))
if n:
	print "Fibonacci series for n={} is as follows:".format(n)
	for i in range(0, n):
		k = fib_series(i)
		print k
else:
	print "\nEnter a new limit next time"