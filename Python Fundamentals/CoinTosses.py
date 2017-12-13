#  Write a function that simulates tossing a coin 5,000 times. Your function should print how many times the head/tail appears.//
# x = .23945593
# y = .798839238
# x_rounded = round(x)
#  # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up to 1

import random

def coinToss():
    headsCount = 0;
    tailsCount = 0;
    tossCount = 0;

    for x in range(1, 5001):
        toss = round(random.random())
        if toss == 0:
            headsCount += 1
            tossCount += 1
            print "Attempt #" , tossCount , ": Throwing a coin... It's a head! ... Got" , headsCount , " head(s) so far and " , tailsCount , " tail(s) so far"
        else:
            tailsCount += 1
            tossCount += 1
            print "Attempt #" , tossCount , ": Throwing a coin... It's a tail! ... Got" , tailsCount , " tail(s) so far and " , headsCount , " head(s) so far"
coinToss()