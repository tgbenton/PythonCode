from sys import argv

script, filename = argv

txt = open(filename)

print "Below are the contents of the file %r" % filename
print txt.read()