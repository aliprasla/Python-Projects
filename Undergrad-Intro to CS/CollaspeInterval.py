#  File: Intervals.py

#  Description: Finds the Non-Intersecting intervals 

#  Student Name: Ali Prasla

#  Student UT EID: anp2429  

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 4/17/2016

#  Date Last Modified: 4/20/2016
def createlist (a):
    #creates a list of all integers given an interval
    out = []
    for i in range (int(a[0]),int(a[1])+ 1):
        out.append(i)
    return out
def main():
    #creates a 2d list of intervals
    in_file = open("intervals.txt","r")
    mod = in_file
    in_list = []
    num_lines = sum(1 for line in open('intervals.txt'))
    for i in range (num_lines):
        row = mod.readline()
        row = row.strip()
        row = row.split()
        in_list.append(row)
    #finds all integers within each interval 
    out = []
    for i in range (len(in_list)):
        out.append(createlist(in_list[i]))
    print(out)
    #determine if each interval is overlapping
    for i in range(len(out)):
        compare = out[i]
        for k in range(len(out[i])):
            current = out[i][k]
            #compare current int to each int in rest of intervals
            
            
    #create a list of collaspable intervals

                
main()
