# this one is like your scritps with argv

def print_two(*args):
	arg1, arg2 = args
	print "arg1:  %r, arg2:  %r" % (arg1, arg2)
	
# ok, that *args is actually pointless, we can just do this

def print_two_again(arg1, arg2):
	print "arg1:  %r, arg2:  %r" % (arg1, arg2)
	name = arg1 + ' ' + arg2
	print name
	
# this just takes one argument

def print_one(arg1):
	print "arg1: %r" % arg1
	
# this one takes no arguments
	
def print_none ():
	print "I got nothin'."
	
print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

print_two_again("Tim", "Benton")
