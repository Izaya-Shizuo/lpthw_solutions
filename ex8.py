# Assigning the variable formatter with 4 5r formatters
formatter = "%r %r %r %r"
# Prints the value of 1234 in place of the four %r in the formatter variable
print formatter % (1, 2, 3, 4)
# Prints the value one two three four in place of the four %r in the formatter variable
print formatter % ("one", "two", "three", "four")
# Prints the value of True False False True in place of the four %r in the formatter variable
print formatter % (True, False, False, True)
# Prints the value of formatter in place of the %r in the formatter variable i.e. %r %r %r %r
print formatter % (formatter, formatter, formatter, formatter)
# Prints the four strings given below in the place of the 4 %r in the formatter variable
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)
