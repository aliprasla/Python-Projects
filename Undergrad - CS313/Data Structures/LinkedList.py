#  File: LinkedList.py
#  Description: creates abstract data type LinkedList and manipulates
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 10/17/2016
#  Date Last Modified: 10/19/2016
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

class LinkedList(object):
  def __init__(self):
     self.head = None
  def __str__(self):
     out = ''
     current = self.head
     for i in range(self.getLength()):
       out = out + str(current.getData()) + ' '
       if i % 10 == 9:
         out = out + '\n'
       current = current.getNext()
     return out 
  def addFirst(self,item):
     temp = Node(item)
     temp.setNext(self.head)
     self.head = temp
  def addLast(self,item):
     temp = Node(item)
     current = self.head
     previous = None
     while current != None:
       previous = current
       current = current.getNext()
     if previous == None:
       self.head = temp
     else:
       previous.setNext(temp)
  def getLength(self):
     current = self.head
     count = 0
     while current != None:
       count += 1
       current = current.getNext()
     return count
  def addInOrder(self,item):
     current = self.head
     previous = None
     stop = False
     while current != None and not stop:
       if current.getData() > item:
         stop = True
       else:
         previous = current
         current = current.getNext()
     temp = Node(item)
     if previous == None:
       temp.setNext(self.head)
       self.head = temp
     else:
       temp.setNext(current)
       previous.setNext(temp)
  def findUnordered(self,item):
     current = self.head
     found = False
     while current != None and not found:
       if current.getData() == item:
         found = True
       else:
         current = current.getNext()
     return found
  def findOrdered(self,item):
     current = self.head
     previous = None
     stop = False
     found = False
     while current != None and not stop and not found:
       if current.getData() > item:
         stop = True
       elif current.getData() == item:
         found = True
       else:
         previous = current
         current = current.getNext()
     return found
  def delete(self,item):
     if self.findUnordered(item):
        current = self.head
        previous = None
        found = False
        while not found:
           if current.getData() == item:
              found = True
           else:
              previous = current
              current = current.getNext()
        if previous == None:
           self.head = current.getNext()
        else:
           previous.setNext(current.getNext())
        return True
     else:
        return False
  def copyList(self):
     temp = LinkedList()
     current = self.head
     while current != None:
        temp.addLast(current.getData())
        current = current.getNext()
     return temp
  def reverseList(self):
     temp = LinkedList()
     current = self.head
     while current != None:
        temp.addFirst(current.getData())
        current = current.getNext()
     return temp
  def orderList (self):
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list
     temp = LinkedList()
     stored_self = LinkedList()
     current = self.head
     for i in range(self.getLength()):
        stored_self.addLast(current.getData())
        current = current.getNext()
     #return minimum of self and addLast to temp
     while stored_self.getLength() > 0:
        minimum = stored_self.head.getData()
        current = stored_self.head
        while current != None:
           if current.getData() < minimum:
              minimum = current.getData()
           else:
              current = current.getNext()
        stored_self.delete(minimum)
        temp.addLast(minimum)
     return temp
  def isOrdered(self):
     not_ordered = False
     if self.getLength() == 1:
        return True
     current = self.head.getNext()
     previous = self.head
     while current != None and not not_ordered:
           if current.getData() < previous.getData():
              not_ordered = True
           else:
              previous = current
              current = current.getNext()
     return not not_ordered
  def isEmpty(self):
     return self.getLength() == 0
  def isEqual(self,b):
     self_current = self.head
     b_current = b.head
     unequal = False
     if (self.getLength() != b.getLength()):
        return False
     while (self_current != None or b_current != None) and not unequal:
        if self_current.getData() != b_current.getData():
           unequal = True
        else:
           self_current = self_current.getNext()
           b_current = b_current.getNext()
     return not unequal
  def removeDuplicates(self):
     temp = LinkedList()
     current = self.head
     while current != None:
        if not temp.findUnordered(current.getData()):           
           temp.addLast(current.getData())
        current = current.getNext()
     return temp
  def mergeList(self,b):
    sorted_self = self.orderList()
    sorted_b = b.orderList()
    out = LinkedList()
    current_self = sorted_self.head
    current_b = sorted_b.head
    while (not sorted_self.isEmpty()) and (not sorted_b.isEmpty()):
       if (current_self.getData() <= current_b.getData()):
          out.addLast(current_self.getData())
          #drop current_self
          sorted_self.delete(current_self.getData())
          current_self = current_self.getNext()
       else:
          out.addLast(current_b.getData())
          sorted_b.delete(current_b.getData())
          current_b = current_b.getNext()
    while not sorted_self.isEmpty():
       out.addLast(current_self.getData())
       sorted_self.delete(current_self.getData())
       current_self = current_self.getNext()
    while not sorted_b.isEmpty():
       out.addLast(current_b.getData())
       sorted_b.delete(current_b.getData())
       current_b = current_b.getNext()
    return out
    # Return an ordered list whose elements consist of the 
    #    elements of two ordered lists combined.
   
def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)
main()
