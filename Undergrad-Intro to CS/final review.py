#memorize these functions---------------------
import random
def charfreq(st):
  dic = {}
  for i in range(len(st)):
    if (st[i] == " "):
      st.replace(" ","")
    elif (st[i] in dic.keys()):
      dic[st[i]] += 1
    else:
      dic[st[i]] = 1
  return dic
def flipped (dic):
  out = {}
  for key,value in dic.items():
    out[value] = key
  return out
def common (a,b):
  out = list(set(a) & set(b))
  return out
def sum2dlist(a,b):
  out = []
  sublist = []
  for i in range(len(a)):
    for k in range(len(a[i])):
      sublist.append(a[i][k]+b[i][k])
    out.append(sublist)
    sublist = []
  return out
def is_anagram (a,b):
  dictA ={}
  dictB = {}
  for i in range(len(a)):
    if (a[i] in dictA.keys()):
      dictA[a[i]] += 1
    else:
      dictA[a[i]] = 1
  for i in range(len(b)):
    if (b[i] in dictB.keys()):
      dictB[b[i]] += 1
    else:
      dictB[b[i]] = 1
  if (set(dictA.values()) == set(dictB.values()) and set(dictA.keys()) == set(dictB.keys())):
    return True
  else:
    return False
  
#end memorization
def randomgrid(columns):
  out = []
  for i in range (columns):
    a = random.uniform(1,100)
    b = random.uniform(1,100)
    c = random.uniform(1,100)
    out.append([a,b,c])
  return out
def sumlists(a,b):
  out = []
  for i in range(len(a)):
    out.append(a[i] + b[i])
  return out

def main():

  in_file = open("passwd.txt","r")
  pairs = {}
  for line in in_file:
    line = line.strip()
    for i in range(len(line)):
      if (line[i] == ":"):
        username = line[:i]
        password = line[i+1:]
    pairs[username] = password
  user = input("Enter a username : ")
  passw = input("password : ")
  print(pairs)
  if (user in pairs.keys()):
    if (pairs[user] == passw):
      print("tru")
    else:
      print('fa')
  else:
    print('fa')
  
  '''
  a = ['a', 'b','c','d','ef','g']
  print(shuffle(a))
  '''
main()
