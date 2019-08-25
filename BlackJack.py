from Players import *
from CardCollections import *
from Card import Card

class Blackjack:

	def __init__(self):
		self.user = User("user")
		self.computer = Computer("computer")
		self.drawpile = Deck("drawpile")
		self.drawpile.shuffle()
		self.game_over = False

	def initial_deal(self):
		self.user.hand.add_card(self.drawpile.remove_card())
		self.user.hand.add_card(self.drawpile.remove_card())
		self.computer.hand.add_card(self.drawpile.remove_card())
		self.computer.hand.add_card(self.drawpile.remove_card())

	def users_turn(self):
		is_bust = self.user.user_turn(self.drawpile)
		if is_bust:
			self.game_over = True

	def computers_turn(self):
		is_bust = self.computer.computer_turn(self.drawpile)
		if is_bust:
			self.game_over = True

	def show_scores(self):
		self.user.display_data()
		print()
		self.computer.display_data()

		user_bust = self.user.check_if_bust()
		computer_bust = self.computer.check_if_bust()
		if self.check_whos_bust(user_bust, computer_bust):
			return

		self.check_scores()

	def check_whos_bust(self, user_bust, computer_bust):
		if user_bust and computer_bust:
			print("Both players bust!")
			return True
		elif user_bust and not computer_bust:
			print("{} bust, {} wins".format(self.user.name, self.computer.name))
			return True
		elif not user_bust and computer_bust:
			print("{} bust, {} wins".format(self.computer.name, self.user.name))
			return True
		return False

	def check_scores(self):
		if self.user.get_score() > self.computer.get_score():
			print("{} wins!".format(self.user.name))
		elif self.user.get_score() < self.computer.get_score():
			print("{} wins!".format(self.computer.name))
		else:
			print("Its a draw!")


	def play_game(self):
		self.initial_deal()
		while True:
			self.users_turn()
			self.computers_turn()
			if self.game_over:
				self.show_scores()
				break
			if self.user.stick and self.computer.stick:
				self.show_scores()
				break

if __name__ == "__main__":
	blackjack = Blackjack()
	blackjack.play_game()