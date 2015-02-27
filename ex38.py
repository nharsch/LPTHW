#Exercise 38 Doing Things To Lists

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ') # takes a string and splits it on chr, populates list with words

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # while the amount of elements is less than 10
	next_one = more_stuff.pop() # removes last element of list, assigns it to var
	print "Adding: ", next_one 
	stuff.append(next_one) # adds var as element to the end of the list
	print "There's %d items now." % len(stuff) 

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1] # prints second element of list
print stuff[-1] # prints last element of list
print stuff.pop() # removes last element from list, prints element
print ' '.join(stuff) #takes list and returns string of elements separated by ' '
print '#'.join(stuff[3:5])

