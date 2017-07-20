#  File: Hailstone.py

#  Description: Given a range of numbers, this computes the integer in the range with the longest hailstone sequence cycle length

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/8/2016

#  Date Last Modified: 2/8/2016
def main():
	#prompt user for inputs
        start = eval(input("Enter starting number of the range: "))
        finish = eval(input("Enter ending number of the range: "))
        while (start < 0 or finish <0 or start > finish):
                start = eval(input("Enter starting number of the range: "))
                finish = eval(input("Enter ending number of the range: "))
        #intialize variables
        max_num = 0
        max_cycle_length = 0
        #write a loop that goes through all the numbers of the range
        counter = start
        while (counter <= finish):
            cycle_length = 0
            num_cycle = counter
            #nested loop that applies the condition.
            while (num_cycle!= 1):
                if (num_cycle % 2 == 1):
                    num_cycle = 3 * num_cycle + 1
                else:
                    num_cycle = num_cycle // 2
                cycle_length = cycle_length + 1
                        #checks if current cycle length is greater than the max cycle length
                if (cycle_length > max_cycle_length):
                    max_cycle_length = cycle_length
                    #assigns the number being computed to max number
                    max_num = counter
            counter = counter + 1  
                #print output
        if (start == 1 and finish == 1):
                max_cycle = 0
                max_num = 1
        print("The number " + str(max_num) + " has the longest cycle length of " + str(max_cycle_length) + ".")
	
main()
