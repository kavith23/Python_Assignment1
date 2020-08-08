# Write a program to read string and print each character separately.
# a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.
# b) Repeat the string 100 times using repeat operator *
# c) Read string 2 and concatenate with other string using + operator.

a = "Chennai"

for i in a:
	print i

print "\n\nRepeating the string a 100 times\n"
c = a*100
print c

print "\n\nConcatenating the string with other string\n"
b = "City"
s = a + " " + b
print s
	
