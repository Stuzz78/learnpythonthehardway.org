# import argv from sys
from sys import argv

# unpack argv
script, filename = argv

# prompt to erase (or not filename)
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

# wait for user's response
raw_input("?")

# open filename for Writing and truncates
print "Opening the file..."
target = open(filename, "w")

# truncate filename
# print "Truncating the file.  Goodbye!"
# target.truncate()

# get user input for 3 lines to write to filename
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# write lines to filename with a newline after each
print "I'm going to write these to the file."

target.write("%s\n%s\n%s\n" % (line1, line2, line3))

# close the file
print "And finally, we close it."
target.close()
