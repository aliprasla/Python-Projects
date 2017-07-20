#  File: Intervals.py

#  Description: Finds the Non-Intersecting intervals 

#  Student Name: Ali Prasla

#  Student UT EID: anp2429  

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 4/17/2016

#  Date Last Modified: 4/19/2016
def main():
    #creates a 2d list of tuples
    in_file = open("intervals.txt","r")
    in_list = []
    num_lines = sum(1 for line in open('intervals.txt'))
    for i in range (num_lines):
        row = in_file.readline()
        row = row.strip()
        row = row.split()
        for j in range(len(row)):
            row[j] = int(row[j])
        in_list.append(tuple(row))
    print("Non-intersecting Intervals:")
    #sort the list of tuples
    in_list.sort()
    
    '''
    1. Compare current tuple to next tuple
    2. If collaspable, then collapse.
        - Compare collasped tuple to next in list
        - repeat
    3. Else - Place tuple in non-intersecting list
    '''
    sorte = []
    #create a list of collaspable intervals
    for i in range(len(in_list)-1):
        if (in_list[i][1] < in_list[i+1][0]):
            interval = in_list[0]
            print(interval)
            sorte.append(interval)
        elif (in_list[i][0] <= in_list[i+1][0]):
            if (in_list[i][1] >= in_list[i+1][1]):
                interval = in_list[i]
                in_list[i+1] = in_list[i]
            
            elif (in_list[i][1] <= in_list[i+1][1]):
                interval = in_list[i][0], in_list[i+1][1]
                in_list[i+1] = interval
        else:
            if (in_list[i][1] >= in_list[i+1][1]):
                interval = in_list[i]
                in_list[i+1] = in_list[i]
            
            elif (in_list[i][1] <= in_list[i+1][1]):
                interval = in_list[i][0], interval[i+1][1]
                in_list[i+1] = interval
    sorte.append(interval)
    #all collasped
    print(interval)
    print()
    #start extra credit -----
    dic = {}
    print("Non-intersecting Intervals in order of size:")
    #finds all ranges for the intervals and inputs them into dictionary dic
    for i in range(len(sorte)):
        key = sorte[i] 
        rang = sorte[i][1] - sorte[i][0]
        dic[key] = rang
    #sorts the dictionary by value while retaining the key
    dic_sorted = sorted(dic, key = dic.get)
    #loop to print sorted values
    for i in range(len(dic_sorted)):
        print(dic_sorted[i])
    print()
                
main()
