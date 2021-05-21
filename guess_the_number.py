import random

def guess(x):
    random_number =random.randint(1,x)
    guess=0
    count=0
    while guess != random_number:
        user = int(input("choose a number from 1 to {} :".format(x)))
        if user <random_number:
            print("sorry guess again too low")
            count+=1
        elif user>random_number:
            print("sorry guess again too high")
            count+=1
        elif user == random_number:
            print("yay!, you guess the right number")
            print("you guess the correct number in {} counts".format(count))
            break



guess(10)
