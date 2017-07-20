import random
#keeps track of all user input 
#choiceCounter[0] is Rock Selection
#choiceCounter[1] is Paper Selection
#choiceCounter[2] is Scissors selection
choiceDict = {0:"Rock",1:"Paper",2:"Scissors"}
def updateChoiceCounter(userChoice,choiceCounter):
    choiceCounter[userChoice] += 1
    return choiceCounter
def computerSelection(choiceCounter):
    #if all choices are equal
    if(choiceCounter[0] == choiceCounter[1] and choiceCounter[1] == choiceCounter[2]):
        return random.choice([0,1,2])
    #if there is one dominant value
    elif(hasSingleLargeValue(choiceCounter)):
        userPref = choiceCounter.index(max(choiceCounter))
        if(userPref == 0):
            return 1
        elif(userPref == 1):
            return 2
        else:
            return 0
    #stochastic handling. I.e if two are equal
    elif(choiceCounter[0] == choiceCounter[1]):
        return random.choice([0,1])
    elif(choiceCounter[0] == choiceCounter[2]):
        return random.choice([0,2])
    elif(choiceCounter[1] == choiceCounter[2]):
        return random.choice([1,2])
    
def hasSingleLargeValue(l):
    m = max(l)
    idx = []
    for item in l:
        if item == m:
            idx.append(item)            
    if len(idx) > 1:
        return False
    return True
def promptUser():
    print ""
    print "Select 1 for Rock"
    print "Select 2 for Paper"
    print "Select 3 for Scissors"
    print "Select 4 to Quit"
    return raw_input()
def isInvalid(inp):
    try:
        k = int(inp)
        if( k not in [1,2,3,4]):
            return True
        return False
    except:
        return True
def printSelections(userChoice, computerChoice):
    print "Player selected: " + choiceDict[userChoice]
    print "Computer selected: " + choiceDict[computerChoice]
def runGame(userChoice,computerChoice,winCounter):
    winner = ""
    printSelections(userChoice,computerChoice)
    if(computerChoice == userChoice):
        print "It's a tie!"
        winner = "Tie"
    #player wins if he/she selects rock, and Cpu selects scissors.
    #if he/she selects paper and Cpu selects rock
    # if he/she selects scissors and Cpu selects paper
    elif((userChoice == 0 and computerChoice == 2) or (userChoice == 1 and computerChoice == 0) or (userChoice == 2 and computerChoice == 1)):
        print "Player wins!"
        winner = "Player"
    else:
        print "Computer wins"
        winner = "Computer"
    return updateCounter(winner,winCounter)
def updateCounter(winner,winCounter):
    if winner == "Player":
        winCounter[0] += 1
    elif winner == "Computer":
        winCounter[1] += 1
    else:
        winCounter[2] += 1
    return winCounter
def main():
    choiceCounter = [0,0,0]
    winCounter = [0,0,0]
    playing = True
    while(playing):
        computerChoice = computerSelection(choiceCounter)
        userChoice = promptUser()
        while(isInvalid(userChoice)):
            print "Invalid Input"
            userChoice = promptUser()
        #change to int
        userChoice = int(userChoice)
        if (userChoice == 4):
            playing = False
            break
        #run game:
        winCounter = runGame(userChoice-1,computerChoice,winCounter)
        choiceCounter = updateChoiceCounter(userChoice-1,choiceCounter)
        
    print ""
    print "Total Games: " + str(sum(winCounter))
    print "Games won: " + str(winCounter[0])
    
    
main()
