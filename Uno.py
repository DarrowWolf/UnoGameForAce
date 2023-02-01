import random
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
                deck.append((j,i))
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

        

# Create a list of players
players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]

# Create a deck of cards
deck = Deck.create_deck()

debug = True
if debug:

    #To Test discard pile and print the player hand whose card has been discarded 
    #'0' is player 1, '1' is player 2 and so on. Default is '0'.
    choose_player = 0

    print(deck) #prints created deck

    print()
    print()

    # Shuffle the deck of cards
    Deck.shuffle_deck(deck)
    print(Deck.shuffle_deck(deck)) #prints shuffled deck

    print()
    print()
    # Deal cards to players
    players = Deck.deal_cards(deck, players)

    # Print the players' hands
    for player in players:
        print(f'{player.name} has the following cards:')
        for card in player.hand:
            print(f'\t{card}')
        print()

    print()
    print()

    discard_pile = DiscardPile()

    # Example test of the discard pile
    discarded_card = players[choose_player].hand.pop()
    discard_pile.add_to_pile(discarded_card)

    print(f'{players[choose_player].name} discarded {discarded_card}')
    print(f'Discard pile: {discard_pile.pile}')

    print()
    print()

    # Print the chosen player's hand
    print(f'{players[choose_player].name} has the following cards:')
    for card in players[choose_player].hand:
        print(f'\t{card}')
    print()
    

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
