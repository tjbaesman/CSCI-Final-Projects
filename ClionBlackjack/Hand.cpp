//
// Created by tj on 11/6/19.
//

#include "Hand.h"
#include <cstdlib>

Hand::Hand(vector<int>& deck, bool isTheDealer) {
    handSplit = false;

    funds = 500;
    currentBet = 0;
    isDealer = isTheDealer;
    acePresent = false;
    randHand(deck);
}

vector<int> Hand::getHand(){
    return cards;
}

int Hand::getBet() {
    return currentBet;
}

int Hand::getFunds() {
    return funds;
}

int Hand::getValue() {
    return value;
}

bool Hand::getAcePresent() {
    return acePresent;
}

void Hand::hit(vector<int>& deck) {
    bool cardChoiceUnmade = true;
    while(cardChoiceUnmade) {
        int card = rand() % 52 + 1;
        if (deck.at(card - 1) > 0) {
            deck.at(card - 1) -= 1;
            cards.push_back(card);
            if(!isDealer) {
                displayHand();
            }
            setValue();
            return;
        }
    }
}

void Hand::randHand(vector<int>& deck) {
    cards.clear();
    hit(deck);
    hit(deck);
}

void Hand::setFunds(int inputFunds) {
    funds = inputFunds;
}

void Hand::displayHand() {
    
}

void Hand::setBet(int inputBet) {
    currentBet = inputBet;
}

void Hand::setValue() {
    int tempValue = 0;
    for(int i = 0; i < cards.size(); i++) {
        switch (cards.at(i) % 13) {
            case 1:
                if(acePresent && (tempValue + 11 > 21)){
                    tempValue += 1;
                } else {
                    tempValue += 11;
                    acePresent = true;
                }
                break;
            case 2:
                tempValue += 2;
                break;
            case 3:
                tempValue += 3;
                break;
            case 4:
                tempValue += 4;
                break;
            case 5:
                tempValue += 5;
                break;
            case 6:
                tempValue += 6;
                break;
            case 7:
                tempValue += 7;
                break;
            case 8:
                tempValue += 8;
                break;
            case 9:
                tempValue += 9;
                break;
            case 0:
            case 10:
            case 11:
            case 12:
                tempValue += 10;
                break;
        }
        if(tempValue > 21 && acePresent) {
            tempValue -= 10;
            acePresent = false;
        }
    }
    acePresent = false;
    value = tempValue;
}

bool Hand::isBlackjack() {
    return (value == 21 && cards.size() == 2);
}

bool Hand::isBust() {
    return (value > 21);
}

bool Hand::canSplitHand() {
    return (((cards.at(0) % 13) == (cards.at(1) % 13)) && (cards.size() == 2));
}

void Hand::splitHand() {
    currentBet *= 2;
    split_cards.at(0).push_back(cards.at(0));
    split_cards.at(1).push_back(cards.at(1));
    handSplit = true;
}

bool Hand::canDoubleDown() {
    return (cards.size() == 2 && (value > 8) && (value < 12));
}

void Hand::doubleDown(vector<int>& deck) {
    currentBet *= 2;
    hit(deck);
}

void Hand::outputCards() {
    for(int i = 0; i < cards.size(); i++) {
        outputCard(i);
    }
    cout << endl;
}

void Hand::outputCard(int idx) {
    cout << "\nThe ";
    switch (cards.at(idx)) {
        case 1:
            cout << "Ace of Clubs";
            break;
        case 2:
            cout << "Two of Clubs";
            break;
        case 3:
            cout << "Three of Clubs";
            break;
        case 4:
            cout << "Four of Clubs";
            break;
        case 5:
            cout << "Five of Clubs";
            break;
        case 6:
            cout << "Six of Clubs";
            break;
        case 7:
            cout << "Seven of Clubs";
            break;
        case 8:
            cout << "Eight of Clubs";
            break;
        case 9:
            cout << "Nine of Clubs";
            break;
        case 10:
            cout << "Ten of Clubs";
            break;
        case 11:
            cout << "Jack of Clubs";
            break;
        case 12:
            cout << "Queen of Clubs";
            break;
        case 13:
            cout << "King of Clubs";
            break;
        case 14:
            cout << "Ace of Diamonds";
            break;
        case 15:
            cout << "Two of Diamonds";
            break;
        case 16:
            cout << "Three of Diamonds";
            break;
        case 17:
            cout << "Four of Diamonds";
            break;
        case 18:
            cout << "Five of Diamonds";
            break;
        case 19:
            cout << "Six of Diamonds";
            break;
        case 20:
            cout << "Seven of Diamonds";
            break;
        case 21:
            cout << "Eight of Diamonds";
            break;
        case 22:
            cout << "Nine of Diamonds";
            break;
        case 23:
            cout << "Ten of Diamonds";
            break;
        case 24:
            cout << "Jack of Diamonds";
            break;
        case 25:
            cout << "Queen of Diamonds";
            break;
        case 26:
            cout << "King of Diamonds";
            break;
        case 27:
            cout << "Ace of Hearts";
            break;
        case 28:
            cout << "Two of Hearts";
            break;
        case 29:
            cout << "Three of Hearts";
            break;
        case 30:
            cout << "Four of Hearts";
            break;
        case 31:
            cout << "Five of Hearts";
            break;
        case 32:
            cout << "Six of Hearts";
            break;
        case 33:
            cout << "Seven of Hearts";
            break;
        case 34:
            cout << "Eight of Hearts";
            break;
        case 35:
            cout << "Nine of Hearts";
            break;
        case 36:
            cout << "Ten of Hearts";
            break;
        case 37:
            cout << "Jack of Hearts";
            break;
        case 38:
            cout << "Queen of Hearts";
            break;
        case 39:
            cout << "King of Hearts";
            break;
        case 40:
            cout << "Ace of Spades";
            break;
        case 41:
            cout << "Two of Spades";
            break;
        case 42:
            cout << "Three of Spades";
            break;
        case 43:
            cout << "Four of Spades";
            break;
        case 44:
            cout << "Five of Spades";
            break;
        case 45:
            cout << "Six of Spades";
            break;
        case 46:
            cout << "Seven of Spades";
            break;
        case 47:
            cout << "Eight of Spades";
            break;
        case 48:
            cout << "Nine of Spades";
            break;
        case 49:
            cout << "Ten of Spades";
            break;
        case 50:
            cout << "Jack of Spades";
            break;
        case 51:
            cout << "Queen of Spades";
            break;
        case 52:
            cout << "King of Spades";
            break;
    }
    cout << endl;
}

void Hand::payout(Hand dealerHand) {
    cout << "The final value of your hand is " << getValue() << endl << endl;
    cout << "The dealer's final hand is:";
    dealerHand.outputCards();
    cout << "Its value is " << dealerHand.getValue() << endl << endl;
    if(isBust()) {
        funds -= currentBet;
    } else if(dealerHand.isBust()) {
        cout << "Dealer busts! Paying out.\n";
        funds += currentBet;
    } else if(getValue() > dealerHand.getValue()) {
        cout << "You win! Paying out.\n";
        funds += currentBet;
    } else if(getValue() == dealerHand.getValue()) {
        cout << "Stand off! You keep your coin.\n";
    } else {
        cout << "You lose! Collecting bets.\n";
        funds -= currentBet;
    }
}