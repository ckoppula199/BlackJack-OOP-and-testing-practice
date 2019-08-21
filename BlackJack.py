from UserDefinedExceptions import *

class Card:

	SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]
	RANK = [None, None, "2", "3", "4", "5", "6", "7", 
			"8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, rank, suit):
		if (rank >= 2 and rank <= 13) and (suit <= 3 and suit >= 0):
			self._rank = rank
			self._suit = suit
		else:
			raise CardException(rank, suit)

	def show(self):
		return "{} of {}".format(Card.RANK[self._rank], Card.SUIT[self._suit])

if __name__ == "__main__":
	card = Card(3, 2)
	card.show()