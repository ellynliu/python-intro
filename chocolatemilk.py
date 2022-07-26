import random
'''
Components of a class:
Once you define a class, then you can create objects.

__init__ - runs automatically when you create an object (instantiation)
properties - values of the object
methods - functions for the class
'''
# Here, we create a class for Dice, called Die
class Die:
    # In the init function, we create properties
    # num_sides is the number of sides on the die
    # face_up is the number on the top face of the die at that moment
    def __init__(self, number_sides):
        self.num_sides = number_sides
        self.face_up = None
    # roll_die is a method for the Die class
    def roll_die(self):
        self.face_up = random.randint(1, self.num_sides)

# Here, we create die1 as an object of the Die class
# Then we call the roll_die method and print out the value that the die landed on
die1 = Die(6)
die1.roll_die()
print(die1.face_up)

# Create a card class to represent cards
# Each card has a value and a suit
class Card:
    def __init__(self, card_val, card_suit):
        self.value = card_val
        self.suit = card_suit
    
    # The desc function can be used to print a string representation of a card
    # For example, the 1 of Spades will be returned as "Ace of Spades"
    def desc(self):
        val_name = self.value
        if self.value == 1:
            val_name = "Ace"
        elif self.value == 11:
            val_name = "Jack"
        elif self.value == 12:
            val_name = "Queen"
        elif self.value == 13:
            val_name = "King"
        return f"{val_name} of {self.suit}"

card1 = Card(9, "Diamonds")
card2 = Card(1, "Hearts")
card3 = Card(13, "Spades")
print(card1.desc())
print(card2.desc())
print(card3.desc())

class Deck:
    def __init__(self):
        self.cards = []
        self.build_deck()

    def build_deck(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for val in range(1, 14):
                self.cards.append(Card(val, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def print_deck(self):
        for c in self.cards:
            c.print()

    #def deal(self, num_players, hand_size):
        # your code here

deck1 = Deck()
deck1.shuffle()
deck1.print_deck()
