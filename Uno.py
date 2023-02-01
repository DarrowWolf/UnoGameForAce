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

class DiscardPile:
    def __init__(self):
        self.pile = []

    def add_to_pile(self, card):
        self.pile.append(card)

# Create a list of players
players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]

# Create a deck of cards
deck = Deck.create_deck()

debug = True
if debug:
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
    discarded_card = players[0].hand.pop()
    discard_pile.add_to_pile(discarded_card)

    print(f'{players[0].name} discarded {discarded_card}')
    print(f'Discard pile: {discard_pile.pile}')

    print()
    print()

    # Print the chosen player's hand
    print(f'{players[0].name} has the following cards:')
    for card in players[0].hand:
        print(f'\t{card}')
    print()
    

else:
    print("Change Debug setting from \"False\" to \"True\" if you want to see debug output")


















#This is such a joke code xd cumsum~ cum cum
#cardValCounts = [deck.count(val) for val in cardVal]
#if debug:
#    print(f'Card value counts: {cardValCounts}')
#    print(f'Cumulative card value counts: {np.cumsum(cardValCounts)}')
