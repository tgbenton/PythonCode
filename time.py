from sys import argv
from os.path import isfile, exists, getmtime
from time import gmtime, strftime, localtime

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists (to_file)
print "Does the output file exist? %r" % isfile (to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done.  The file was updated at %s localtime" % (strftime('%Y-%m-%d %H:%M:%S', localtime(getmtime(to_file))))
print "Alright, all done.  The file was updated at %s GMT" % (strftime('%Y-%m-%d %H:%M:%S',  gmtime(getmtime(to_file))))

print "GMT Time is %s" % (strftime('%Y-%m-%d %H:%M:%S', gmtime()))
print "The current local time is %s" % (strftime('%Y-%m-%d %H:%M:%S', localtime()))

out_file.close()
in_file.close()
