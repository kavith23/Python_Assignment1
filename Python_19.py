# Using loop structures print even numbers between 1 to 100.  
# a) By using For loop, use continue/ break/ pass statement to skip odd numbers.
# i) Break the loop if the value is 50
# ii) Use continue for the values 10,20,30,40,50

# b) By using while loop, use continue/ break/ pass statement to skip odd numbers.
# i) Break the loop if the value is 90
# ii) Use continue for the values 60,70,80,90

def loop_for(start, stop):
	a= []
	for i in range(start, stop):
		if i%2 == 0:
			if i == 50:
				break
			if i%10 == 0:
				continue
			a.append(i)
		else:
			pass
	return a

def loop_while(b, start, stop):
	while(start < stop+1):
		if start%2 == 0:
			if start%10 == 0:
				start += 1
				continue
			b.append(start)
		elif start == 90:
			break
		else:
			pass
		start += 1
	return b

b = loop_for(1, 51)
print "\nUsing for loop: {}".format(b)
print "\nUsing while loop: {}". format(loop_while(b, 51,100))

				
			