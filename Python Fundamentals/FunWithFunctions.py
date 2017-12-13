# Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether it's an odd or even number.//
def odd_even():
    for i in range(1, 2001, 1):
        if i % 2 == 0:
            print ("Number is " + str(i) + " This is an even number!")
        if i % 2 == 1:
            print ("Number is " + str(i) + " This is an odd number!")

odd_even()

# Multiply each value in the list by 5

a = [2,4,10,16]
b = []
def multiply():
    for x in a:
        b.append(x * 5)
        print b
multiply()

# Hacker Challenge: should return the multiplied list as a two-dimensional list//

def hackChal(lst):
    y = []
    for i in lst:    
        listinlist = []
        for k in range(0,i):
            listinlist.append(1)
        y.append(listinlist)
    print y

hackChal([10,2,18])