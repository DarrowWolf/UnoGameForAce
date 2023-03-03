import random
import time
import numpy as np

# Create an array of card values and colors
cardVal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'Skip', 'Reverse', 'Draw Two', 'Wild', 'Wild Draw Four']
cardColors = ['Red', 'Yellow', 'Green', 'Blue']

class Deck:

    # makes a deck of cards
    @staticmethod
    def create_deck():
        deck = []
        for i in cardColors:
            for j in cardVal:
                if j not in ['Wild', 'Wild Draw Four']:
                    deck.append((j,i))
                else:
                    deck.append((j, None))
        return deck




    # Create a function to shuffle the cards
    @staticmethod
    def shuffle_deck(deck):
        random.shuffle(deck)
        return deck

    # Create a function to deal n number of cards to n number players
    @staticmethod
    def deal_cards(deck, players):
        numOfPlayers = len(players)
        numOfCards = 7
        for i in range(numOfCards*numOfPlayers):
            players[i % numOfPlayers].hand.append(deck[i])
        return players

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    #Draw cards from the top of the deck
    def draw_card(self, deck):
        card = deck.pop()
        self.hand.append(card)
        return card

class DiscardPile:
    #Creates a list to store discarded cards
    def __init__(self):
        self.pile = []
    #Adds to the discarded pile
    def add_to_pile(self, card):
        self.pile.append(card)


#Will expand on this later on when adding the rules n mechs to the game
class UnoMain:
    def __init__(self, players):
        self.players = players
        self.deck = Deck()
        self.discard_pile = DiscardPile()
        self.current_player = 0
        self.direction = 1 
        self.skip = False
        self.draw_count = 0


        starting_card = deck.pop()
        self.discard_pile.add_to_pile(starting_card)

    def choose_color(self, player):
        print(f"{player.name}, choose a color (Red, Yellow, Green, Blue): ")
        color = input().strip()
        while color not in cardColors:
            print("Invalid color, choose a valid color (Red, Yellow, Green, Blue): ")
            color = input().strip()
        return color
    
    def draw(self, player):
        card = deck.pop()
        player.hand.append(card)
        print(f"{player.name} drew a card")
        return card

    def card_legality(self, card):
        if len(self.discard_pile.pile) == 0:
            return True
        if not self.discard_pile.pile:
            return False
        top_card = self.discard_pile.pile[-1]
        if top_card[1] is None:
            # Wild card is on top, so any card can be played
            return True
        if card[1] == top_card[1] or card[0] == top_card[0]:
            # Card color or value matches top card
            return True
        if card[0] in ['Wild', 'Wild Draw Four']:
            # Wild card can be played at any time
            return True

        return False

    def play_card(self, player, card):
        if self.card_legality(card):
            player.hand.remove(card)
            self.discard_pile.add_to_pile(card)
        else:
            print("Illegal move, please play another card!")
            return

        if card[0] in ["Wild", "Wild Draw Four"]:
            color = self.choose_color(player)
            card = (card[0], color)

        self.discard_pile.add_to_pile(card)

        if card[0] == "Skip":
            self.skip = True
        elif card[0] == "Reverse":
            self.direction *= -1
        elif card[0] == "Draw Two":
            self.draw_count = 2
        elif card[0] in ["Wild Draw Four"]:
            self.draw_count = 4

        if self.draw_count:
            next_player = self.players[(self.players.index(player) + self.direction) % len(self.players)]
            for i in range(self.draw_count):
                next_player.draw_card(deck)
            self.draw_count = 0
        if self.skip:
            self.skip = False
            self.current_player = (self.current_player + 2*self.direction) % len(self.players)
        else:
            self.current_player = (self.current_player + self.direction) % len(self.players)

            

# Create a list of players
players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]

# Create a deck of cards
deck = Deck.create_deck()
deck = Deck.shuffle_deck(deck)
players = Deck.deal_cards(deck, players)
game = UnoMain(players)

# Main game loop
while True:
    restartGame = False
    while True:
        player = game.players[game.current_player]
        print(f"{player.name}'s turn")
        print(f"Your hand: {player.hand}")
        print(f"If you want to draw a card type 'Draw'")
        if game.discard_pile.pile:
            print(f"Top card: {game.discard_pile.pile[-1]}")
        else:
            print("The discard pile is empty.")
        print(f"Enter the index of the card you want to play:")
        print("\tIf you pick 0 it will play your first card. if you pick 1 it will play your second card")
        input_str = input().strip()
        if input_str.lower() == "draw":
            game.draw(player)
        if input_str.lower() == "bark at me":
            print("\n\n")
            print("\nWoof! Woof! Awrf! Woof!")
            print("\n\n")
            continue
        if input_str.lower() == "rage quit":
            break
        if input_str.lower() == "restart":
            restartGame = True
            break
        try:
            index = int(input_str) #0 is your first card, 1 is your second card and so on. try avoiding picking wild cards.. reverse works :D 
            card = player.hand[index]
            game.play_card(player, card)
            if len(player.hand) == 0:
                print(f"{player.name} has won the game!")
                restartGame = True
                break
        except ValueError:
            print("Please enter a valid integer.")
        except IndexError:
            print("Please enter an index within the range of your hand.")
    if restartGame == False:
        break

