# milestone project 2
import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,'Queen':10, 'King':10, 'Ace':11}

playing = True

### define classes ###
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                # create card
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        deck_comp = ""
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return f"The deck has: " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        if type(card) == list:
            self.cards.extend(card)
            for card in card:
                self.value += card.value
                if card.rank == "Ace":
                    self.aces += 1
            print(self.value)
        else:
            self.cards.append(card)
            self.value += card.value
            print(self.value)
            if card.rank == "Ace":
                self.aces += 1
    
    #def count_value(self):
     #   self.value = 0
      #  for card in self.cards:
       #     self.value += card.value
       # return self.value

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
        
    def __str__(self):
        return f"Player has {len(self.cards)}"

class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -+ self.bet

### define functions ###
def take_bet(bet_amount,chips_obj):
    try:    
        if bet_amount <= chips_obj.total:
            chips_obj.win_bet()
            print("werkt")
        else:
            print("bet amount is too damn high")
    except:
        print("the passed parameters are either not integers or not an chips object")

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        hitstand = input("Hit or Stand? H=Hit S=Stand")
        if hitstand == "H" or hitstand == "h":
            hit(deck,hand)
            break
        elif hitstand == "S" or hitstand == "s":
            playing = False
            break

def show_some(player,dealer):
    
    pass
    
def show_all(player,dealer):
    print(player)

def player_busts():
    pass

def player_wins():
    pass

def dealer_busts():
    pass
    
def dealer_wins():
    pass
    
def push():
    pass

###TEST
test_chips = Chips(500)
print(test_chips.total)
test_deck = Deck()
test_hand = Hand()

take_bet(200,test_chips)
hit_or_stand(test_deck,test_hand)
#test_card = Card("Diamonds","Three")
#print(test_card.value)

#test_deck = Deck()
#test_deck.shuffle()
#print(test_deck)
#test_hand = Hand()
#for eachcard in range(20):
#    test_hand.add_card(test_deck.deal())

#print(test_hand.aces)

#test_deck.shuffle()

#test_deal = test_deck.deal()

while playing:
    break