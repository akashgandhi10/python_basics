# # Blackhjack
#
# - Deck
# - Card
# - Player, Dealer
#
#
# class Card(object):
#   def __init__(self):
#     self.suite, self.facevalue, self.value,
#
#
# class Deck(object):
#   def __init__(self):
#     self.deck = 52 * Card()
#     self.shuffle,
#     self.dealCard()
#
#
# def game():
#   player1, player2,
#   deck = Deck()
#   deck,shuffle(),
#   deck.dealCard()

import random



class Card(object):
    def __init__(self, suite, value):
        self.suite = suite
        self.value = value
        if value >= 10:
        	self.facevalue = 10
        else:
        	self.facevalue = value


    def __repr__(self):
    	return self.suite + str(self.value)


class Deck(object):
	def __init__(self):
		self.cards = self.generateDeck()  # This will assign 52 cards for the deck
		self.shuffle()


	@staticmethod
	def generateDeck():
		suits = ['clubs', 'spades', 'hearts', 'diamonds']
		values = range(1, 14)
		cards = []
		for s in suits:
			for v in values:
				cards.append(Card(suite=s, value=v))
		return cards


	def shuffle(self):
		random.shuffle(self.cards)


	def deal(self):
		return self.cards.pop()


class Player(object):
	def __init__(self, name):
		self.name = name
		self.cards = []
		self.total = 0


	def __repr__(self):
		return self.cards


	def giveCard(self, card):
		self.cards.append(card)
		self.makeTotal()


	def makeTotal(self):
		total = 0
		for c in self.cards:
			total += c.facevalue
		self.total = total


def printPlayer(p):
	print p.cards, p.total


def printDealer(d):
	print d.cards, d.total


def checkWinner(p, d):
	if p.total == 21:

		print 'Player Wins!'
		return True
	elif d.total == 21:
		printPlayer(p)
		printDealer(d)
		print 'Dealer Wins!'
		return True
	elif p.total > 21:
		printPlayer(p)
		printDealer(d)
		print 'Dealer Wins!'
		return True
	elif d.total > 21:
		printPlayer(p)
		printDealer(d)
		print 'Player Wins!'
		return True
	return False


def main():
	deck = Deck()
	player1 = Player('akash')
	player2 = Player('dealer')

	player1.giveCard(deck.deal())
	player1.giveCard(deck.deal())
	printPlayer(player1)
	player2.giveCard(deck.deal())
	print player2.cards, player2.total
	player2.giveCard(deck.deal())



	checkWinner(player1, player2)

	while True:
		if checkWinner(player1, player2):
			return
		print " "
		askplayer = raw_input("Do you want to hit or stay?(h/s) ").lower()

		if askplayer.startswith("h"):
			player1.giveCard(deck.deal())
			printPlayer(player1)
		else:
			break

	while player2.total < 17:
		player2.giveCard(deck.deal())
		if checkWinner(player1, player2):
			return

	printPlayer(player1)
	printDealer(player2)
	pf = 21 - player1.total
	df = 21 - player2.total
	if pf < df:
		print("Player Wins")
	elif df < pf:
		print("Dealer Wins")
	else:
		print("Push")
	return



if __name__=='__main__':
	main()
