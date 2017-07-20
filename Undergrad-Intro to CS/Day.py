#  File: Day.py

#  Description: Finds the day of the week using Zeller's congruence

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 2/3/2016

#  Date Last Modified: 2/4/2016

def main ():

	#User enters inputs
        year = eval(input("Enter year: "))
        #error checking for year
        while ((year < 1900) or (year > 2100)):
                year = eval(input("Enter year: "))
        #user enters month
        month = eval (input("Enter month: "))
        #error checking for month
        while ((month < 1) or (month > 12)):
                month = eval (input("Enter month: "))
        day = eval (input("Enter day: "))
        # error checking for days
        num_days = 0        
        if ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
                num_days = 31
        elif ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
                num_days = 30
        elif ((month == 2)):
                num_days = 28
        #check leap year
        is_leap = (year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0))
        if (is_leap):
                num_days = 29
        while ((day < 1) or (day > num_days)):
                day = eval (input("Enter day: "))
        #convert from Gregorian month to month starting in January
        if ((month == 1) or (month == 2)):
                month = month + 10
                
        else:
                month = month - 2
        a = month
        #assign day
        b = day
        #seperate last two digits of year
        c = year
        if (year < 2000):
               c = c - 1900
        
        else:
                c = c - 2000
        #adjust c for year starting in march
        if ((month == 11) or (month == 12)):
                c = c - 1
        #finds the century
        d = year //100
        #apply Zeller's algorithm
        w = (13 * a - 1 ) // 5 

        x = c // 4 

        y = d // 4 

        z = w + x + y + b + c - 2 * d 

        r = z % 7 

        r = (r + 7) % 7
        #adjust for year 1900
        if (((month == 11) or (month == 12)) and year == 1900):
                r = r + 1
        #print day of week
        if (r == 0):
                print ()
                print ("The day is Sunday.")
        if (r == 1):
                print ()
                print ("The day is Monday.")
        if (r == 2):
                print ()
                print ("The day is Tuesday.")
        if (r == 3):
                print ()
                print ("The day is Wednesday.")
        if (r == 4):
                print ()
                print ("The day is Thursday.")
        if (r == 5):
                print()
                print("The day is Friday.")
        if (r == 6):
                print ()
                print ("The day is Saturday.")
        
               
main()
