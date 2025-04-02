import sys

#check for errors
if len(sys.argv) < 2:
    sys.exit("too few arguments")

elif len(sys.argv) > 2:
    sys.exit("too many arguments")

#print less tags

print("hello, my name is", sys.argv[1])
