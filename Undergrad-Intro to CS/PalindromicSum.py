#  File: PalindromicSum.py

#  Description: Finds the max cycle length of a Palindromic sum

#  Student Name: Ali Prasla

#  Student UT EID: anp2429  

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/17/2016

#  Date Last Modified: 2/18/2016
def rev_num (a):
    #reverses the digits of a number
    num_ = 0
    while (a > 0):
            num_ = (10*num_) + a%10
            a = a // 10
    return num_
def is_palindromic (b):
    #tests if n is a palandrome
    if (rev_num(b) == b):
        return True
    else:
        return False
def main ():
    #prompts user for inputs
    start = eval(input("Enter starting number of the range: "))
    finish = eval(input("Enter ending number of the range: "))
    if (start < 0 or finish < 0):
        start = eval(input("Enter starting number of the range: "))
        finish = eval(input("Enter ending number of the range: "))
    #intializes variables
    max_cycle_length = 0
    max_num = 0
    num = start
    #starts calculations
    while (num <= finish):
        cycle_length = 0
        sum_ = num
        #nested while determines each num's cycle length
        while (is_palindromic(sum_) == False):
            sum_ = sum_+ rev_num(sum_)
            cycle_length += 1
        #inputs largest num that has the max_length number of the series
        if (cycle_length >= max_cycle_length):
            max_cycle_length = cycle_length
            max_num = num
        num += 1
    print ("The number " + str(max_num) + " has the longest cycle length of " + str(max_cycle_length) + ".")        
main()
