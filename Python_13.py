# Write a program to find the biggest of 4 numbers.
# a) Read 4 numbers from user using Input statement.
# b) extend the above program to find the biggest of 5 numbers.
# (PS: Use IF and IF & Else, If and ELIf, and Nested IF)

k = []
n = int(input("Enter the no. of elements: "))

for i in range(0, n):
	k.append(int(input("Enter the numbers: ")))
	
max = k[0]
for i in k:
	if max == i:
		continue
	elif max > i:
		max = max
	elif max < i:
		max = i
		
print "The biggest of {} numbers provided by user is {}".format(n, max)