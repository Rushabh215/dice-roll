import random
min = 1
max = 6

roll_again = "yes"

while roll_again == "yes":
    print "Rolling the dice..."
    print "the values is .."
    print random.randint(min,max)
    print random.randint(min,max)

    roll_again = raw_input("Roll the dice again?")
