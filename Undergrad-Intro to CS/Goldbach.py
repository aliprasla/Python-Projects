#  File: Goldbach.py

#  Description: Program to calculate Euler's corollary to Goldbach's thingy in a given range

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/26/2016

#  Date Last Modified: 2/26/2016


#function returns if a number is prime
def is_prime(x):
    y = 2
    if x < 2:
        return False
    while y < x:
        if x % y == 0 :
            return False
        y += 1
    return True

def main():
    #prompt user for inputs
    low = eval(input("Enter the lower limit: "))
    high =eval(input("Enter the upper limit: "))
    #error checking on inputs
    while (low < 4):
        low = eval(input("Enter the lower limit: "))
        high = eval(input("Enter the upper limit: "))
    while (low % 2 != 0 and high % 2 != 0):
        low = eval(input("Enter the lower limit: "))
        high = eval(input("Enter the upper limit: "))
    while (low > high):
        low = eval(input("Enter the lower limit: "))
        high = eval(input("Enter the upper limit: "))
    n = low
    #find Goldbach
    while (n <= high):
        count = n
        cycle = 0
        print (n, end = " ")
        while (count >= n/2):
            if (is_prime(count) and is_prime(cycle)):
                print("= " + str(count) + " + " + str(cycle), end = " ")       
            count -= 1
            cycle += 1
        n += 2
        print("")
main()
