#  File: DNA.py

#  Description: Finds longest common sequence

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: March 25, 2016

#  Date Last Modified: March 25, 2016
import string

def substr (st,str2):
    wnd = len (st)
    maxchar = ""
    while (wnd > 0):
        start_idx = 0
        while ((start_idx + wnd) <= len(st)):
            piece = st[start_idx : start_idx + wnd]
            if (str2.find(piece) > 0 and len(piece) >= len(maxchar)):
                if (len(piece) == len(maxchar)):
                    print (piece, end = "\n"+ "        ")
                else:
                    maxchar = piece
            start_idx += 1
        wnd = wnd - 1
    if (maxchar == ""):
        print("No Common Sequence Found")
    else:
        print(maxchar)


def main():

    # read text file and set n to number to pairs of DNA to follow
    in_file = open("dna.txt", "r")
    line = ""
    
    n = int(in_file.readline())
    
    count = 0
    print("")
    print("Longest Common Sequences")
    print("")
    #reads a pair of line
    for i in range(0, n):
        # line 1
        line = in_file.readline()
        line = line.rstrip()
        line = line.upper()
        
        # line 2
        pair_line = in_file.readline()
        pair_line = pair_line.rstrip()
        pair_line = pair_line.upper()
        print("Pair " + str(i+1) + ": ", end = "")
        substr(pair_line,line)
        print("")

main()
