# Ex 42: Is-A, Has-A, Objects, Classes

## Animal is-a object (yes, sort of confusing) look at the extra credit

## Creates Class Animal that is an object
class Animal(object):
	pass

## creates class Dog that is an instance of Animal
class Dog(Animal):
	#takes self and name as args
	def __init__(self, name):
		## ??
		self.name = name

class Cat(Animal):

	def __init__(self, name):
		##??
		self.name = name

class Person(object):

	def __init__(self, name):
		##??
		self.name = name

		## PErson has--a pet of some kind
		self.pet = None

class Employee(Person):

	def __init__(self, name, salary):
		## ?? what is this
		super(Employee, self).__init__(name)
		##
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")

##
satan = Cat("Satan")

mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

crouse = Salmon()

harry = Halibut()

'''
from PyDoc:

A namespace is a mapping from names to objects. Most 
namespaces are currently implemented as Python dicts.

The important thing to know about namespaces is that there is 
absolutely no realtion between names in different namespaces;
for instance, two different modules may both
define a function "maximize" without confusion -- users of the
modules must prefix it with the module name.

Attribute if used for any name following a dot

attributes may be read-only or writable. In the latter case,
assignment to attributes is possible. Module attributes are 
writable: you can write modname.the_answer = 42.

Writable attributes may also be deleted with the del statement.
For example, del modname.the_answer will remove the attribute 
the_answer from the object named modname.




