# Multiples: write code that prints all odd number from 1 to 1000//

for x in range(1,1000):
    if x%2!=0:
        print x

# Part 2 - Creat anotehr program that prints multiples of 5 from 5 to 1,000,000//

for y in range(5, 1000000):
    if y%5==0:
        # print y

# Sum List - create program that prints the sum of all the values in the list//

x = [1,2,5,10,255,3]
print sum(x)

# Average list - Create a program that prints the average of the values in the list//

x = [1,2,5,10,255,3]
print sum(x)/len(x)