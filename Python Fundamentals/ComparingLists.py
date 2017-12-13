# Write a program that compares two lists and prints a message depending on if the inputs are identical or not.
# Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list1 = [1,2,5,6,34]
list2 = [1,2,5,6,34]

list3 = [1,2,5,6,33,34]
list4 = [1,2,5,6,34]

list5 = ['celery','carrots','bread','milk']
list6 = ['celery','carrots','bread','cream']

def compareList(first, second):
    first.sort()
    second.sort()
    if first == second:
        print "The lists are the same."
    else:
        print "the lists are not the same."
compareList(list3, list4)
    
