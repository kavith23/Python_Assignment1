# Write a program to receive 5 command line arguments and print each argument separately.
# Example: >> python test.py arg1 arg2 arg3 arg4 arg5
# a) From the above statement your program should receive arguments and print them each of them. 
# b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

import sys

for i in range (1, len(sys.argv)):
	print sys.argv[i]
	
a=int(sys.argv[1])
b=int(sys.argv[2])
c=int(sys.argv[3])
	
print "The biggest of three numbers is ", max(a, b, c)
	
