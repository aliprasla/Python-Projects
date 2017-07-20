import random
#  File: Blackjack.py
#  Description: One player plays blackjack with the computer
#  Student's Name: Ali Prasla
#  Student's UT EID: anp2429
#  Course Name: CS 313E 
#  Unique Number: 51320
#  Date Created: 9/18/2016
#  Date Last Modified: 9/21/2016
class Deck():
  #a deck has 4 suits and 13 different pips
        cardList = []
        possible_pips = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
        possible_suits = ['C','D','H','S']
        def __init__(self):
                for i in range(len(self.possible_suits)):
                        for k in range(len(self.possible_pips)):
                                newCard = Card(self.possible_pips[k],self.possible_suits[i])
                                self.cardList.append(newCard)
                                
        def shuffle(self):
                random.shuffle(self.cardList)
        def __str__ (self):
                out = ''
                for i in range(0,13):
                        out += ' ' + str(self.cardList[i])
                out += '\n'
                for i in range(13,26):
                        out += ' ' + str(self.cardList[i])
                out += '\n'
                for i in range(26,39):
                        out += ' ' +str(self.cardList[i])
                out += '\n'
                for i in range(39,len(self.cardList)):
                        out += ' ' +str(self.cardList[i])
                out += '\n'
                return out
         
        def dealOne(self,player):
                player.hand.append(self.cardList[0])
                player.handTotal += self.cardList[0].val
                self.cardList = self.cardList[1::]
class Card(Deck):
        #a card has a suit and a pip
        pip = ''
        suit = ''
        val = 0
        def __init__(self, pip,suit):
                self.pip = pip
                self.suit = suit
                #card value
                try:
                        self.val = int(pip)
                except ValueError:
                        if pip == 'A':
                                self.val = 11
                        else:
                                self.val = 10
        def __str__ (self):
                return str(self.pip) + str(self.suit)
class Player():
        def __init__(self):
                self.hand = []
                self.handTotal = 0
        def __str__(self):
                end = ''
                for i in range(len(self.hand)):
                        end += str(self.hand[i]) + ' '
                return end
def showHands(player, dealer):
        for i in range(2):
                print()
        print("Dealer shows " + str(dealer.hand[1]) + " faceup")
        print("You show " + str(player.hand[1]) + " faceup")
        print ()
        print ("You go first.")
        print()
def opponentTurn(cardDeck,dealer,opponent):
        print("You hold " + str(opponent) + 'for a total of ' + str(opponent.handTotal))
        #if ace is drawn.
        if (opponent.hand[0].pip == 'A' or opponent.hand[1].pip == 'A'):
                print("Assuming ace is 11")
        #action
        action = eval(input("Do you want to hit (1) or stay (2)? "))
        print()
        first_move = True
        while action == 1:
                print("You drew " + str(cardDeck.cardList[0]))
                cardDeck.dealOne(opponent)
                #need to check if there is an ace
                if first_move:
                        if (opponent.hand[0].pip == 'A' or opponent.hand[1].pip == 'A') and opponent.handTotal > 21:
                                print("Over 21. Switching Ace into 1")
                                #fix this logic
                                opponent.handTotal -= 10
                else:
                        if(opponent.hand[-1].pip == 'A'):
                                if opponent.handTotal > 21:
                                        print("Over 21. Switching Ace into 1")
                                        opponent.handTotal -= 10
                        else:
                                if opponent.handTotal > 21:
                                        print("Over 21. You bust!")
                if opponent.handTotal > 21:
                        print("Your hand is worth : " + str(opponent.handTotal))
                        print("You bust!" , end = ' ')
                        return
                if opponent.handTotal == 21:
                        print("21! ", end = '')
                        return
                print("You hold " + str(opponent) + 'for a total of ' + str(opponent.handTotal))
                print()
                action = eval(input("Do you want to hit (1) or stay (2)? "))
                print()
                first_price = False
        if action == 2:
                print("Staying with " + str(opponent.handTotal))
def dealerTurn(cardDeck,dealer,opponent):
        print()
        if opponent.handTotal > 21:
                print()
                print ("Game over. Dealer wins.")
                print()
                return
        else:
                print("Dealer's turn")
                print("Your hand: " + str(opponent) + 'for a total of ' + str(opponent.handTotal))
                print("Dealer's hand: " + str(dealer) + 'for a total of ' + str(dealer.handTotal))
                #insert dealers moves
                first_move = True
                while dealer.handTotal < opponent.handTotal:
                        if first_move:
                                if (dealer.hand[0].pip == 'A' or dealer.hand[1].pip == 'A') and dealer.handTotal > 21:
                                        print("Over 21. Switching Ace into 1")
                                #fix this logic
                                        opponent.handTotal -= 10
                        else:
                                if(opponent.hand[-1].pip == 'A'):
                                        if opponent.handTotal > 21:
                                                print("Over 21. Switching Ace into 1")
                                                opponent.handTotal -= 10
                        first_move = False
                        print()
                        print("Dealer hits: " + str(cardDeck.cardList[0]))
                        cardDeck.dealOne(dealer)
                        print("New total: " + str(dealer.handTotal))
                        print()
                        for i in range(len(dealer.hand)):
                                if dealer.hand[i].pip == 'A' and dealer.handTotal > 21:
                                        print("Over 21. Switching Ace into 1")
                                        #fix this logic
                                        dealer.handTotal -= 10
                        if dealer.handTotal > 21:
                              print()
                              print("Dealer busts! You win.")
                              print("Game over.")
                              return
        if dealer.handTotal >= opponent.handTotal:
                print("Dealer wins. Game over.")
                print()
                return
        
def main():
        cardDeck = Deck()
        print("Initial deck:")
        print(cardDeck)
        #still need to figure out how to print out deck and card.
        random.seed(50)
        cardDeck.shuffle()
        print("Shuffled deck:")
        print(cardDeck)
        dealer = Player()
        print("Deck after four draws:")
        opponent = Player()
        cardDeck.dealOne(opponent) #face down
        cardDeck.dealOne(dealer) #face down
        cardDeck.dealOne(opponent) #face up
        cardDeck.dealOne(dealer) #face up
        print(cardDeck)
        
        showHands(opponent,dealer)
        opponentTurn(cardDeck,dealer,opponent)
        dealerTurn(cardDeck,dealer,opponent)
        #things still left to accomplish:
        #ace reversion form 11 to 1.
        #opponent turn method.
        print("Final hands: ")
        print("  Dealer:  " + str(dealer))
        print("  Opponent: " + str(opponent))
main()
