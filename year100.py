import datetime

now = datetime.datetime.now()

#name = input('Enter your name> ')
name = raw_input('Enter your name> ')

age = input('Enter your age> ' )
age = int(age)

year100 = (100 - age) + now.year

print "Current year %d" % now.year

print "%s, you are currently %d years old.  You will reach age 100 in the year %d" % (name, age, year100)