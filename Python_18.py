# Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing)
# a) By using For loop 
# b) By using while loop
# c) Let mystring ="Hello world"
# print each character of mystring in to separate line using appropriate loop structure.

def loop_for(start, stop, step):
	a = []
	for i in range(start, stop, step):
		a.append(i)
	return a
	
def loop_while(n, step):
	i = 1
	a = []
	if step == 1:
		while(i < n):
			a.append(i)
			i += step
	elif step == -1:
		while(n > 0):
			a.append(n)
			n += step
	return a
			
print "Using for loop: {}".format(loop_for(1, 101, 1))
print "Printing in reverse using for loop: {}".format(loop_for(100, 0, -1))
print "Using while loop: {}".format(loop_while(101, 1))
print "Printing in reverse using while loop: {}".format(loop_while(100, -1))

mystring ="Hello world"
print "\nPrinting each character of mystring in to separate line:"
for i in mystring:
	print i

