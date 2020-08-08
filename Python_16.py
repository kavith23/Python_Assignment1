# Write program to perform following:
# i) Check whether given number is prime or not.
# ii) Generate all the prime numbers between 1 to N where N is given number.

n = int(input("Input n: "))
prime_no = []

def prime(a):
	for i in range(2, a):
		if a % i == 0 :
			break
	else:
		return a

if n > 1:
	for i in range(1, n):
		if i == 1:
			continue
		else:
			a = prime(i)
			if a:
				prime_no.append(a)
	print "\nPrime numbers between 1 to {} is : {}".format(n, prime_no)
else:
	print "\nEnter a valid input next time"

	

