# Here the integer value 10 will replace the %d in the printing of the string
x = "There are %d types of people." % 10
# Variable binary is assigned the value or string "binary"
binary = "binary"
# Variable do_not is assigned the value or string "don't"
do_not = "don't"
# Variable y is assigned the string where the %s will be replaced by the 
# values stored in the variables binary and do_not
y = "Those who know %s and those who %s." % (binary, do_not)
# Printing the value of x
print x
# Printing the value of y
print y
# The string will get printed with the %r gettin' replaced with the value storedin the variable x 
print "I said: %r." % x
# The string will get printed with the %s gettin' replaced with the value storedin the variable y 
print "I also said: '%s'." %y

# Assigning the value of False to the variable hilarious
hilarious = False
# Assigning joke_evaluation with the string
joke_evaluation = "Isn't that joke so funny?! %r"
# Printing the value of joke_evaluation with %r gettin' replaced with the value of the variable hilarious
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."
#Here w and e are two variables which have been assigned with two separate string and in the print statement we are printing there combined value
print w+e
