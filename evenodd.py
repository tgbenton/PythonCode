
print "Check if a number is even or odd."
print "Enter a number: "
input_num = int(raw_input())

if (input_num % 2):
	print "%d is an odd number" % input_num
else:
	print "%d is an even number" % input_num
	
if not (input_num % 4):
	print "%d is also divisible by 4" % input_num
	
print "Enter two numbers to check if the first number is divisible by the second number."
print "Enter the first number:"
input_num = int(raw_input())
print "Enter a number to check if it is divisible by the first number: "
check_num = int(raw_input())

if not (input_num % check_num):
	print "%d is divisible by %d" % (input_num, check_num)
else:
	print "%d is not divisible by %d" % (input_num, check_num)
	
print "Done!"