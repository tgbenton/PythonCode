# Import the sys.argv library
from sys import argv

# argv accepts 2 arguments
script, filename = argv

# create a file object for the filename and assign it to the variable txt.
txt = open(filename)

# print the filename and print out the contents of the file.
print "Here's your file %r: " % filename
print txt.read()

# accept the filename forom user input
print "Type the filename again: " 
file_again = raw_input("> ")

# open the filename again and assign it to txt_again
txt_again = open(file_again)

# read and print the contents of the filename opened by txt_again
print txt_again.read()