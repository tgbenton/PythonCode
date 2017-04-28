from sys import argv

script, filename = argv

print "Script is: %r" % script
print "Filename is: %r" % filename

print "We're going to erase %r." % filename
print "If you dont want that, hit CTRL-C (^C)."
print "If you do want that, hit ENTER."

raw_input (">")

print "Opening the file..."
target = open(filename, 'w')

print "Truncating the file..."
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm goint to write these to the file, %r. \n" % filename

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")


print "The contents of the file now contain this: "
target = open(filename)
print target.read()

#line = target.readline()
#print "Line 1:  " % (line)

print "And finally, we close it...  Goodbye!"
target.close()
