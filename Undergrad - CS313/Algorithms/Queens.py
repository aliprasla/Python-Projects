#  File: Queens.py
#  Description: Prints out solution of N-Queens problem
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 11/9/2016
#  Date Last Modified: 11/11/2016
class QueensProblem():
  def __init__(self,n):
    #board is a 1 d list with length n
    self.board = []
    self.which_sol = 1
    for i in range(n):
      # - 100 = dummy filler.
      self.board.append(-100)
  def __str__(self):
    out = ''
    for k in range(len(self.board)):
      #iterate through rows
      for i in range(len(self.board)):
        #iterate through columns
        if self.board[k] == i:
          #if there is a queen in this row,col
          out += 'Q '
        else:
          out += '* '
      out += '\n'
    return out
    
  def isValidPlace(self,row,col):
    for i in range(row):
      #check row - if there are two ints in self.board that equal each other then it returns false
      #this is the equivalent of 2 queens on the same row
      if self.board[i] == self.board[row]:
        return False
      #checks diagonals
      if (row - i == abs(self.board[row] - self.board[i])):
        return False
    return True
  def solve(self,n):
    #n is which queen you are on
    if n == len(self.board):
      #base case of recursion - ends
      return True
    else:
      for i in range(len(self.board)):
        #test
        self.board[n] = i
        fin = None
        if self.isValidPlace(n,0):
          #if that is a valid location
          #recurse
          fin = self.solve(n+1)
          #if there is a solution then end.
        if fin:
          #prints output
          print("Solution # " + str(self.which_sol))
          print(self)
          self.which_sol += 1
          #note - this doesn't end. this keeps recursing and iterating
    return False
def main():
  #asks user for input
  size = eval(input("Enter the size of the square board: "))
  while size <= 3:
    print("Invalid input.")
    size = eval(input("Enter the size of the square board: "))
  a = QueensProblem(size)
  print()
  #n = beginning- start at 0,0 in board
  a.solve(0)
main()
