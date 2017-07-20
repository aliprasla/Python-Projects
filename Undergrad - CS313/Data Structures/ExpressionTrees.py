#  File: ExpressionTrees.py
#  Description: Evaluates an expression using a binary tree
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 11/17/2016
#  Date Last Modified: 11/30/2016
class Stack (object):
   def __init__(self):
      self.items = [ ]
   def isEmpty (self):
      return self.items == []
   def push (self, item):
      self.items.append (item)
   def pop (self):
      return self.items.pop ()
   def peek (self):
      return self.items [len(self.items)-1]
   def size (self):
      return len(self.items)
   def __str__(self):
       return (str(self.items))
class BinaryTree (object):
    def __init__ (self,newVal = None):
        if newVal != None:
            self.data = newVal
        else:
            self.data = None
        self.left = None
        self.right = None
    def getRootVal(self):
        return self.data
    def setRootVal(self,newVal):
        self.data = newVal
    def getLeftChild(self):
        return self.left
    def getRightChild(self):
        return self.right
    def insertLeft(self,newVal):
       if self.left == None:
           self.left = BinaryTree(newVal)
       else:
           t = BinaryTree(newVal)
           t.left = self.left
           self.left = t
    def insertRight(self,newVal):
        if self.right == None:
             self.right = BinaryTree(newVal)
        else:
             t = BinaryTree(newVal)
             t.right = self.right
             self.right = t
    def createTree(self,stack):
        #pushStack is an easy way to traverse up
        pushStack = Stack()
        pushStack.push(self)
        current = self
        for i in range(stack.size()):
            item = stack.pop()
            if item == "(":
                current.insertLeft('')
                pushStack.push(current)
                current = current.getLeftChild()
            elif item == ")":
                #set current Node to parent
                current = pushStack.pop()
            elif item in ['+','-','*','/']:
                current.setRootVal(item)
                current.insertRight('')
                pushStack.push(current)
                current = current.getRightChild()
            else:
                #if num
                current.setRootVal(item)
                current = pushStack.pop()
                #set current Node to parent
    def evaluate(self,node):
          #recursively evaluate using order of operations
         if node.left != None or node.right != None:
            left_val = node.evaluate(node.getLeftChild())
            right_val = node.evaluate(node.getRightChild())
            return eval(str(left_val) + str(node.data) + str(right_val))
         else:
            return node.data
    def preFix(self,node):
       #because leaf nodes will have no children that's the end condition
      if node != None:
         print(str(node.data),end = ' ')
         node.preFix(node.getLeftChild())
         node.preFix(node.getRightChild())
    def postFix(self,node):
       if node != None:
          node.postFix(node.getLeftChild())
          node.postFix(node.getRightChild())
          print(str(node.data), end = ' ')
          
      
def main():
    #open file
    newFile = open('treedata.txt','r')
    input_data = []
    for line in newFile:
        splited = line.split(' ')
        temp = Stack()
        for i in reversed(splited):
            if i[-1:] == '\n':
                i = i[:-1]
            temp.push(i)
        run = BinaryTree()
        run.createTree(temp)
        val = run.evaluate(run)
        print()
        print('Infix Expression: ', line)
        print('   Value:   ',val)
        print('   Prefix:  ', end = '')
        run.preFix(run)
        print()
        print('   Postfix:  ', end = '')
        run.postFix(run)
        print()
        
    #clean up new line character
    
main()
