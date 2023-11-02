"" cardGame.py
basic card game framework
keeps track of card locations for as many hands as needed
"""
#import from random all the classes and libraries
from random import *
#these variables get a certain value and they are all a part of the
starter code
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
#these variables are all a part of the starter code with them being used
throughout the code
cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
"Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")
# function clearDeck is defined
def clearDeck():
#cardLoc variable gets index 0 multiplied by the value of variable
NUMCARDS
cardLoc=[0]*NUMCARDS
#function assignCard gets defined
def assignCard(y):
#keepGoing variable gets value True
keepGoing = True
#while loop is introduced with: “while keepGoing”, keepGoing value is true
so the while loop begins
while keepGoing:
#variable random gets a random integer between 0 and 51
random = randint(0,51)
#if variable cardLoc index random is equal to 0
if cardLoc[random] == 0:
#cardLoc index random is stored in variable “y”
cardLoc[random]= y
#keepGoing variable now has False value
keepGoing = False
#function showDeck is defined
def showDeck():
#print statement: Location of all cards
print("Location of all cards")
#print statement: ("# card location")
print("# card location")
# variable number gets value 0
number = 0
# for i in range length suitName, for each value in the length of suitName
for i in range (len(suitName)):
# for k in range length rankName, for each value in the length of rankName
for k in range (len(rankName)):
# print the value of number + one of the value from rankName list + one
of the value from suitName list + playerName index the cardLoc index of
the value of number
print (number , " " + rankName[k] +" of "+ suitName[i] + " "
+ playerName[cardLoc[number]])
# number now gets number plus the value 1
number = number +1
# function showHand is defined
def showHand(y):
#this print statement is just for spacing
print()
#print statement saying displaying computer or player’s hand
print("Displaying " + playerName[y] + " hand:")
#this print statement is just for spacing
print()
#for in in the range of 52
for i in range (52):
# if the carLoc variable with index i is equal to value of y
if cardLoc[i] == y:
# print the rankName index i mod 13, of, and the suitName i divided by 13
using integer division
print(rankName[i%13]+ " of " + suitName[i//13])
#this is all a part of the stater code calling all of the functions
def main():
clearDeck()
# this is for assigning a card to the computer and player, it will do for
i in range 5 to assign each person five cards
for i in range(5):
assignCard(PLAYER)
assignCard(COMP)
#these functions are called for showing the deck and which ones are for
computer and which ones are for the player
showDeck()
showHand(PLAYER)
showHand(COMP)
#main is defined at the bottom
main()
