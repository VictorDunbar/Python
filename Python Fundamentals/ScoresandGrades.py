# Create a list that prints grades based on the number values//

import random
random_num = random.randint(1,100)

def ScoresGrades(score):
    
    if score < 60:
        print ("Score: "+ str(score) + "; Your grade is an F, chump!")
    elif score in range(60,69):
        print ("Score: "+ str(score) + "; Your grade is a D. Need some work.")
    elif score in range(70,79):
        print ("Score: "+ str(score) + "; Your grade is a C. Getting warmer..")
    elif score in range(80,89):
        print ("Score: "+ str(score) + "; Your grade is a B. Alright, alright, alright!")
    elif score in range(90,100):
        print ("Score: "+ str(score) + "; Your grade is an A. Good job, CHUMP!")


ScoresGrades(random_num)
