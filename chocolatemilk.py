import random
from termcolor import colored

'''
The game of Chocolate Milk_7 involves 2 dice, a deck of 52 cards (without jokers),
and 2 or more players. Each player is dealt 7 cards and both of the dice are rolled. 

Add up the cards in your hand that are less than or equal to the sum of the dice.
Ace is worth one point, 2-10 are worth the amount on the card, Jack is 11, Queen is 12, and King is 13.
The goal is to have the highest score of all the players at the end of the round. 

Game play goes around in a circle, where each player has the option to re-roll the dice
or "stand" (AKA fold). If the player wants to re-roll the dice, they must first discard
a card in their hand before re-rolling. 

If a player choses to stand, they should turn their cards facedown and wait for the
round to end. Once all players have chosen to stand, everyone flips over their cards
and calculates their score based off the final dice roll.

The first place winner(s) of each round get 2 points, second place winner(s) get 1 point, 
and everyone else gets 0 points. Gameplay continues until one player reaches 7 points. 
'''

class Die:
    def __init__(self, num_of_faces):
        self.num_faces = num_of_faces
        self.face_up = None

    def roll_die(self):
        self.face_up = random.randint(1, self.num_faces)

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __repr__(self):
        new_name = ""
        if self.value == 1:
            new_name = "Ace"
        elif self.value == 11:
            new_name = "Jack"
        elif self.value == 12:
            new_name = "Queen"
        elif self.value == 13:
            new_name = "King"
        else:
            new_name = self.value
        new_suit = ''
        if self.suit == "Hearts":
            new_suit = colored('♥', 'red')
        elif self.suit == "Diamonds":
            new_suit = colored('♦', 'red')
        elif self.suit == "Clubs":
            new_suit = '♣'
        elif self.suit == "Spades":
            new_suit = '♠' 	 	 	 
        return f"{new_name}{new_suit}"
 	 	 	
    def print(self):
        print(self.__repr__())
    
class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        self.cards = []
        for suit in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))
    
    def show_deck(self):
        print(f'deck size {len(self.cards)}')
        print(self.cards)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num_players, hand_size):
    # TODO: may want to verify if there are enough cards in the deck
    # for the number of players and the hand size
        list_of_hands = []
        for i in range(num_players):
            hand_cards = []
            for j in range(hand_size):
                top_of_deck = self.cards.pop(0)
                hand_cards.append(top_of_deck)
            list_of_hands.append(hand_cards)
        return list_of_hands

def dict_to_sorted_tuple_list(dict):
    return sorted(dict.items(), key=lambda x: x[1], reverse=True)

# Check if the user input is an integer and that it is a value between 0 and the given max_bound.
def read_int_input(max_bound):
    while True:
        try:
            idx = int(input("What index card do you want to remove? "))
        except ValueError:
            print("Please enter a valid integer within the provided index range.")
        else:
            if 0 <= idx <= max_bound:
                return idx
            else:
                print("Please enter a valid integer within the provided index range.")

# Check if the user inputs 's' or 'r'
def read_s_or_r():
    choice = input("Do you want to stand (s) or re-roll (r)? ")
    while True:
        if choice == 's' or choice == 'r':
            return choice
        else:
            choice = input("Invalid option. Do you want to stand (s) or re-roll (r)? ")

