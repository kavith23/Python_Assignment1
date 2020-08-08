# Create a list of 5 names and check given name exist in the List.
# a) Use membership operator (IN) to check the presence of an element.
# b) Perform above task without using membership operator.
# c) Print the elements of the list in reverse direction.

a = ["Mary", "Paul", "John", "Caesar", "Roger"]

# Checking presence of an element in the list using membership operator
if "John" in a:
	print "\nThe element is available in the list"
else:
	print "\nThe element is not available in the list"

# Checking presence of an element in the list without using membership operator
count = count1 = 0
for i in a:
	if "John" == i:
		print "\nJohn is available in the list"
		count = 1
	else:
		count1 += 1
		continue
if count != 1:
	print "\nThe element is not available in the list"

print "\nPrinting the elements of the list in reverse direction"
b = a[::-1]		
for i in b:
	print i
