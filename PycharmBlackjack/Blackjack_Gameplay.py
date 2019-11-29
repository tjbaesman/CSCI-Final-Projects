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
    while bet_choice_unmade:
        temp_bet = input("How much would you like to bet? (Whole numbers only) ")
        if temp_bet.isdigit():
            temp_bet = int(temp_bet)
        else:
            print("Invalid input, try again")
            continue
        if temp_bet <= 0:
            print("Invalid input, try again")
            continue
        if temp_bet > player_hand.funds:
            print("Bet greater than available funds. Enter a bet that can be paid.")
            continue
        bet_choice_unmade = False
    player_hand.current_bet = temp_bet


def choices(player_hand, dealer_hand, deck):
    choice_unmade = True

    print()
    print("Your hand is:")
    player_hand.display_hand()

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
    print()

    print("What would you like to do with your hand?")
    print("Your options: (What to Enter)\nHit(H)")
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
            split_choices(player_hand, dealer_hand, deck)
            break
        elif choice == "D" and player_hand.can_double_down():
            player_hand.double_down(deck)
            return
        elif choice == "N":
            return
        else:
            print("Invalid choice, try again")


def dealer_choices(dealer_hand, deck):
    while dealer_hand.value < 17:
        dealer_hand.hit(deck)


def split_choices(player_hand, dealer_hand, deck):
    choice_unmade = True

    print()
    print("Your hand is:")
    player_hand.display_hand()

    if player_hand.ace_present_L:
        print("The left hand's values are %d and %d" % (player_hand.value_L, player_hand.value_L - 10))
    else:
        print("The left hand's value is: %d" % player_hand.value_L)
    print()

    if player_hand.ace_present_R:
        print("The right hand's values are %d and %d" % (player_hand.value_R, player_hand.value_R - 10))
    else:
        print("The right hand's value is: %d" % player_hand.value_R)
    print()

    if player_hand.is_bust():
        if player_hand.hand_side == "L":
            print("Your left hand Busts! Better luck next time.")
            player_hand.hand_side = "R"
            split_choices(player_hand, dealer_hand, deck)
        else:
            print("Your right hand Busts! Better luck next time.")
            player_hand.hand_side = "L"
            return

    print("The dealer has:")
    dealer_hand.display_hand()
    print()

    if player_hand.hand_side == "L":
        print("What would you like to do with your left hand?")
    else:
        print("What would you like to do with your right hand?")

    print("Your options: (What to Enter)\nHit(H)\nStand(N)")

    while choice_unmade:
        choice = input()
        if choice == "H":
            player_hand.hit(deck)
            split_choices(player_hand, dealer_hand, deck)
            break
        elif choice == "N":
            if player_hand.hand_side == "L":
                player_hand.hand_side = "R"
                split_choices(player_hand, dealer_hand, deck)
            else:
                player_hand.hand_side = "L"
            return
        else:
            print("Invalid choice, try again")


def end_game(player_hand):
    if player_hand.funds <= 0:
        print("You're out!")
        return False

    choice_unmade = True
    while choice_unmade:
        end_char = input("Would you like to play another hand? (Y/N)")
        if end_char == "Y":
            return True
        elif end_char == "N":
            return False
        else:
            print("Invalid input, try again")
