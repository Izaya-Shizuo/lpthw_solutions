# Defining the function here with two arguments. The function prints the values of the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" %cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket .\n"

print "We can just give the function numbers directly:"
# Directly give the values to the arguments of the functions
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
# Giving the variables their values and defining them as the arguments of the functions
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
# Performing the addition and assigning those values to the arguments of the function
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
# Same thing here we just add a constant with variable and assigning their sum to the arguments of the function
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)

	
