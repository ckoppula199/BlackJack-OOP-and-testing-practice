import random
import Card

class CardCollection:

	def __init__(self, label):
		"""label is a name, cards is a list of cards"""
		self.label = label
		self.cards = []

	def __repr__(self):
		return "{}: {}".format(self.label, self.cards)

	def add_card(self, card):
		self.cards.append(card)

	#overloaded method, if no index given removes the last element in the list
	def remove_card(self, index=None):
		if index == None:
			return self.cards.pop(self.get_size() - 1)
		return self.cards.pop(index)

	def get_size(self):
		return len(self.cards)

	def is_empty(self):
		return self.get_size() == 0

	def swap_cards(self, a, b):
		temp_card = self.cards[a]
		self.cards[a] = self.cards[b]
		self.cards[b] = temp_card

	def shuffle(self):
		for index in range(self.get_size() - 1):
			random_index = random.randint(0, index)
			self.swap_cards(index, random_index)

	def deal(self, deal_to_collection, num_of_cards):
		for i in range(num_of_cards):
			temp_card = self.remove_card()
			deal_to_collection.add_card(temp_card)


#DEBUG
if __name__ == "__main__":
	draw_pile = CardCollection("Draw Pile")
	hand = CardCollection("Hand")
	for i in range(2, 14):
		card = Card.Card(i, 2)
		draw_pile.add_card(card)


	print(draw_pile)
	draw_pile.shuffle()
	print(draw_pile)
	draw_pile.swap_cards(2, 6)
	print(draw_pile)
	draw_pile.deal(hand, 6)
	print(hand)
