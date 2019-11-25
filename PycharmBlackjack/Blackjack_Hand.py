# TJ Baesman
# CSCI 101 - Section D
# Blackjack - Hand Class
import random
from Blackjack_Gameplay import *


class Hand:

    def __init__(self, dealer_status):
        self.ace_present = False
        self.ace_present_L = False
        self.ace_present_R = False
        self.hand_split = False
        self.hand_side = "L"
        self.is_dealer = dealer_status
        self.cards = []
        self.split_L = []
        self.split_R = []
        self.value = 0
        self.value_L = 0
        self.value_R = 0
        self.funds = 500
        self.current_bet = 0

    def hit(self, deck):
        card_choice_unmade = True
        while card_choice_unmade:
            card = random.randint(1, 52)
            if deck[card - 1] > 0:
                deck[card - 1] -= 1
                if not self.hand_split:
                    self.cards.append(card)
                elif self.hand_side == "L":
                    self.split_L.append(card)
                else:
                    self.split_R.append(card)
                self.set_value()
                return

    def rand_hand(self, deck):
        self.cards = []
        self.split_L = []
        self.split_R = []
        self.hit(deck)
        self.hit(deck)
        if not self.is_dealer:
            print()
            print("Your Deal:")
            self.display_hand()

    def set_value(self):
        if not self.hand_split:
            temp_value = 0
            for i in self.cards:
                if i % 13 == 1:
                    if self.ace_present and (temp_value + 11 > 21):
                        temp_value += 1
                    else:
                        temp_value += 11
                        self.ace_present = True
                elif i % 13 == 2:
                    temp_value += 2
                elif i % 13 == 3:
                    temp_value += 3
                elif i % 13 == 4:
                    temp_value += 4
                elif i % 13 == 5:
                    temp_value += 5
                elif i % 13 == 6:
                    temp_value += 6
                elif i % 13 == 7:
                    temp_value += 7
                elif i % 13 == 8:
                    temp_value += 8
                elif i % 13 == 9:
                    temp_value += 9
                else:
                    temp_value += 10
                if temp_value > 21 and self.ace_present:
                    temp_value -= 10
                    self.ace_present = False
            self.ace_present = False
            self.value = temp_value
        else:
            temp_value = 0
            for i in self.split_L:
                if i % 13 == 1:
                    if self.ace_present_L and (temp_value + 11 > 21):
                        temp_value += 1
                    else:
                        temp_value += 11
                        self.ace_present_L = True
                elif i % 13 == 2:
                    temp_value += 2
                elif i % 13 == 3:
                    temp_value += 3
                elif i % 13 == 4:
                    temp_value += 4
                elif i % 13 == 5:
                    temp_value += 5
                elif i % 13 == 6:
                    temp_value += 6
                elif i % 13 == 7:
                    temp_value += 7
                elif i % 13 == 8:
                    temp_value += 8
                elif i % 13 == 9:
                    temp_value += 9
                else:
                    temp_value += 10
                if temp_value > 21 and self.ace_present_L:
                    temp_value -= 10
                    self.ace_present_L = False
            self.ace_present_L = False
            self.value_L = temp_value

            temp_value = 0
            for i in self.split_R:
                if i % 13 == 1:
                    if self.ace_present_R and (temp_value + 11 > 21):
                        temp_value += 1
                    else:
                        temp_value += 11
                        self.ace_present_R = True
                elif i % 13 == 2:
                    temp_value += 2
                elif i % 13 == 3:
                    temp_value += 3
                elif i % 13 == 4:
                    temp_value += 4
                elif i % 13 == 5:
                    temp_value += 5
                elif i % 13 == 6:
                    temp_value += 6
                elif i % 13 == 7:
                    temp_value += 7
                elif i % 13 == 8:
                    temp_value += 8
                elif i % 13 == 9:
                    temp_value += 9
                else:
                    temp_value += 10
                if temp_value > 21 and self.ace_present_R:
                    temp_value -= 10
                    self.ace_present_R = False
            self.ace_present_R = False
            self.value_R = temp_value

    def display_hand(self):

        values = {
            1: "A",
            2: "2",
            3: "3",
            4: "4",
            5: "5",
            6: "6",
            7: "7",
            8: "8",
            9: "9",
            10: "10",
            11: "J",
            12: "Q",
            0: "K"
        }

        symbols = {
            0: "♣",
            1: "♦",
            2: "♥",
            3: "♠"
        }

        read_blank_card = open("blank_ascii_card.txt", "r")
        read_back_card = open("back_ascii_card.txt", "r")
        for i in range(7):
            blank_card_line = read_blank_card.readline()[:-1]
            back_card_line = read_back_card.readline()[:-1]

            if not self.hand_split:
                for j in range(len(self.cards)):
                    if self.is_dealer and j == 0:
                        print(back_card_line, end=' ')
                    else:
                        if i == 1:
                            if len(values[self.cards[j] % 13]) == 1:
                                print(blank_card_line.format(values[self.cards[j] % 13], " "), end=' ')
                            else:
                                print(blank_card_line.format(values[self.cards[j] % 13], ""), end=' ')
                        elif i == 3:
                            print(blank_card_line.format(symbols[(self.cards[j] - 1) // 13]), end=' ')
                        elif i == 5:
                            if len(values[self.cards[j] % 13]) == 1:
                                print(blank_card_line.format(" ", values[self.cards[j] % 13]), end=' ')
                            else:
                                print(blank_card_line.format(values[self.cards[j] % 13], ""), end=' ')
                        else:
                            print(blank_card_line.format(), end=' ')
            else:
                for j in range(len(self.split_L)):
                    if i == 1:
                        if len(values[self.split_L[j] % 13]) == 1:
                            print(blank_card_line.format(values[self.split_L[j] % 13], " "), end=' ')
                        else:
                            print(blank_card_line.format(values[self.split_L[j] % 13], ""), end=' ')
                    elif i == 3:
                        print(blank_card_line.format(symbols[(self.split_L[j] - 1) // 13]), end=' ')
                    elif i == 5:
                        if len(values[self.split_L[j] % 13]) == 1:
                            print(blank_card_line.format(" ", values[self.split_L[j] % 13]), end=' ')
                        else:
                            print(blank_card_line.format(values[self.split_L[j] % 13], ""), end=' ')
                    else:
                        print(blank_card_line.format(), end=' ')

                print(end='\t\t')

                for j in range(len(self.split_R)):
                    if i == 1:
                        if len(values[self.split_R[j] % 13]) == 1:
                            print(blank_card_line.format(values[self.split_R[j] % 13], " "), end=' ')
                        else:
                            print(blank_card_line.format(values[self.split_R[j] % 13], ""), end=' ')
                    elif i == 3:
                        print(blank_card_line.format(symbols[(self.split_R[j] - 1) // 13]), end=' ')
                    elif i == 5:
                        if len(values[self.split_R[j] % 13]) == 1:
                            print(blank_card_line.format(" ", values[self.split_R[j] % 13]), end=' ')
                        else:
                            print(blank_card_line.format(values[self.split_R[j] % 13], ""), end=' ')
                    else:
                        print(blank_card_line.format(), end=' ')
            print()
        read_blank_card.close()

    def is_blackjack(self):
        return self.value == 21 and len(self.cards) == 2

    def is_bust(self):
        if not self.hand_split:
            return self.value > 21
        elif self.hand_side == "L":
            return self.value_L > 21
        elif self.hand_side == "R":
            return self.value_R > 21

    def can_split_hand(self):
        return self.cards[0] % 13 == self.cards[1] % 13 and len(self.cards) == 2 and self.current_bet * 2 <= self.funds

    def split_hand(self):
        self.hand_split = True
        self.split_L.append(self.cards[0])
        self.split_R.append(self.cards[1])
        self.cards = []
        self.set_value()

    def can_double_down(self):
        return 8 < self.value < 12 and len(self.cards) == 2 and self.current_bet * 2 <= self.funds

    def double_down(self, deck):
        self.current_bet *= 2
        self.hit(deck)
        self.display_hand()

    def output_cards(self):
        if not self.hand_split:
            for i in self.cards:
                self.output_card(i)
        else:
            print("Left:")
            for i in self.split_L:
                self.output_card(i)
            print("Right:")
            for i in self.split_R:
                self.output_card(i)

    def output_card(self, idx):
        print("The ", end='')
        if idx == 1:
            print("Ace of Clubs")
        elif idx == 2:
            print("Two of Clubs")
        elif idx == 3:
            print("Three of Clubs")
        elif idx == 4:
            print("Four of Clubs")
        elif idx == 5:
            print("Five of Clubs")
        elif idx == 6:
            print("Six of Clubs")
        elif idx == 7:
            print("Seven of Clubs")
        elif idx == 8:
            print("Eight of Clubs")
        elif idx == 9:
            print("Nine of Clubs")
        elif idx == 10:
            print("Ten of Clubs")
        elif idx == 11:
            print("Jack of Clubs")
        elif idx == 12:
            print("Queen of Clubs")
        elif idx == 13:
            print("King of Clubs")
        elif idx == 14:
            print("Ace of Diamonds")
        elif idx == 15:
            print("Two of Diamonds")
        elif idx == 16:
            print("Three of Diamonds")
        elif idx == 17:
            print("Four of Diamonds")
        elif idx == 18:
            print("Five of Diamonds")
        elif idx == 19:
            print("Six of Diamonds")
        elif idx == 20:
            print("Seven of Diamonds")
        elif idx == 21:
            print("Eight of Diamonds")
        elif idx == 22:
            print("Nine of Diamonds")
        elif idx == 23:
            print("Ten of Diamonds")
        elif idx == 24:
            print("Jack of Diamonds")
        elif idx == 25:
            print("Queen of Diamonds")
        elif idx == 26:
            print("King of Diamonds")
        elif idx == 27:
            print("Ace of Hearts")
        elif idx == 28:
            print("Two of Hearts")
        elif idx == 29:
            print("Three of Hearts")
        elif idx == 30:
            print("Four of Hearts")
        elif idx == 31:
            print("Five of Hearts")
        elif idx == 32:
            print("Six of Hearts")
        elif idx == 33:
            print("Seven of Hearts")
        elif idx == 34:
            print("Eight of Hearts")
        elif idx == 35:
            print("Nine of Hearts")
        elif idx == 36:
            print("Ten of Hearts")
        elif idx == 37:
            print("Jack of Hearts")
        elif idx == 38:
            print("Queen of Hearts")
        elif idx == 39:
            print("King of Hearts")
        elif idx == 40:
            print("Ace of Spades")
        elif idx == 41:
            print("Two of Spades")
        elif idx == 42:
            print("Three of Spades")
        elif idx == 43:
            print("Four of Spades")
        elif idx == 44:
            print("Five of Spades")
        elif idx == 45:
            print("Six of Spades")
        elif idx == 46:
            print("Seven of Spades")
        elif idx == 47:
            print("Eight of Spades")
        elif idx == 48:
            print("Nine of Spades")
        elif idx == 49:
            print("Ten of Spades")
        elif idx == 50:
            print("Jack of Spades")
        elif idx == 51:
            print("Queen of Spades")
        elif idx == 52:
            print("King of Spades")

    def payout(self, dealer_hand):
        print("The final value of your hand is", self.value, end="\n\n")
        print("The dealer's final hand is:")
        dealer_hand.display_hand()
        dealer_hand.output_cards()
        print("Its value is", dealer_hand.value, end="\n\n")
        if self.is_blackjack():
            self.funds += self.current_bet*2
        elif self.hand_split:
            bet_mod = 0
            if self.is_bust() or self.value_L < dealer_hand.value:
                print("Your left hand loses! Paying out.")
                bet_mod -= 1
            elif self.value_L == dealer_hand.value:
                print("Your left hand stands off! You keep your coin.")
            else:
                print("Your left hand wins! Paying out.")
                bet_mod += 1
            self.hand_side = "R"
            if self.is_bust() or self.value_R:
                print("Your right hand loses! Paying out.")
                bet_mod -= 1
            elif self.value_R == dealer_hand.value:
                print("Your right hand stands off! You keep your coin.")
            else:
                print("Your right hand wins! Paying out.")
                bet_mod += 1
            self.hand_side = "L"
        elif self.is_bust():
            self.funds -= self.current_bet
        elif dealer_hand.is_bust():
            print("Dealer busts! Paying out.")
            self.funds += self.current_bet
        elif self.value > dealer_hand.value:
            print("You win! Paying out.")
            self.funds += self.current_bet
        elif self.value == dealer_hand.value:
            print("Stand off! You keep your coin.")
        else:
            print("You lose! Collecting bets.")
            self.funds -= self.current_bet
        self.hand_split = False
