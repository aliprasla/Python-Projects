#  File: Sorting.py
#  Description: Prints out a table of the calculation times of different sort algorithms
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 11/14/2016
#  Date Last Modified: 11/16/2016
import random
import time
import sys
sys.setrecursionlimit(10000)
#imported sort algorithms
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)
def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)
def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    return rightmark
def printHeader(whichList):
  #prints a header
  print("Input type =",whichList)
  print("                    avg time   avg time   avg time")
  print("   Sort function     (n=10)    (n=100)    (n=1000)")
  print("-----------------------------------------------------")
def run(which_type,num_trials,which_method):
  #run is a generic function that can be iterated through.
  #which_type is what is the manipulation to the list
  #num_trials is an int 10, 100 or 1000  (length of list)
  #which_method selects which sort algorithm to use. 
  out = []
  for i in range (5):
    myList = [i for i in range(num_trials)]
    #which list manipulation
    if which_type == "Random":
        random.shuffle(myList)
    elif which_type == "Reverse":
        myList.reverse()
    elif which_type == "Almost Sorted":
        count = 0
        while count < (num_trials * .1):
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            #if you return the same index (especially for n = 10)
            while randomIndex1 == randomIndex2:
                randomIndex1 = random.randint(0,len(myList)-1)
                randomIndex2 = random.randint(0,len(myList)-1)
            temp = myList[randomIndex2]
            myList[randomIndex2] = myList[randomIndex1]
            myList[randomIndex1] = temp
            count += 1
    #which sort algorithm
    if which_method == "bubbleSort":
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
    elif which_method == "selectionSort":
        startTime = time.perf_counter()
        selectionSort(myList)
        endTime = time.perf_counter()
    elif which_method == "insertionSort":
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
    elif which_method == "shellSort":
        startTime = time.perf_counter()
        shellSort(myList)
        endTime = time.perf_counter()
    elif which_method == "mergeSort":
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
    elif which_method == "quickSort":
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
    elasped = endTime - startTime
    out.append(elasped)
  string = '%f' % (round(sum(out)/num_trials,6))
  #formatting and printing of this specific run situtation
  blank = ''
  num_spaces = len(which_method)
  while num_spaces < 16:
      blank += ' '
      num_spaces += 1
  if num_trials == 10:
    print(blank+ which_method + "    " + str(string),end = "")
  elif num_trials == 100:
    print("   " + str(string),end = "")
  else:
    print("   " + str(string))
def main():
  #manipulation types
  list_types = ["Random","Sorted","Reverse","Almost Sorted"]
  #sort algorithms
  sort_types = ["bubbleSort","selectionSort","insertionSort","shellSort","mergeSort","quickSort"]
  for item in list_types:
      printHeader(item)
      for algo in sort_types:
          run(item,10,algo)
          run(item,100,algo)
          run(item,1000,algo)
      print()
main()
