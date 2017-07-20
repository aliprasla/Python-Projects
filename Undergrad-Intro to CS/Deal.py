# File: Deal.py

# Description: Predicts dominant strategy for Let's make a deal
# Student Name: Ali Prasla

# Student UT EID: anp2429

# Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 3/4/2016

#  Date Last Modified: 3/4/2016
import random
def main():
    numGame = eval(input("Enter number of times you want to play: "))
    print ("")
    print ("  Prize      Guess       View    New Guess ")
    count = 0
    numWins = 0
    while (count <= numGame):
        prize = random.choice ('123')
        guess = random.choice ('123')
        view = random.choice ('123')
        while (view == guess or view == prize):
            view = random.choice('123')
        newGuess = random.choice('123')
        while (newGuess == guess or newGuess==view):
            newGuess =random.choice('123')
        print ("    {}          {}          {}          {}     ".format(prize,guess,view,newGuess))
        if (newGuess == prize):
            numWins += 1
        count += 1
    prob_win = numWins / numGame
    prob_l = 1 - prob_win
    print ("Probability of winning if you switch = %3.2f" % prob_win)
    print ("Probability of winning if you do not switch = %3.2f" % prob_l)
main()
