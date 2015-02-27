#Ex36 Designing and Debugging

'''
Rules for if statements
1	Every if statement must have an else

2	If this else should never be run because it doesn't make sense, then you must use a die function in the else that prints out an error message and dies. This will find many errors.

3	Never nest if-statements more than two deep and always try to do them one eep. This means if you put an if in an if then you should be looking to move that second if into another function.

4	Treat if-statements like paragraphs, where each if elif else grouping is like a set of sentences

5	Your boolean tests should be simple. If they are complex, move thier calculations to variables earlier in you function and use a good name for the variable

Remember, these rules are guidlines to better programming, but if you find them pointless in a given context, consider throwing them out.


Rules for Loops

1	Use a while-loop only to loop forever, and that means probably never. This only applies to Python.

2	Use a for-loop for all other kinds of looping, especially if there is a fixed or limited number of things to loop over.


Tips for Debugging

1	Do not use a "debugger."

2	The best way to debug a program is to use print to print out the values of variables at points in the program to see where they go wrong.

3	Make sure parts of your programs work as you work on them. Do not write massive files of code before you try to run them. Code a little, run a little, fix a little.


