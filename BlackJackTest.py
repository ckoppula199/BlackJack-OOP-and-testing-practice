import BlackJack

def basic_card_test():
	card = BlackJack.Card(12, 2)
	assert card.show() == "The Queen of Hearts", "Output: " + card.show()

def tests():
	basic_card_test()

if __name__ == "__main__":
	tests()