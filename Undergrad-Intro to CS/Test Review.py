#memorize these-
def selection_sort (a):
    #go through list a
    for i in range (len(a) - 1):
        min_n = a[i]
        min_idx = i
        for j in range(i + 1, len(a)):
            if (a[j] < min_n):
                min_n = a[j]
                min_idx = j
        a[min_idx] = a[i]
        a[i] = min_n
    return a
def bin_search (a , x):
    lo = 0
    hi = len(a) - 1
    while (lo <= hi):
        mid = (lo + hi)//2
        if (x > a[mid]):
            low = mid + 1
        elif (x < a[mid]):
            hi = mid - 1
        else:
            return mid
    return -1
#sequential search
def seq_search (a,x):
    for i in range (len(a)-1):
        if (a[i] == x):
            return i
    return -1

def seq_mod(a,x):
    low = find(a,x)
    hi = rfind(a,x)
    #returns span
    return hi -low
    



#finish 
def pattern1 (until):
    end = 1
    while (end <= until):
        n = 1
        while(n <= end):
            print (n, end = "")
            n += 1
        end += 1
        print("")
        while( n >= end):
            print(n, end = "")
            n -= 1
    n = 1
#completed
def compress(a):
    b = a.replace(" ", "")
    c = b.replace("\n", "")
    return c
def replace_2015 (a):
    b = a.replace("2015", "2016")
    return b

#not yet
def printall(x,a):
    #for every time x string is found in a, print string and string indx
    while(counter <= num):
        previous = 0
        initial = find(x,a)
        print("Location: " + (initial+previous) + "String: " + x)
        #a = [initial : len(a) - 1]
        previous = initial
        counter += 1
#completed
def higher_average(a,b):
    aver_a = sum(a)/len(a)
    aver_b = sum(b)/len(b)
    if (aver_a > aver_b):
        return a
    if (aver_b > aver_a):
        return b
#completed
def high_range (a,b):
    sort_a = selection_sort(a)
    sort_b = selection_sort(b)
    range_a = a[len(a)-1] - a[0]
    range_b = b[len(b) - 1] - b[0]
    if (range_a > range_b):
        return a
    else:
        return b
def no_vowels(a):
    b = a.replace("a","")
    c = b.replace("e","")
    d = c.replace("i","")
    e = d.replace("o","")
    f = e.replace("u","")
    return f

def str_rotate (a,numrotations):
    for i in range (numrotations):
        end = a[-1]
        a = a[:-1]
        a = end + a
    return a
#memorize - worked.
def ispalindrome(a):
    return a  == a[::-1]

def ispalindromedig(a):
    return str(a) == str(a)[:: -1]
def is_sublist (a,b):
    length = 0
    for i in range (len(b)- 1):
        if (b[i] == a[0]):
            for k in range (len(a)):
                if (a[k] == b[i+k]):
                    length += 1

    if (length == len(a)+ 1):
        return True
    else:
        return False

def main():
   a ="hello"
   out = ""
   for i in range(len(a)):
       out = out + a[i] + a[i]
   print(out)
main()
