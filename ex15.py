# import argv from sys
from sys import argv

# unpack argv
script, filename = argv

# open 'filename' and assign it to txt
txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()  # do the 'read' command on txt

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
