# greeting = "Bruce"
# _myName = "Tim" # Can use an _ (underscore) for the variable name
# Tim_Was_57= "Hello" # Cannot start a variable name with a number but you can include a number in the variable name
# Greeting = "There"  # Variables are case sensitive so this is different from greeting
#
# print(Tim_Was_57 + ' ' + Greeting + ' ' + greeting)
#
# age = 24
#
# print(age)
#
# print(greeting + ' ' + str(age))

#
# a = 12
# b = 3
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b) # returns a float
# print(a // b) # returns an integer
# print(a % b) # returns the remainder
# print("\n")
#
# for i in range(1, a//b):
#     print(i)

# a = 12
# b = 3
# print(a + b / 3 - 4 * 12)
# print(8 / 2 * 3)  # IndexError: string index out of range
# print(8 * 3 / 2)
#
# print((((a + b) / 3) - 4) * 12)
#
# c = a + b
# d = c / 3
# e = d - 4
# print(e * 12)

parrot = "Norwegian Blue"
print(parrot)

print(parrot[3]) # counting starts at 0 (zero)
print(parrot[0])
# print(parrot[14]) This gives an error because there is no character at [14], IndexError: string index out of range
print(parrot[-1])  # To reach the last character in the string you can go to [-1] or [13]
print(parrot[13])
print(parrot[0:6]) # Print a range of characters in a string using n:n
print(parrot[:6]) # When no number is specified before the colon, it starts from the beginning
print(parrot[6:]) # When no number is specified after the colon, it starts at the character specified and goes
 #                  to the end of the string
print(parrot[-4:2]) # This does not give us anything since it is bi-directional
print(parrot[-4:-2]) # This does work since it is a range in the same direction
print(parrot[0:6:2]) # This starts at char 0 and goes to the 6th char and prints every 2nd character
print(parrot[2:10:3]) # This starts at char 2 and goes to the 10th char and prints every 3rd character

number = "9,223,372,036,854,775,807"
print(number[1::4])

number = "1, 2, 3, 4, 5, 6, 7, 8, 9"
print(number[0::3])

string1 = "he's "
string2 = "probably "
print(string1 + string2)
print("he's " "probably " "pining") # Not the best way to do this but shows what you can do with strings

print("Hello " * 5) # Repeats the string 5 times.  Operator precedence applies
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "friday"
print("day" in today) # checks to see if "day" is in the string assigned to today, friday.  This is true
print("fri" in today) # true
print("thur" in today) # false

print("parrot" in "fjord") # checks explicit strings as well.  This is false




