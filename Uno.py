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

# Create a list of players
players = [Player("Player 1"), Player("Player 2"), Player("Player 3"), Player("Player 4")]

# Create a deck of cards
deck = Deck.create_deck()
print(deck) #prints created deck

print()
print()
print()
print()

# Shuffle the deck of cards
Deck.shuffle_deck(deck)
print(Deck.shuffle_deck(deck)) #prints shuffled deck

print()
print()
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

debug = True
cardValCounts = [deck.count(val) for val in cardVal]
if debug:
    print(f'Card value counts: {cardValCounts}')
    print(f'Cumulative card value counts: {np.cumsum(cardValCounts)}')
