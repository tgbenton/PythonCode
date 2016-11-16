print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()
print "Type any number...",
extra = int(raw_input())

print "Type any statement...",
extraStmt = str(raw_input())

print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)
print "%d" % extra
print "%s" % extraStmt
