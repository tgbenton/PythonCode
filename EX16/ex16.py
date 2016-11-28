#from sys import argv

#script, filename = argv

filename = "ex16_sample.txt"

print ("We're going to erase {0}.".format (filename))
print ("If you dont want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input ("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file.  Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm goint to write these to the file. \n")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print ("The contents of the file now contain this: ")

target = open(filename)
print(target.read())

print ("\nAnd finally, we close it.")
target.close()
