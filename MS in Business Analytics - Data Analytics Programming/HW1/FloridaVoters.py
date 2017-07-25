# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 11:17:02 2017

@author: Ali Prasla
"""
import re
def byDem(x):
    return x[2]
def printList(x):
    print x[0] + " " + str(x[1]) + " " + str(x[2])
def main():
    fl = open('FloridaVoters.html')
    allTds = []
    for line in fl:
        if(line.find("td") > 0):
            line = re.findall("<td>(.*?)</td>",line)
            allTds.append(line)
    allTds = allTds[1:]
    #Normalize into 2d list
    finalDataSet = []
    currentList = []
    for index,item in enumerate(allTds):
      #reset currentList
      item = item[0].replace(",","")
      try:
          item = int(item)
      except:
          k = ""
      if(index % 6 == 0 and index != 0):
          finalDataSet.append(currentList)
          currentList = []    
      currentList.append(item)
    #append total row:
    finalDataSet.append(currentList)
    #final DataSet is a 2d list with a matrix
    sortedList = sorted(finalDataSet,key = byDem)
    for item in sortedList:
        printList(item)
main()
