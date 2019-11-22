# TJ Baesman
# CSCI 101 - Section D
# Blackjack - Gameplay functions

from Blackjack_Hand import Hand


def deal_new_hands(player_hand, dealer_hand, deck):
    player_hand.rand_hand(deck)
    dealer_hand.rand_hand(deck)


def make_bets(player_hand):
    bet_choice_unmade = True
    print("You have $%d" % player_hand.funds)
    temp_bet = int(input("How much would you like to bet? (Whole numbers only) "))
    while bet_choice_unmade:
        if temp_bet <= 0:
            print("Invalid input, try again")
            continue
        if temp_bet > player_hand.funds:
            print("Bet greater than available funds. Enter a bet that can be paid.")
            temp_bet = int(input("How much would you like to bet? (Whole numbers only) "))
            continue
        bet_choice_unmade = False
    player_hand.current_bet = temp_bet


def choices(player_hand, dealer_hand, deck):
    choice_unmade = True

    print()
    print("Your hand is:")
    player_hand.output_cards()
    if player_hand.ace_present:
        print("Its values are %d and %d" % (player_hand.value, player_hand.value - 10))
    else:
        print("Its value is: %d" % player_hand.value)
    print()

    if player_hand.is_blackjack():
        print("Blackjack! Paying double bets")
        return
    elif dealer_hand.is_blackjack():
        print("Dealer has Blackjack! Too bad.")
        return

    if player_hand.is_bust() and not player_hand.ace_present:
        print("You Bust! Better luck next time.")
        return

    print("The dealer has:")
    dealer_hand.display_hand()
    print("The dealer's visible hand is ")
    dealer_hand.output_card(dealer_hand.cards[1])
    print()

    print("You can: (What to Enter)\nHit(H)")
    if player_hand.can_split_hand():
        print("Split(S)")
    if player_hand.can_double_down():
        print("Double Down(D)")
    print("Stand(N)")

    while choice_unmade:
        choice = input()
        if choice == "H":
            player_hand.hit(deck)
            choices(player_hand, dealer_hand, deck)
            break
        elif choice == "S" and player_hand.can_split_hand():
            player_hand.split_hand()
            break
        elif choice == "D" and player_hand.can_double_down():
            player_hand.double_down()
            return
        elif choice == "N":
            return
        else:
            print("Invalid choice, try again")


def dealer_choices(dealer_hand, deck):
    while dealer_hand.value < 17:
        dealer_hand.hit(deck)


def end_game(player_hand):
    choice_unmade = True
    while choice_unmade:
        end_char = input("Would you like to play another hand? (Y/N)")
        if end_char == "Y":
            return True
        elif end_char == "N" or player_hand.funds <= 0:
            print("Thanks for playing")
            return False
        else:
            print("Invalid input, try again")
