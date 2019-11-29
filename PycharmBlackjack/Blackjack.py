# TJ Baesman
# CSCI 101 - Section D
# Explore Project - Blackjack

import Blackjack_Gameplay, time, random
from Blackjack_Hand import Hand

random.seed(time.monotonic())

deck = []
for i in range(52):
    deck.append(3)

player_hand = Hand(False)
dealer_hand = Hand(True)

print("Welcome to Blackjack!")
game_running = True
iterator = 0
while game_running:
    Blackjack_Gameplay.make_bets(player_hand)
    Blackjack_Gameplay.deal_new_hands(player_hand, dealer_hand, deck)
    Blackjack_Gameplay.choices(player_hand, dealer_hand, deck)
    Blackjack_Gameplay.dealer_choices(dealer_hand, deck)
    player_hand.payout(dealer_hand)
    game_running = Blackjack_Gameplay.end_game(player_hand)
    if iterator % 5 == 0:
        deck = []
        for i in range(52):
            deck.append(3)
    iterator += 1
print("Thanks for playing!")
