from os.path import exists

logfile = "add.log"

if not exists(logfile):
	print "Log file does not exists.  Creating logfile..."
	
target = open(logfile, 'a')

print "Enter two numbers: "
a = int(raw_input())
b = int(raw_input())

c = a + b
logentry = "The sum of the numbers is %d \n" % (c)

target.write(logentry)
print "The sum of the numbers is %d" % (c)

target.close()