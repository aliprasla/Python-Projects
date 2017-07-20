#  File: CreditCard.py

#  Description: Determines Validity of Credit Card numbers

#  Student Name: Ali Prasla

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: April 8, 2016

#  Date Last Modified: April 9, 2016
def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
def is_valid(cc_num):
    print("")
    if (len(str(cc_num))== 15 or len(str(cc_num)) == 16):
        pass
    else:
        print("Not a 15 or 16-digit number")
        return
    #------------------apply luhn's test-----------------------------------
    #convert int into list
    cc_str = str(cc_num)
    cc_list = []
    for i in range (len(cc_str)):
        cc_list.append(eval(cc_str[i]))
    #multiply all odd digits and sum their digits
    i = 0
    if len(cc_str) == 16:
        while (i <= len(cc_str)-1):
            cc_list[i] = 2*int(cc_str[i])
            cc_list[i] = sum_digits(cc_list[i])
            i += 2
    else:
        while (i <= len(cc_str)-2):
            cc_list[i+1] = 2*int(cc_str[i+1])
            cc_list[i+1] = sum_digits(cc_list[i+1])
            i += 2
    sum_dig = 0
    #sum all
    for j in range(len(cc_list)):
        sum_dig = sum_dig + cc_list[j]
    if (sum_dig % 10 == 0):
        return True
    else:
        print("Invalid credit card number")
        return False
    
def cc_type(cc_num):
    cc_type = ""
    cc_str = str(cc_num)
    if (cc_str[0] == "3" and (cc_str[1] == '4' or cc_str[1] == '7')):
        return "Valid American Express credit card number"
    if (cc_str[0:4] == '6011' or cc_str[0:3] == '644' or cc_str[0:2] == '65'):
        return "Valid Discover credit card number"
    if (cc_str[0] == "4"):
        return "Valid Visa credit card number"
    #test mastercard
    if (cc_str[0:2] == "50" or cc_str[0:2] == "51" or cc_str[0:2] == "52" or cc_str[0:2] == "53" or cc_str[0:2] == "54" or cc_str[0:2] == "55"):
        return "Valid MasterCard credit card number"
    else:
        return "Valid credit card number"
def main():
    creditCard = eval(input('Enter 15 or 16-digit credit card number: '))
    if (is_valid(creditCard)):
        print(cc_type(creditCard))

main()
