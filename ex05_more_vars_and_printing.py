##ex05 More Variables and Printing

name = 'Nigel Harsch'
age = 27
height = (5*12) + 10 #inches
weight = 180 #lbs
eyes = 'Grey'
teeth = 'Yellowy'
hair = 'Mostly Gone'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." %teeth

#this line is tricky
print "If I add %d, %d, and %d I get %d." % ( age, height, weight, age + height + weight)
