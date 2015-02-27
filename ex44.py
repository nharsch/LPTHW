#Inheritance

#	stay far away from inheritance if you can
#	multiple inheritance is the worst

# class Foo(Bar) =
#		make class Foo that inherits from Bar

#	3 ways that parent child classes can interact:
#		1. Actions on the child imply an aciton on the parent
#		2. Actions on the child override the action on the parent
#		3. Actions on the child alter the action on the parent.

#	Implicit inheritance:
#		define a function in the parent, but not in the child:

# class Parent(object): #defines class parent that inherits from object

# 	def implicit(self): #defines method that passes self as arg
# 		print "PARENT implicit()"

# class Child(Parent): #creates child class that inherits from Parent
# 	pass # creates an empty block, nothing new is defined

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

#	Override Explicitly

# class Parent(object):

# 	def override(self):
# 		print "PARENT override()"

# class Child(Parent):
# 	"""docstring for Child"""
# 	def override(self):
# 		print "CHILD override()"

# dad = Parent()
# son = Child()

# dad.override()
# son.override()

# Alter Before or After

# class Parent(object):
# 	"""docstring for Parent"""
	
# 	def altered(self):
# 		print "PARENT altered()"

# class Child(Parent):
# 	"""docstring for Child"""
# 	def altered(self):
# 		print "CHILD, BEFORE PARENT altered()" #overrides parent altered procedure
# 		super(Child, self).altered() #call super with args Child and self and run altered on what is returned
# 		print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.altered()
# son.altered()

# All three combined

# class Parent(object):

# 	def override(self):
# 		print "PARENT override()"

# 	def implicit(self):
# 		print "PARENT implicit()"

# 	def altered(self):
# 		print "PARENT altered()"

# class Child(Parent):

# 	def override(self): #explicit override
# 		print "CHILD override()"

# 	def altered(self): 
# 		print "CHILD, BEFORE PARENT altered()"
# 		super(Child, self).altered()
# 		print "CHILD, AFTER PARENT altered()"

# dad = Parent()
# son = Child()

# dad.implicit()
# son.implicit()

# dad.override()
# son.override()

# dad.altered()
# son.altered()

