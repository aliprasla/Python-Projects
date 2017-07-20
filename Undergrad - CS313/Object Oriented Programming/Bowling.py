#  File: Bowling.py
#  Description: Reads a list of bowling scores
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429  
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 9/2/2016
#  Date Last Modified: 9/9/2016

#class Frame ():
class Game():
  f = ''
  f1 = ''
  def __init__(self,list_scores,which_game):
    score_values = {'X':10,'9':9,'8':8,'7':7,'6':6,'5':5,'4':4,'3':3,'2':2,'1':1,'-':0}
    #read through list_scores
    #initialize variables
    which_frame = 1
    which_throw = 1
    frame_scores = []
    point_counter = 0
    total_score = 0
    tenth = 0
    which_throw_list = []
    #loop through the game
    for i in range(len(list_scores[which_game])):
     #you need a point counter. and you need a frame counter
     current = list_scores[which_game][i]
     if (which_throw >= 3) or (point_counter >= 10):
       point_counter = 0
       which_frame += 1
       which_throw = 1
     which_throw_list.append(which_throw)
     if current == 'X' and which_frame < 10:
         #num of pins knocked over in the next 2
         point_counter = 10
         try:
           f = score_values[list_scores[which_game][i+1]]
           f2 = score_values [list_scores[which_game][i+2]]
         except KeyError:
           f = int(score_values[list_scores[which_game][i+1]])
           f2 = 10 - int(score_values[list_scores[which_game][i+1]])
         point_counter += f + f2
         which_throw += 1
     elif current == '/' and which_frame < 10:
       point_counter =  10 + score_values[list_scores[which_game][i+1]]
       which_throw += 1
     elif current == '-':
       which_throw += 1
     else:
       if which_frame == 10:
         if current == 'X':
           if list_scores[which_game][i + 2] == '/':
             point_counter = 10 + 10
           else:
             point_counter = 10 + score_values[list_scores[which_game][i + 1]]+ score_values[list_scores[which_game][i + 2]]
           total_score += point_counter
           frame_scores.append(total_score)
           break
         elif current.isdigit() and which_throw == 1:
            point_counter += score_values[current]
            which_throw += 1
            continue
         elif current.isdigit() and which_throw == 2:
            point_counter += score_values[current]
            total_score += point_counter
            frame_scores.append(total_score)
            which_throw += 1
            break
         elif current == '/' and which_throw == 2:
            point_counter = 10 + score_values[list_scores[which_game][i+1]]
            total_score += point_counter
            frame_scores.append(total_score)
            which_throw += 1
            break
       else:
          point_counter += score_values[current]
          which_throw += 1
     if (which_throw == 3 or point_counter >= 10):
       total_score += point_counter
       frame_scores.append(total_score)
    #begin printing/formatting
    which_frame = 1
    which_throw = 1
    print('|', end = '')
    list_len = len(list_scores[which_game])
    for j in range(list_len):
      current = list_scores[which_game][j]
      if which_frame == 10:
        try:
          print(current + ' '+list_scores[which_game][j+1] +' '+ list_scores[which_game][j+2] + '|', end = '')
        except IndexError:
          print(current + ' '+ list_scores[which_game][j+1]+ '  |', end = '')
        break
      if current == 'X':
        print(current + '  |',end = '')
        point_counter = 0
        which_throw = 1
        which_frame += 1
      elif current == '-' and which_throw == 1:
        which_throw += 1
        print(current, end = ' ')
      elif current == '-' and which_throw == 2:
        print(current, end = '|')
        which_throw = 1
        which_frame += 1
      elif current.isdigit() and which_throw == 1:
        print (current, end = ' ')
        which_throw += 1
      elif (current.isdigit() and which_throw == 2):
        print(current, end = '|')
        which_frame += 1
        which_throw = 1
      elif current == '/' and which_throw == 2:
        print(current, end = '|')
        which_frame += 1
        which_throw = 1
      else:
        print(current, end = ' |')
        which_frame += 1
        which_throw = 1
    print ()
    print('|', end = '')
    which_frame = 1
    if frame_scores[-1] == 0:
      list_len = len(frame_scores)
    else:
      list_len = len(frame_scores)
    for k in range(list_len):
      if which_frame == 10:
        if len(str(frame_scores[k])) == 1:
          print('    '+ str(frame_scores[k])+'|', end = '')
        elif len(str(frame_scores[k])) == 2:
          print('   '+ str(frame_scores[k])+'|', end = '')
        else:
          print('  '+ str(frame_scores[k])+'|', end = '')
        break
      if len(str(frame_scores[k])) == 1:
        print('  '+ str(frame_scores[k])+'|', end = '')
      elif len(str(frame_scores[k])) == 2:
        print(' '+ str(frame_scores[k])+'|', end = '')
      elif len(str(frame_scores[k]))== 3:
        print(''+ str(frame_scores[k])+'|', end = '')
      which_frame += 1
    print()
     
def create_format_top():
  first_row = "  1"
  for i in range(2,10):
    first_row = first_row + "   "+ str(i)
  first_row = first_row + "    10 "
  print(first_row)
  second_row = "+---+"
  for i in range(2,10):
    second_row = second_row + "---+"
  second_row = second_row + "-----+"
  print(second_row)
def create_format_bottom():
  second_row = "+---+"
  for i in range(2,10):
    second_row = second_row + "---+"
  second_row = second_row + "-----+"
  print(second_row)
def main():
  #first you need to open the file and import the scores into a list
  scores = open("scores.txt",'r')
  list_scores = []
  for line in scores:
    line = line.strip()
    line = line.split()
    list_scores.append(line)
  #list_scores is a storage vessel for our imported scores
  for i in range(len(list_scores)):
    create_format_top()
    f2 = Game(list_scores,i)
    create_format_bottom()
    print()
main()
