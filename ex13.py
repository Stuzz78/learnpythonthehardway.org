# import the argv function(?) from the sys module
from sys import argv

# unpack the argument variable (argv) into the 4 variables to the left of =
script, first, second, third = argv

# print the contents of the 4 variables unpacked from argv
print "The script is called:", script
print "your first variable is:", first
print "Your second variable is:", second
print "Your thrid variable is:", third
fourth = raw_input("Enter your fourth variable: ")
print "Your fourth variable is:", fourth
