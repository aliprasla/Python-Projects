#  File: Benford.py

#  Description: Frequency table of first digit of 2009 Census Data

#  Student Name: Ali Prasla	

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 4/20/2016

#  Date Last Modified: 4/20/2016
def main():
  # create an empty dictionary
  pop_freq = {}

  # initialize the dictionary
  pop_freq ['1'] = 0
  # fill the rest
  for i in range(2,10):
      pop_freq [str(i)] = 0
  # open file for reading
  in_file = open ("./Census_2009.txt", "r")
  # read the header and ignore
  header = in_file.readline()
  
  # read subsequent lines
  total_entries = 0
  for line in in_file:
    line = line.strip()
    pop_data = line.split()
    # get the last element that is the population number
    pop_num = pop_data[-1]
    # make entries in the dictionary
    # find first digit of pop_num
    first_dig = pop_num[0]
    #make actual entries into dictionary
    key = first_dig
    pop_freq[key] += 1
    total_entries += 1
  # close the file
  in_file.close()

  # write out the result
  items = list(pop_freq.items())
  #sort by first index 
  for i in range(len(items)):
      #change to from tuple to list
      items[i] = list(items[i])
      #change to int
      items[i][0] = int(items[i][0])
  #sort
  items.sort()
  #print results
  print("Digit" + " " + " Count" + "    " + "%")
  for i in range(len(items)):
      if (len(str(items[i][1]))== 3):
        print(str(items[i][0]) + "      {}".ljust(7).format(str(items[i][1])) + "      {}".ljust(7).format(str(round((items[i][1] / total_entries)*100,1))))
      else:
        print(str(items[i][0]) + "      {}".ljust(7).format(str(items[i][1])) + "     {}".ljust(7).format(str(round((items[i][1] / total_entries)*100,1))))
main()
