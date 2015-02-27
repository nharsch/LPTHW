#ex 20
from sys import argv #imports argv from sys

script, input_file = argv #sets vars to args

def print_all(f): #function takes a file object as arg
	print f.read() #calls read function on object and prints
	
def rewind(f): 
	f.seek(0) #calls seek function on file object, passing 0 as arg
	#seeking resets read pos?

def print_a_line(line_count, f): #takes two args
	print line_count, f.readline() #prints 1st arg, calls readline() on 2nd arg & prints
	
current_file = open(input_file) #sets global var to input_file object

print "First let's print the whole file: \n"

print_all(current_file) #calls function on current_file obj

print "Now let's rewind, kind of like a tape."

rewind(current_file) #calls seek on current_file, sets read point to 0

print "Let's print three lines:"

current_line = 1 #sets var
print_a_line(current_line, current_file) #calls funciton, passes var as 1st arg

current_line += 1 #increments var
print_a_line(current_line, current_file) #calls function with updated var num

current_line +=1 #increments var again
print_a_line(current_line, current_file) #calls function again with updated var num