class ChocolateMilk:
    def __init__(self, list_of_player_names, hand_size):
        # Keep track of the players, their names, and randomize the player order
        self.players = list_of_player_names
        random.shuffle(self.players)
        self.num_players = len(list_of_player_names)

        # Deal out cards to the players
        self.hand_size = hand_size
        self.players_hands = {}
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.deal()

        # Initialize two dice
        self.die1 = Die(6)
        self.die2 = Die(6)
        self.roll()
        self.previous_dice_rolls = [self.current_dice()]
        self.round_number = 1

        # Keep track of each player's score as a dictionary where the key is the player's name
        # The winner(s) of each round get 2 points, second place winner(s) get 1 point,
        # and everyone else gets 0 points
        self.players_game_scores = {}
        for p in self.players:
            self.players_game_scores[p] = 0

    # Call restart before starting a new round
    # Shuffle and deal a new deck of cards
    def restart(self):
        self.round_number += 1
        self.players_hands = {}
        self.deck = Deck()
        self.deck.build()
        self.deck.shuffle()
        self.deal()
        self.roll()
        self.previous_dice_rolls = [self.current_dice()]
        # Rotate the players by one
        first = self.players.pop(0)
        self.players.append(first)

    # Print out a player's hand
    def print_hand(self, player_name):
        count = 0
        for c in self.players_hands[player_name]:
            print(f"{count}: ", end ="")
            c.print()
            count += 1

    # Deal cards and then create a dictionary of players and their cards
    def deal(self):
        dealed_cards_list = self.deck.deal(self.num_players, self.hand_size)
        self.players_hands = dict(zip(self.players, dealed_cards_list))

    def deck(self):
        return self.deck

    def roll(self):
        self.die1.roll_die()
        self.die2.roll_die()

    def current_dice(self):
        return self.die1.face_up + self.die2.face_up
    
    # Return the card that was removed
    def remove_card(self, player_name, chosen_card_idx):
        removed_card = self.players_hands[player_name].pop(chosen_card_idx)
        return removed_card

    # Calculate the number of points a player has based on the sum of the dice
    def score_hand(self, player_name):
        score = 0
        for c in self.players_hands[player_name]:
            if c.value <= self.current_dice():
                score += c.value
        return score

    # Given a SORTED list of tuples (player_name, score), return a list
    # of player names who got the highest score (including those who tied for 1st)
    # and the winning score
    def find_winners(self, sorted_scores):
        winners_list = []
        if len(sorted_scores) < 1:
            return [], 0
        max_score = sorted_scores[0][1]
        # Get winners
        for k, v in sorted_scores:
            if v == max_score:
                winners_list.append(k)

        return winners_list, max_score

    # Play one turn where the player has the option to re-roll and remove a card
    # Return the player's name IF they choose to stand (AKA fold)
    # Otherwise, return None
    def run_turn(self, player_name):
        print(f"\n{player_name}'s turn")

        # If a player has no cards left, return their name to skip their turn
        # Essentially, they have automatically chosen to stand
        if len(self.players_hands[player_name]) == 0:
            print("No cards left. Cannot play turn.")
            return player_name

        print(f"Current value of dice: {self.current_dice()}")
        print(f"Past dice rolls: {self.previous_dice_rolls}")
        print("Your hand: ")
        self.print_hand(player_name)
        print(f"Your current score is: {self.score_hand(player_name)}")

        # Check if the user inputs 's' or 'r'
        next = read_s_or_r()
        
        # Stand
        if next == 's':
            return player_name

        # Re-roll
        elif next == 'r':
            # Ask for input to remove card
            to_remove = read_int_input(len(self.players_hands[player_name]))
            
            # Roll the dice and remove the desired card
            self.roll()
            self.previous_dice_rolls.append(self.current_dice())
            print(f"New value of dice: {self.current_dice()}")
            removed = self.remove_card(player_name, to_remove)
            print(f"You removed {removed}")
            return None

    # Play a round
    # As long as there are some players remaining who have not chosen to stand, keep playing.
    def run_round(self):
        print(f"\nSTARTING ROUND {self.round_number}")
        standing_players = []
        while (len(standing_players) < self.num_players):
            for player in self.players:
                if player in standing_players:
                    continue
                else:
                    result_of_turn = self.run_turn(player)
                    # If a player chose to stand or ran out of cards, 
                    # run_turn will return the player's name
                    if result_of_turn != None:
                        standing_players.append(player)
        print(f"END OF ROUND {self.round_number}")
        
        # At the end of the round, calculate the scores of each player's hand
        total_scores = {}
        for p in self.players:
            total_scores[p] = self.score_hand(p)

        # sorted_scores contains a list of tuples of player names and their scores, sorted in descending order
        sorted_scores = dict_to_sorted_tuple_list(total_scores) 
        print_sorted_scores = dict_to_sorted_tuple_list(total_scores) 
        
        # Get first place winners
        first_place_list, first_place_score = self.find_winners(sorted_scores)
        
        # Remove first place winners to find the second place winners 
        for i in range(len(first_place_list)):
            sorted_scores.pop(0)

        # Get second place winners
        second_place_list, second_place_score = self.find_winners(sorted_scores)

        print(f"Everyone's scores: {print_sorted_scores}")
        print(f"First place winner(s): {first_place_list}")
        print(f"Second place winner(s): {second_place_list}")

        for p in first_place_list:
            self.players_game_scores[p] += 2
        for p in second_place_list:
            self.players_game_scores[p] += 1

        print_sorted_game_scores = dict_to_sorted_tuple_list(self.players_game_scores)
        print("Game scores: \n", print_sorted_game_scores)
        input("\nType any key to continue: ")
        
    # The game is over once a player reaches 7 points
    def check_game_over(self):
        for k, v in self.players_game_scores.items():
            if v >= 7:
                return True
        return False

    def run_game(self):
        while not self.check_game_over():
            self.run_round()
            self.restart()
        print("Game over!")
        print_sorted_final_scores = dict_to_sorted_tuple_list(self.players_game_scores)
        print(f"Final scores: {print_sorted_final_scores}")

# To play a game, replace the list of names with the names of your players
# The 7 determines the hand size, so each player will receive 7 cards.
game = ChocolateMilk(["Ms. Ellyn", "Ms. K", "Mr. Emilio", "Mr. Ben", "Mr. Shaw"], 7) 
game.run_game()
