#ex33 while loops
numbers = []

def incer(top, incer):
	i = 0
	while i < top:
		global numbers
		print "At the top i is %d" % i
		numbers.append(i)
		i += incer
		print "Numbers now: ", numbers
		print "At the bottom is is %d" % i
		#numbers = []

def printnums():
	print "The numbers: "
	for num in numbers:
		print num
	
