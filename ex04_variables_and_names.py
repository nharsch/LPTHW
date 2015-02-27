# Ex04 Variables and Names

#creates variables
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90

#maps difference of cars and drivers to new var
cars_not_driven = cars - drivers
#maps drivers to new var
cars_driven = drivers
#maps cars_driven * space_in_a_car to new var
carpool_capacity = cars_driven * space_in_a_car
#divides passengers by cars and maps to new var
average_passengers_per_car = passengers / cars_driven

#prints messages and vars
print "There are", cars, "cars available."
print "there are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
#capacity
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
	
