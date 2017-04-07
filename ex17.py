# imports!
from sys import argv
from os.path import exists

# unpack!
script, from_file, to_file = argv

# what are we doing?
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line, how?
in_file = open(from_file); indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output files exist? %r" % exists(to_file)
print "Ready, hit RETURN to contineu, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()
