#  File: LinkedLists.py
#  Description: Plays Hot Potatoe
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 10/21/2016
#  Date Last Modified: 10/23/2016

#create a sentinel node - skip when counting
#define nodes
class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            
   def getData (self):
      return self.data            
   def getNext (self):
      return self.next            
   def setData (self, newData):
      self.data = newData         
   def setNext (self,newNext):
      self.next = newNext
class CircularList(object):
   def __init__ (self): 
      # the circular list constructor method.
      self.head = Node(None)
      self.head.setNext(self.head)
   def add (self,item):
      
      temp = Node(item)
      next_ = self.head.getNext()
      self.head.setNext(temp)
      temp.setNext(next_)
   def isEmpty (self):
      # Return True if the cicrcular list is empty.
      return self.head.getNext() == self.head
   def __str__(self):
      out = ''
      if self.isEmpty():
         return out
      current = self.head.getNext()
      i = 0
      while current != self.head:
         out = out + str(current.getData()) + ' '
         current = current.getNext()
         if i % 10 == 9:
            out = out + '\n'
         i += 1
      return out
   def onlyOneNode(self):
      return self.head.getNext().getNext() == self.head
   def remove(self,current,previous):
      previous.setNext(current.getNext())
      return previous.getNext()
def main():
   file = open('HotPotatoData.txt','r')
   for line in file:
      try:
         count = int(line[0])
         #Game starts are identified.
      except ValueError:
         continue
      #imports the number of people in the list and the number of iterations
      start = line[:-1]
      num_people = ''
      counter = 0
      while start[counter] != ' ':
         num_people = num_people + start[counter]
         counter += 1
      iterations = ''
      counter += 1
      while line[counter] != '\n':
         iterations = iterations + line[counter]
         counter += 1
      num_people = int(num_people)
      iterations = int(iterations)
      circle = CircularList()
      #imports list of people
      for i in range(num_people):
         circle.add(next(file).replace('\n',''))
      print('-------------------------------------------------------- NEW GAME --------------------------------------------------------')
      print('Original Set of Players: ')
      print(circle)
      counter = 1
      current = circle.head
      previous = None
      while not circle.onlyOneNode():
         print()
         print('Iteration Number ', str(counter), ': ')
         i = 1
         while i < iterations + 1:
            previous = current
            current = current.getNext()
            if current.getData() is None:
               i = i - 1
            i += 1
         print(current.getData() + ' deleted')
         circle.remove(current,previous)
         if not circle.onlyOneNode():
            print('New Set of Players : ')
         else:
            print('The sole survivor is : ',end = '')
         print (circle)
         print()
         counter += 1
      #num_people is the number of people in the hot potato game
      #current line is a placeholder
      current_line = line
main()
