from sys import argv

# Setting up two command line variables 
script, filename = argv
# opening the file whose name is stored in filename variable and storing that opened file in txt
txt = open(filename)
# Printing the name of the file
print "Here's your files %r:" % filename
# txt.read will read the whole file and with the help of print command will print the contents on the console
print txt.read()


print "Type the filename again:"
# Taking the filename input from the user and storing it in file_again variable
file_again = raw_input("> ")
# Opening the file in the file_again variable and storing it in the variable txt_again
txt_again = open(file_again)
# Printing the whole content of the file on the console using the read function on the txt_again
print txt_again.read()
# Closing both the files using the close function on the both the file variables
txt.close()
txt_again.close()


