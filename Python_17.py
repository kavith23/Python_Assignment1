# Write program to find the biggest and Smallest of N numbers.
# PS: Use the functions to find biggest and smallest numbers. 

def biggest(user_list):
	max = user_list[0]
	for i in user_list:
		if max > i:
			max = max
		elif max < i:
			max = i
		elif max == i:
			continue
	return max
	
def smallest(user_list):
	min = user_list[0]
	for i in user_list:
		if min < i:
			min = min
		elif min > i:
			min = i
		elif min == i:
			continue
	return min

n = int(input("Enter the limit : "))
a = []
if n > 0:
	for i in range(0, n):
		k = int(input("Enter the number: "))
		a.append(k)
	print "\nThe Maximum number in the list is {}".format(biggest(a))
	print "The Minimum number in the list is {}".format(smallest(a))
else:
	print "\nEnter a valid limit"

	


		
		
	
