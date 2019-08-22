class CardException(Exception):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

		print("Invalid Card Configurations: suit -> {}, rank -> {}".format(self.suit, self.rank))

	