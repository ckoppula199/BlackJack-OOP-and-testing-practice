from CardCollections import Hand, Deck

class Player:

	def __init__(self, name):
		self.name = name
		self.hand = Hand(self.name)
		self.stick = False

	def get_score(self):
		score = 0
		for index in range(self.hand.get_size()):
			score += self.hand.cards[index].get_card_value()
		return score

	def get_hand_size(self):
		return self.hand.get_size()

	def draw(self, drawpile):
		self.hand.add_card(drawpile.remove_card())
		if self.check_if_bust():
			return True
		return False

	def check_if_bust(self):
		if self.get_score() > 21:
			return True
		else:
			return False

	def display_data(self):
		print("{} has score of {}".format(self.name, self.get_score()))
		print("{}'s Hand:".format(self.name))
		print()
		for i in range(self.get_hand_size()):
			print(self.hand.cards[i])

	

class User(Player):
	def __init__(self, name):
		super().__init__(name)

	def user_turn(self, drawpile):
		print("Your score is {}".format(self.get_score()))
		print(self.hand)
		print("1) Draw card")
		print("2) Stick")
		choice = self.get_user_input()
		return self.process_choice(choice, drawpile)

	def get_user_input(self):
		choice = ""
		while True:
			choice = input(">>: ")
			if self.validate_input(choice):
				break
			print("Enter 1 or 2")
		return choice

	def validate_input(self, choice):
		if choice == "1" or choice == "2":
			return True
		else:
			return False

	def process_choice(self, choice, drawpile):
		if choice == "1":
			return self.draw(drawpile)
		else:
			self.stick = True
			return False
	

class Computer(Player):
	
	def __init__(self, name):
		super().__init__(name)

	def computer_turn(self, drawpile):
		if self.get_score() > 16:
			self.stick = True
			return False
		else:
			return self.draw(drawpile)


#DEBUG
if __name__ == "__main__":
	player = User("Chak")
	deck = Deck("testdeck")
	deck.shuffle()
	deck.deal(player.hand, 2)
	print(player.get_hand_size())
	print(player.hand)
	player.user_turn(deck)

