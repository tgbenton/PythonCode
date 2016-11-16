# Calculator Python Program

x = input('Enter a number:  ')
y = input('Enter another number: ')
op = raw_input("What mathmatical operation do you want to perform? ")

if op == "+":
	print "The sum is:  ", float(x) + float(y)
elif op == "-":
	print "The difference is:  ", x - y
elif op == "*":
	print "The product is:  ", x * y
elif op == "/":
	print "The quotient is:  ", x / y
	


