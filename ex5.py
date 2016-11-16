name = 'Zed A. Shaw'
age = 35
height = 74
weight = 180.75
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
kg_per_pound = 2.2
kg_weight = float(weight) * float(kg_per_pound)

print "Let's talk about me %s." %name
print "He's %d inches tall." %height
print "He's %d pounds... or %d kilograms heavy." %(weight, kg_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." %(eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." %(age, height, weight, age + height + weight)
