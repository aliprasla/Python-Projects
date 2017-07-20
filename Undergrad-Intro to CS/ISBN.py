#  File: ISBN.py

#  Description: Determines Validity of Isbn numbers

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: March 31, 2016

#  Date Last Modified: April 2, 2016
def is_valid(str_a):
    #checks if last digit is digit or x or X
    if (not(str_a[-1].isdigit or str_a[-1] == 'X' or str_a[-1] == 'x')):
        return "invalid"     
    #normalize- remove hyphens and upper case the x's 
    partial = str_a.replace("-","")
    partial = partial.upper()            
    #partial sum check - creates two lists s1 and s2. s1 is the partial sums of the isbn digits. s2 is the partial sums of s1.
    s1 = []
    s2 = []
    sum = 0
    for i in range (len(partial)):
        if (partial[i] == 'X'):
            sum = sum + 10
        else:
            sum = sum + eval(partial[i])
        s1.append(sum)
    sum1 = 0
    for j in range (len(s1)):
        sum1 = sum1 + s1[j]
        s2.append(sum1)
    #check remove x's. see if only digits are left
    partial = partial.replace('x', '')
    partial = partial.replace ('X', '')
    
    if (not partial.isdigit()):
        return "invalid"
    #checks last condition of partial sums
    if (s2[-1] % 11 == 0):
        return "valid"
    else:
        return "invalid"
    #end partial summing


def main():    
    
    in_file = open("isbn.txt", "r")
    #figure out num lines
    with in_file as f:
        num_lines = sum(1 for _ in f)
    #reopen files
    in_file = open("isbn.txt","r")
    outfile = open("isbnOut.txt","w")

    #still need to figure out formatting
    for count in range (num_lines):
        line = in_file.readline()
        line = line.rstrip()
        #adjust following line to complete formatting issues.
        output = line + " %s"%is_valid(line).ljust(8)
        outfile.write("{} \n".format(output))
    outfile.close()
    in_file.close()
main()

