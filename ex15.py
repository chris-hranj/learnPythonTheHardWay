from sys import argv

script, filename = argv

#open file indicated in argument
txt = open(filename)

#read file
print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
txt.close()
