#  File: GuessingGame.py

#  Description: Program that guesses user's number

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 4/11/2016

#  Date Last Modified: 4/11/2016


def main():
    print ("Guessing Game")
    print ("")
    print("Think of a number between 1 and 100 inclusive. \nAnd I will guess what it is in 7 tries or less")
    print("")
    #asks users to play
    ready = input("Are you ready? (y/n): ")
    #error checking
    if (ready != 'y' and ready != 'n'):
        while ((ready != "y") or (ready != "n")):
            ready = input("Are you ready? (y/n): ")
            if (ready == "y"):
                print()
                break
    if (ready == "n"):
        print ("Bye")
        exit()
    print()
    lo = 1
    hi = 100
    guessNum = 1
    guessCheck = -1
    while (guessNum <= 7):
        mid = (lo + hi)//2
        print ("Guess " + str(guessNum) + " : The number you thought was " + str(mid))
        guessCheck = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
        if (guessCheck != -1 and guessCheck != 0 and guessCheck != 1):
            while (guessCheck != -1 and guessCheck != 0 and guessCheck != 1):
                guessCheck = eval(input("Enter 1 if my guess was high, -1 if low, and 0 if correct: "))
        if (guessCheck == 1):
            hi = mid - 1
            print()
        elif (guessCheck == -1):
            lo = mid + 1
            print()
        elif (guessCheck == 0):
            break
        guessNum += 1

    if (guessCheck == 0):
        print("")
        print("Thank you playing the Guessing Game")
    else:
        print ("Either you guessed a number out of range or you had incorrect entry")

main()