class TestChecks:
    @staticmethod
    def run_tests():
        print("Test Starting...")
        time.sleep(2)#Make ccool pause before everyhting shows pass!! yay!

        print("Testing create_deck funtion:")
        if TestChecks.test_deck_create_deck():
            print("\tPASSED")
        else:
            print("\tFAILED")
            print(deck)
        
        print("Testing shuffle_deck function:")
        if TestChecks.test_deck_shuffle_deck():
            print("\tPASSED")
        else:
            print("\tFAILED")
            print(Deck.shuffle_deck(deck))

        print("Testing deal_cards function:")
        if TestChecks.test_deck_deal_cards():
            print("\tPASSED")
        else:
            print("\tFAILED")

        print("Testing draw_card function:")
        if TestChecks.test_discard_pile():
            print("\tPASSED")
        else:
            print("\tFAILED")

        print("Testing direction is set to 1:")
        if TestChecks.test_uno_main_direction():
            print("\tPASSED")
        else:
            print("\tFAILED")

    @staticmethod
    def test_deck_create_deck():
        deck = Deck.create_deck()
        if len(deck) == len(cardVal)*len(cardColors):
            if ("0", "Red") in deck and ("Wild Draw Four", "Blue") in deck:
                return True
        return False


    @staticmethod
    def test_deck_shuffle_deck():
        deck_shuffled = Deck.shuffle_deck(deck)
        if deck != deck_shuffled:
            return False
        return True

    @staticmethod
    def test_deck_deal_cards():
        deck = Deck.create_deck()
        players = [Player("Player 1"), Player("Player 2")]
        dealt_players = Deck.deal_cards(deck, players)
        for player in dealt_players:
            if len(player.hand) != 7:
                return False
        return True

    @staticmethod
    def test_discard_pile():
        discard_pile = DiscardPile()
        discard_pile.add_to_pile(("0", "Red"))
        if len(discard_pile.pile) == 1:
            if discard_pile.pile[0] == ("0", "Red"):
                return True
        return False

    @staticmethod
    def test_uno_main_direction():
        uno_game = UnoMain(players)
        if uno_game.direction == 1:
            return True
        return False


#Debug usually set to 'False' but is set to 'True' for testing purposes~
debug = False
if debug:
    
    TestChecks.run_tests()
    print("Tests finished.")
    print("\n\n")
    print("\n\n")

    time.sleep(2)

    #To Test discard pile and print the player hand whose card has been discarded 
    #'0' is player 1, '1' is player 2 and so on. Default is '0'.
    choose_player = 0

    deck = Deck.create_deck()
    
    print(deck) #prints created deck

    print("\n\n")

    # Shuffle the deck of cards
    Deck.shuffle_deck(deck)
    print(Deck.shuffle_deck(deck)) #prints shuffled deck

    print("\n\n")

    # Deal cards to players
    players = Deck.deal_cards(deck, players)

    # Print the players' hands
    for player in players:
        print(f'{player.name} has the following cards:')
        for card in player.hand:
            print(f'\t{card}')
        print()

    print("\n\n")

    discard_pile = DiscardPile()

    # Example test of the discard pile
    discarded_card = players[choose_player].hand.pop()
    discard_pile.add_to_pile(discarded_card)

    print(f'{players[choose_player].name} discarded {discarded_card}')
    print(f'Discard pile: {discard_pile.pile}')

    print("\n\n")

    # Print the chosen player's hand
    print(f'{players[choose_player].name} has the following cards:')
    for card in players[choose_player].hand:
        print(f'\t{card}')

    print("\n\n")
    

else:
    print("Change Debug setting from \"False\" to \"True\" if you want to see debug output")









#Everything so messy.. 
#I need clean more
#Later i also forget what i'm reading LOL






#This is such a joke code xd cumsum~ cum cum
#cardValCounts = [deck.count(val) for val in cardVal]
#if debug:
#    print(f'Card value counts: {cardValCounts}')
#    print(f'Cumulative card value counts: {np.cumsum(cardValCounts)}')
