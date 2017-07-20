#  File: FibbonaciBase.py

#  Description: Converts any number into binary with the fibbonaci sequence as its base

#  Student Name: Ali Prasla	

#  Student UT EID: anp2429

#  Course Name: CS 303E

#  Unique Number: 50865

#  Date Created: 4/29/2016

#  Date Last Modified: 4/29/2016

#writes fibonacci sequence
def seq(n):
  a = 0
  b = 1
  c = 0
  seq = [a,b]
  for i in range (n):
    c =  a + b
    seq.append(c)
    a = b
    b = c
  return seq

#flips fibonacci sequence
def flipseq(seq):
  r = list(reversed(seq))
  return r
def main():
  num = eval(input("Enter a number: "))
  #figure out largest bit you need
  count= 0
  while(flipseq(seq(count))[0] < num):
    if (flipseq(seq(count))[0] > num):
        continue
    else:
        count += 1
  lenfib = count
  fib = flipseq(seq(lenfib))
  #delete 0 and 1 from list
  fib = fib[:-2]
  #fib is the sequence you are going to use to construct the binary base fib
  #construct output list
  output = []
  if (num < fib[0]):
    del fib[0]
  for j in range (len(fib)):
    output.append(0)
  sum_ = 0
  for i in range(len(fib)):
    if(fib[i] + sum_ <= num):
      sum_ = sum_ + fib[i]
      output[i] = 1
    elif (sum_ == num):
      break
    else:
      continue
  #convert from list to str
  out = ''
  for i in range(len(output)):
    out = out + str(output[i])
  print(str(num) + ' = ' + out + ' (fib)')
main()
