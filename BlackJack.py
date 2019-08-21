class Card:

	SUIT = ["Clubs", "Diamonds", "Hearts", "Spades"]
	RANK = [None, None, "2", "3", "4", "5", "6", "7", 
			"8", "9", "10", "Jack", "Queen", "King"]

	def __init__(self, rank, suit):
		self._suit = suit
		self._rank = rank

	def show(self):
		return "The {} of {}".format(Card.RANK[self._rank], Card.SUIT[self._suit])

if __name__ == "__main__":
	pass