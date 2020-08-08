# Create a tuple with at least 10 elements having integer values in it;
# Print all elements
# Perform slicing operations
# Perform repetition with * operator
# Perform concatenation with other tuple.

a= (1,3,5,7,9,2,4,6,8,10)

print "\nPrinting all elements"
for i in a:
	print i

print "\nPerforming slicing operation"	
c = a[7:]
print c

print "\nPerforming repetition with * operator"
d = c*5
print d

print "\nPerforming concatenation with other tuple"
b = (90,99)
e = a + b
print e