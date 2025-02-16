from random import randint
from IPython.display import clear_output

class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ("Spades", "Hearts", "Diamond", "Clubs")
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A")
    
    def makeDeck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    def pullCard(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))

class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def addCard(self, card):
        self.hand.append(card)

    def showHand(self, dealer_start = True):
        print(f"\n{self.name}")
        print("===============")
        for i in range(len(self.hand)):
            if self.name == "Dealer" and i == 0 and dealer_start:
                print(" - of - ")
            else:
                card = self.hand[i]
                print(f"{card[0]} of {card[1]}")

        print(f"Total = {self.calcHand(dealer_start)}")

    def calcHand(self, dealer_start = True):
        total = 0
        aces = 0 
        card_values = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8, 9:9, 10:10, "J":10, "Q":10, "K":10, "A":11}
        if self.name == "Dealer" and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        
        for card in self.hand:
            if card[0] == "A":
                aces += 1
            else:
                total += card_values[card[0]]

        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11

        return total


game = Blackjack()
game.makeDeck()
player = Player(input("What's your name?"))
dealer = Player("Dealer")

for i in range(2):
    player.addCard(game.pullCard())
    dealer.addCard(game.pullCard())

player.showHand()
dealer.showHand()

player_bust = False
while input("Would you like to stay or hit?").lower() != "stay":
    clear_output()
    player.addCard(game.pullCard())

    player.showHand()
    dealer.showHand()

    if player.calcHand() > 21:
        player_bust = True
        print("You loser!")
        break

dealer_bust = False
if not player_bust:
    while dealer.calcHand(False) < 17:
        dealer.addCard(game.pullCard())

        if dealer.calcHand(False) > 21:
            dealer_bust = True
            print("F*cking Winner!")
            break

clear_output()
player.showHand()
dealer.showHand(False)

if player_bust:
    print("You busted fella! better luck next time!")
elif dealer_bust:
    print("Massive win fella!, The loser dealer busted!")
elif dealer.calcHand(False) > player.calcHand():
    print("Dealer has higher cards, you lose!")
elif dealer.calcHand(False) < player.calcHand():
    print("You beat the dealer! Congrats!")
else:
    print("You pushed, no one wins!")