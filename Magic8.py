# Import the modules
import sys
import random

ans = True

while ans:
    question = raw_input("Ask a question:")

    answers = random.randint(1,9)

    if question == "":
        sys.exit()

    elif answers == 1:
        print "It is certain"

    elif answers == 2:
        print "I hope for your life its ok"

    elif answers == 3:
        print "YES"

    elif answers == 4:
        print "Ask again"

    elif answers == 5:
        print "Concentrate and ask again"

    elif answers == 6:
        print "Don't be stupid"

    elif answers == 7:
        print "NO"

    elif answers == 8:
        print "My sources say no"

    elif answers == 9:
        print "Get a life"
