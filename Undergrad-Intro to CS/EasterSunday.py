#  File: EasterSunday.py

#  Description: Program to calculate date ofEaster Sunday

#  Student Name: Ali Prasla	

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 1/31/2016

#  Date Last Modified: 2/1/2016

def main ():
#prompt user for year
        y = eval(input("Enter a year: "))
#apply gauss's algorithm
        a = y%19
        b = y//100
        c = y%100
        d = b//4
        e = b%4
        g = (8*b+13)//25
        h = (19*a+b-d-g+15)%30
        j = c//4
        k = c%4
        m = (a+11*h)//319
        r = (2*e+2*j-k-h+m+32)%7
        n = (h-m+r+90)//25
        p = (h-m+r+n+19)%32
# print statements
        if (n == 3):
                print("In {} Easter Sunday is on {} March.".format(y,p))
        elif (n == 4):        
                print("In {} Easter Sunday is on {} April.".format(y,p))
        
main()
	
	
