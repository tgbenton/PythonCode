age = 24
# print("My age is " + age + " years") # TypeError: Can't convert 'int' object to str implicitly
print("My age is " + str(age) + " years")

print("My age is {0} years".format(age)) # Use a replacement field {n}

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7} ".format(31, "January", "March",
    "May", "July", "August", "October", "December" ))

print("""January: {2}
February: {0}
March: {2}
April: {1}
May: {2}
June: {1}
July: {2}
August: {2}
September: {1}
October: {2}
November: {1}
December: {2}""".format(28,30,31)) # values can be reused, also they can be used out of order.  Jan starts with {2}

print("My age is %d years" % age)
print("My age is %d %s, %d, %s" % (age, "years", 6, "months"))

for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %4d" %(i, i ** 2, i ** 3)) # i, (i ** 2) i-squared, (i * * 3) i-cubed

print("PI is approximately %12f" % ( 22 / 7 )) # formatting the output using formatting operators %12f
print("PI is approximately %12.50f" % ( 22 / 7 )) # formatting the output using formatting operators %12.50f

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3)) # using replacement fields
# {0:2} = value 0 for a width of 2.  {1:4} = value 1 for a width of 4 ...

for i in range(1, 12):
    print("No. {0:2} squared is {1:<4} and cubed is {2:<4}".format(i, i ** 2, i ** 3)) # use < to left align the values


print("PI is approximately {0:12.50}".format( 22 / 7 )) # converting old style modifiers to the new .format style

for i in range(1, 12):
    print("No. {} squared is {} and cubed is {:4}".format(i, i ** 2, i ** 3)) # without specifying the first value
# python assumes they are in order...  0, 1, 2... Values cannot be used more than once.




