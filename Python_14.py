# Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation
# a) Print all names on to screen
# b) Read the index from the  user and print the corresponding name from both list.
# c) Print the names from 4th position to 9th position
# d) Print all names from 3rd position till end of the list
# e) Repeat list elements by specified number of times (N- times, where N is entered by user)
# f)  Concatenate two lists and print the output.
# g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

a = ["1234", "4532", "1356", "9845", "9834", "3456", "4321", "8745", "4325", "7623"]
b = ["Mary", "Paul", "John", "Cloe", "Roger", "Smith", "Nikil", "Victor", "David", "Christy"]

print "\nPrinting all names on to screen"
for i in b:
	print i
	
n = int(input("Please enter an index value: "))
print "The entry in list a corresponding to the user index is {}".format(a[n])
print "The entry in list b corresponding to the user index is {}".format(b[n])

k = b[3:9]
print "\nThe names from 4th to 9th position is as follows:"
for i in k:
	print i

l = b[2:]
print "\nThe names from 3rd to last position is as follows:"
for i in l:
	print i

k = int(input("Enter the repetition rate: "))
print "\nThe repetition of list a {}".format(a*k)
print "The repetition of list b {}".format(b*k)

print "\nThe concatenation of two lists is {}".format(a+b)

print "\nPrinting element of list A and B side by side"
for i, j in zip(a, b):
	print i, j
