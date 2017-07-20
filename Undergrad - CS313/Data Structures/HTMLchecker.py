#  File: HTMLchecker.py
#  Description: checks an html file to see if its tags are valid
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 10/3/2016
#  Date Last Modified: 10/7/2016
VALIDTAGS = []
class Stack (object):
   def __init__(self):
      self.items = [ ]
   def isEmpty (self):
      return self.items == [ ]
   def push (self, item):
      self.items.append (item)
   def pop (self):
      return self.items.pop ()
   def peek (self):
      return self.items [len(self.items)-1]
   def size (self):
      return len(self.items)
def getTag(string,search):
   begin_tag = False
   st = ''
   for i in range(search,len(string)):
      if string[i] == '<' and not(begin_tag):
         begin_tag = True
         continue
      if string[i] == '>':
         return st, (i+1)
      if begin_tag:
         st += string[i]
def getTagList(file):
  #returns list of tags
  List = []
  for line in file:
     List.append(line)
  checked_str = ''
  for i in range(len(List)):
     checked_str += List[i]
  print(checked_str)
  tagList = []
  end = 0
  #List is just all characters in the file. checked_str is just all the items in list appended to a string
  for i in range(len(checked_str)):
     try:
        tag, end = getTag(checked_str, end)
        tagList.append(tag)
     except TypeError:
        break
  print("The list of tags is :" + str(tagList))
  return tagList
def createStack(tagList):
  s = Stack()
  for item in range(len(tagList)):
    s.push(tagList[item])
  return s
def checkTags(s):
  #pull out of stack until you find a pair
   b = Stack()
   exceptions = ['br','meta','hr']
   while s.size()> 0:
     peeks = s.peek()
     peekb = ''
     if b.size() > 0:
        peekb = b.peek()
     print("Tag " + str(peeks) + ' pushed: ', end = '')
     #error check - if closing tag and if mismatch
     if peekb == '':
        pass
     elif (peekb[1::] != peeks) and  (peekb[0] != '/') and not(peeks in exceptions or exceptions[1] in peeks):
        print('\nError:  tag is ' + peekb + ' but top of stack is ' +peeks )
        return
     b.push(s.pop())
     validtagchecker = b.peek()
     print('Stack is now ' + str(b.items))
     if b.peek() in exceptions or (exceptions[1] in b.peek()):
        excep = b.peek()
        b.pop()
        print('Tag '+ excep + ' does not need to match. Stack is still ' + str(b.items))
     try:
        if peekb[1::] == peeks:
           print('Tag ' + str(b.peek()) + ' matches top of stack: Stack is now ', end = '')
           b.pop()
           b.pop()
           print(b.items)
     except UnboundLocalError:
        pass
     if not(validtagchecker in VALIDTAGS):
        VALIDTAGS.append(validtagchecker)
        print("New tag " + validtagchecker + " found and added to the list of valid tags")
   print()
   print()
   if b.size() == 0:
     print('Processing complete. No mismatches found.')
   else:
     print('Processing complete. Unmatched tags remain on stack:  ' + str(b.items))
def main():
  file = open('htmlfile.txt','r')
  a, b = getTag('<html>',0)
  tagList = getTagList(file)
  s = createStack(tagList)
  checkTags(s)
 
      
      
main()
