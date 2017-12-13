# Write a program that takes a list and prints a message for each element in the list, based on that element's data type.//
# Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.//

a = ["Deion Sanders", 21, " is", 23, " G.O.A.T"]
def typeList(lis):
        stri = ''
        count1 = 0
        added = 0
        count2 = 0
        for i in lis:
            if type(i) == str:
                stri += i
                count1 += 1
            elif type(i) == int or type(i) == float:
                added += i
                count2 += 1
        if count1 > 0 and count2 > 0:
            print ('The list You entered is a mixed type')
            print stri
            print added
        elif count1:
            print ('The list You entered is a string type')
            print stri
        elif count2:
            print ('The list You entered is an integer type')
            print added

typeList(a)



