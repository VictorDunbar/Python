#Multiples part 1

def oddnumbers():
    for x in range(1, 1000, 2):
        print x

#Multiples part 2

def byFive():
    for y in range(5, 1000, 5):
        print y

#Sum List

def sumList():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for y in range(0, len(a)):
        sum += a[y]
        print sum

#Average List
def avgList():
    a = [1, 2, 5, 10, 255, 3]
    sum = 0
    for y in range(0, len(a)):
        sum += a[y]
    avg = sum/len(a)
    print sum
