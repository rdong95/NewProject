#!/usr/bin/python

import sys
import unittest
import random
suit = ("heart","diamond","club","spades")
ranks = ('A', '2','3','4','5','6','7','8','9','10','J','Q','K')
values = {'A':1 or 11, '2':2, '3':3,'4':4, '5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'J':10,'Q':10,'K':10}

class card:
	def __init__(self, suit, ranks): 
		self.suit = suit
		self.values = ranks
		 
	def __str__(self):
		return self.ranks + "of" + self.suit
class deck:
	def __init__(self):
		self.card = [ ] 
		for x in range(13):
			for y in range(4):
				self.card.append(card(y,x))
	def __str__(self):
		return self.card
	def deal(self, handsize):
        	dealtcards = [ ]
        	for i in range(handsize):
            		dealtcards.append(str(self.card[randrange(52)]))
        	return dealtcards 	
	def printdeck(self):
			for card in self.card:
				print card

class Player: 
	def __init__(self, name = "Player 1"):
		self.hand = [] 
		self.name = name 
		self.score = 0
	def sethand(self,card):
		self.hand.append(card)
	def gethand(self):
		return self.hand 
	def clearhand(self):
		self.hand = []
	def setscore(self):
		self.score=self.score + 1
	def getscore(self):
		return self.score	
class Dealer:
	def __init__(self):
		self.hand = []
		self.name = "DEALER"	
	def sethand(self,card):
		self.hand.append(card)
	def gethand(self):
		return self.hand
	def clearhand(self):
		self.hand = []
class GAME: 
	def __init__(self):
		self.deck = deck()
		self.card = card()
		self.player = Player()
		self.dearler = Dealer()
	def intro(self):
		print "Hello, let's play Blackjack"
		self.player
	def 
	
