# Write a program that prints a "Checkerboard" pattern to console.//
# Should require no input and produce an output as follows///


def Checkerboard():
    for i in range(10):
        if i%2 == 0:
            print "* * * * * "
        if i%2 == 1:
            print " * * * * *"
Checkerboard()