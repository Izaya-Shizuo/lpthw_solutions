from sys import argv
# Assigning script and input_file as arguments during the command 
script, input_file = argv
# Defining the function to print the whole content of the file
def print_all(f):
	print f.read()
# Defining the function to move the cursor back to the first line of the file
def rewind(f):
	f.seek(0)
# Defining the function to print the lines of the file one at a time
def print_a_line(line_count, f):
	print line_count, f.readline()
# File object storing the value of the file input_file
current_file = open(input_file)
# Printing the statement here
print "First let's print the whole file:\n"
# Calling the function with current_file as the argument
print_all(current_file)
# Printing the statement
print "Now let's rewind, kind of like a tape."
# Calling the function with current_file as the argument
rewind(current_file)
# Printing the statement
print "Let's print three lines:"
# Assigning the value of 1 to the variable current_line
current_line = 1
# Calling the function with current_line and current_file as the arguments. Here the current_line is equal to line_count
print_a_line(current_line, current_file)
# Adding the constant 1 to the value stored in the variable in current_line and then calling the function with the same arguments
current_line += 1
print_a_line(current_line, current_file)
# Adding the constant 1 to the value stored in the variable in current_line and then calling the function with the same arguments
current_line += 1
print_a_line(current_line, current_file)
