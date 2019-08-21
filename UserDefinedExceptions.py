class CardException(Exception):

	def __init__(self, rank, suit):
		self.rank = rank
		self.suit = suit

		print("Invalid Card Configurations")
		print("Given rank: {}".format(self.rank))
		print("Given suit: {}".format(self.suit))

	