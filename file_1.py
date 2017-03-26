
#import codecs
#try:

str = raw_input("Enter your input: ")
print "Received input is : ", str

# Open a file
fh = open("hello_world.txt", "ab+")
print "Name of the file: ", fh.name
print "Closed or not : ", fh.closed
print "Opening mode : ", fh.mode
print "Softspace flag : ", fh.softspace

print "\n"
fh.write(str)
fh.write("\nPython is a great language\n")

#finally:
fh.close()
