## ex19 Functions and Variables


#creates a function that passes 2 vars and prints 4 statements, the first two reference 
#passed args
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man oh man"
	print "Get a blanket. \n"


print "We can just give the function numbers directly:"
#calls the above function, passes 20 and 30 as args
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
#sets up global vars
amount_of_cheese = 10
amount_of_crackers = 50

#calls function with global vars as args
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
#calls function with arithmetic expressions as args
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
#calls function with global vars as part of arithmetic expressions as args
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

##my own function

print "This is my own function:"
def notter(a):
	print "%s NOT!" % a
	print "That takes me back..."

notter("That's totally cool")

statement = "I am the greatest coder"

notter(statement)
