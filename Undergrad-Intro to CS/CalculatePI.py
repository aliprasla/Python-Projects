
#  File: CalculatePI

#  Description: Program to calculate Pi

#  Student Name: Ali Prasla	

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/29/2016

#  Date Last Modified: 2/29/2016
import math
import random
def computePI (numThrows):
    count = 0
    num = numThrows
    while (num >= 0):
        xPos = random.uniform(-1.0,1.0)
        yPos = random.uniform(-1.0,1.0)
        distance_from_center = math.hypot(xPos, yPos)
        num = num - 1
        if (distance_from_center < 1):
            count += 1
        
    calculated_PI = (count / numThrows)*4
    return calculated_PI
def main():

    num1 = computePI (100)
    difference1 = num1 - math.pi
    num1 = format(num1, '.6f')
    difference1 = eval(format(difference1,'.6f'))
    if (difference1 > 0):
        difference1 = "+" + str(difference1)
    print("Computation of PI using Random Numbers")
    print("")
    print ('num = 100'.ljust(17),'Calculated PI = {}'.ljust(20).format (num1), 'Difference = {}'.ljust(0).format (difference1))
    num2 = computePI (1000)
    difference2 = num2 - math.pi
    num2 = format(num2, '.6f')
    difference2 = eval(format(difference2,'.6f'))
    if (difference2 > 0):
        difference2 = "+" + str(difference2)
    print ('num = 1000'.ljust(17),'Calculated PI = {}'.ljust(20).format (num2), 'Difference = {}'.ljust(0).format (difference2))


    num3 = computePI (10000)
    difference3 = num3 - math.pi
    num3 = format(num3, '.6f')
    difference3 = eval(format(difference3,'.6f'))
    if (difference3 > 0):
        difference3 = "+" + str(difference3)
    print ('num = 10000'.ljust(17),'Calculated PI = {}'.ljust(20).format (num3), 'Difference = {}'.ljust(0).format (difference3))
    num4 = computePI (100000)
    difference4 = num4 - math.pi
    difference4 = eval(format(difference4,'.6f'))
    num4 = format(num4, '.6f')
    if (difference4 > 0):
        difference4 = "+" + str(difference4)
    print ('num = 100000'.ljust(17),'Calculated PI = {}'.ljust(20).format (num4), 'Difference = {}'.ljust(0).format (difference4))

    num5 = computePI (1000000)
    difference5 = num5 - math.pi
    difference5 = eval(format(difference5,'.6f'))
    num5 = format(num5, '.6f')
    if (difference5 > 0):
        difference5 = "+" + str(difference5)
    print ('num = 1000000'.ljust(17),'Calculated PI = {}'.ljust(20).format (num5), 'Difference = {}'.ljust(0).format (difference5))

    num6 = computePI (10000000)
    difference6 = num6 - math.pi
    difference6 = eval(format(difference6,'.6f'))
    num6 = format(num6, '.6f')
    if (difference6 > 0):
        difference6 = "+" + str(difference6)
    print ('num = 10000000'.ljust(17),'Calculated PI = {}'.ljust(20).format (num6), 'Difference = {}'.ljust(0).format (difference6))
main()
