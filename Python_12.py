# Read 10 numbers from user and find the average of all.
# a) Use comparison operator to check how many numbers are less than average and print them
# b) Check how many numbers are more than average.
# c) How many are equal to average.

n = 10
count1 = count2 = count3 = 0
a = []

for i in range(0, n):
	k = int(input("Enter a number: "))
	a.append(k)

avg = sum(a)/n
print "Average: {}".format(avg)

for i in a:
	if i < avg:
		count1 += 1
	if i > avg:
		count2 += 1
	if i == avg:
		count3 += 1

print "{} numbers are less than average".format(count1)		
print "{} numbers are more than average".format(count2)		
print "{} numbers are equal to average".format(count3)		



