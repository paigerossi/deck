"""
***************************************************************
FILE: Deck.py
AUTHOR: Paige Rossi
PARTNER: none
ASSIGNMENT: Project 6
DATE: October 30, 2016
DESCRIPTION: This is a program that develops a class for a card and another for 
a deck of cards then tests them
***************************************************************
"""

import random
from cs110graphics import *

class Deck:
    """A class for building a deck of cards. This class is not graphical."""
    
    def __init__(self):
        """Creates a complete deck of 52 playing cards."""
        
        suits = ['hearts', 'clubs', 'diamonds', 'spades']
        names = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen',
                 'king', 'ace']
                 
        link = 'http://cs.hamilton.edu/~mbailey/cards/'
        suffix = '.gif'
        backFaceName = 'http://cs.hamilton.edu/~mbailey/cards/back.gif'
        cardList = []
                 
        for suit in suits:
            for name in names:
                card = Card(suit, name, (link + suit[0] + name[0] +
                                         suffix), backFaceName)
                cardList.append(card)
                
        self._cards = cardList
        
    def returnDeck(self):
        """Returns the list of cards in the deck"""
        
        return self._cards
        
    def empty(self):
        """Returns True if the deck no longer contains any cards."""
        
        remainInDeck = self._cards
        
        if len(remainInDeck) == 0:
            return True
        return False
        
    def deal(self):
        """Deals a card. A card is removed from the top of the deck 
        and returned"""
        
        deckList = self._cards
        topCard = deckList[-1]
        deckList.pop(-1)
        return topCard
        
        
    def shuffle(self):
        """All cards currently in the deck are randomly ordered."""
        
        deckList = self._cards
        shuffledList = []
        
        for _ in range(len(deckList)):
            choice = deckList[random.randrange(len(deckList))]
            shuffledList.append(choice)
            deckList.remove(choice)
            
        self._cards = shuffledList
        
        
class Card(EventHandler):
    """A class used for building graphical playing cards"""
    
    def __init__(self, suit, name, faceFileName, backFileName):
        """Creates a playing card with the given suit and name."""
        EventHandler.__init__(self)
        self._suit = suit
        self._name = name
        self._back = backFileName
        self._face = faceFileName
        self._center = (200, 200)
        self._width = 71
        self._height = 96
        
        self._cardBack = Image(self._back, self._center, self._width,\
        self._height)
        self._cardBack.addHandler(self)
        
        self._cardFront = Image(self._face, self._center, self._width,\
        self._height)
        self._cardFront.addHandler(self)
        
    def handleMousePress(self):
        """Flips the card when it is clicked."""
        
        self.flip()
        
    def getSuit(self):
        """Returns the name of the suit."""
        
        return self._suit
        
    def getName(self):
        """Returns the name of the card"""
        
        return self._name
        
    def addTo(self, window):
        """Adds the card to the given graphics window"""
        
        window.add(self._cardFront)
        window.add(self._cardBack)
        
    def removeFrom(self, window):
        """Removes the card from the given graphics window."""
        
        window.remove(self._cardBack)
        window.remove(self._cardFront)
        
    def flip(self):
        """Flips the card over visually."""
        
        frontDepth = self._cardFront.getDepth()
        self._cardBack.setDepth(frontDepth + 1)
        
        self._cardFront.move(-100, 0)
        self._cardBack.move(-100, 0)
        self._cardFront.setDepth(0)
        
    def move(self, dx, dy):
        """Moves a card by dx and dy."""
        
        self._cardFront.move(dx, dy)
        self._cardBack.move(dx, dy)
        
    def getReferencePoint(self):
        """The point representing the center of the card image is returned."""
        
        refPoint = self._cardFront.getCenter()
        return refPoint
        
    def size(self):
        """Returns the tuple (width, height)"""
        
        dimensions = (self._width, self._height)
        return dimensions
        
    def setDepth(self, depth):
        """Sets the depth of graphical objects representing the card to depth"""
        
        self._cardFront.setDepth(depth)
        
def testDeck(win):
    """Tests the classes for Card and Deck"""
    
    deck = Deck()
    deck.shuffle()
    deckList = deck.returnDeck()
    for _ in range(len(deckList)):
        card = deck.deal()
        card.addTo(win)
        
StartGraphicsSystem(testDeck)
