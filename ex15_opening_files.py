#imports argv from sys module
from sys import argv

#sets script and filename vars to command line args passed after python is called
script, filename, = argv

# sets txt var to open(filename), var is not "filename" but the file object
txt = open(filename)

#prints prompt with filename
print "Here's your file %r:" % filename

#calls read() function on txt object, (which is open("filename")), prints
print txt.read()

#prompts username to input filename
print "Type the filename again:"
#creates new var file_again and inputs user input string
file_again = raw_input("> ")

#puts contents of file in var txt_again
txt_again = open(file_again)

#calls read() function on txt_again, prints
print txt_again.read()

txt.close()
txt_again.close()

