a = int(input("Enter a number: "))

if a > 2:
	for i in range(2, a):
		if a % i == 0 :
			print "The given number ", a, "is not prime"
			break
	else:
		print "The given number ", a, "is prime"
else:
	print "Please enter a different number next time"
