# Create a list with at least 10 elements having integer values in it;
# Print all elements
# Perform slicing operations
# Perform repetition with * operator
# Perform concatenation with other list.

a= [2, 3, 4, 5, 1, 9, 8, 7, 10, 6]

print "\nPrinting all elements in the list"
for i in a:
	print i

print "\nPerforming Slicing operations"	
c = a[7:]
print c

print "\nPerforming repetition with * operator"
d = c*5
print d

print "\nPerforming concatenation with other list"
b = [98, 99]
e = a + b
print e

