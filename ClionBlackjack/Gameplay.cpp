//
// Created by tj on 11/9/19.
//

#include "Gameplay.h"

void dealNewHands(Hand& playerHand, Hand& dealerHand, vector<int>& deck) {
    playerHand.randHand(deck);
    dealerHand.randHand(deck);
}

void choices(Hand& playerHand, Hand& dealerHand, vector<int>& deck) {
    bool choiceUnmade = true;
    char choice;

    cout << "\nYour hand is:";
    playerHand.outputCards();
    if(playerHand.getAcePresent()) {
        cout << "Its values are " << playerHand.getValue() << " and " << playerHand.getValue() - 10 << endl;
    } else {
        cout << "Its value is: " << playerHand.getValue() << endl;
    }

    if(playerHand.isBlackjack()) {
        cout << "Blackjack! Paying double bets\n";
        return;
    } else if(dealerHand.isBlackjack()) {
        cout << "Dealer has Blackjack! Too bad.\n";
        return;
    }

    if(playerHand.isBust() && !playerHand.getAcePresent()) {
        cout << "You Bust! Better luck next time." << endl;
        return;
    }

    // Output dealer's face-up card
    cout << "The dealer's face-up card is ";
    dealerHand.outputCard(1);

    cout << "\nYou can: (What to Enter)\nHit(H)\n";
    if(playerHand.canSplitHand()) {
        cout << "Split(S)\n";
    }
    if(playerHand.canDoubleDown()) {
        cout << "Double Down(D)\n";
    }
    cout << "Stand(N)\n";

    while(choiceUnmade) {
        cin >> choice;
        if(choice == 'H') {
            playerHand.hit(deck);
            choices(playerHand, dealerHand, deck);
            break;
        } else if(choice == 'S' && playerHand.canSplitHand()) {
            playerHand.splitHand();
            break;
        } else if(choice == 'D' && playerHand.canDoubleDown()) {
            playerHand.doubleDown(deck);
            return;
        } else if(choice == 'N') {
            return;
        } else {
            cout << "Invalid choice, try again\n";
        }
    }
}

void dealerChoices(Hand& dealerHand, vector<int>& deck) {
    while(dealerHand.getValue() < 17) {
        dealerHand.hit(deck);
    }
}


void makeBets(Hand& playerHand) {
    bool betChoiceUnmade = true;
    int tempBet = 0;
    cout << "\nYou have $" << playerHand.getFunds() << "\nHow much would you like to bet? (Whole numbers only) ";

    while(betChoiceUnmade) {
        cin >> tempBet;
        if (cin.fail() || tempBet <= 0) {
            cout << "Invalid input, try again\n" << endl;
            cin.clear();
            cin.get();
            continue;
        }
        if(tempBet > playerHand.getFunds()){
            cout << "Bet greater than available funds. Enter a bet that can be paid." << endl;
            continue;
        }
        betChoiceUnmade = false;
    }
    playerHand.setBet(tempBet);
}

bool endGame(Hand playerHand) {
    bool choiceUnmade = true;
    char endChar;
    cout << "Would you like to play another hand? (Y/N) ";
    while(choiceUnmade) {
        cin >> endChar;
        if(endChar == 'Y') {
            return true;
        } else if(endChar == 'N' || playerHand.getFunds() <= 0) {
            cout << "Thanks for playing!\n";
            return false;
        } else {
            cout << "Invalid input, try again\n";
        }
    }
}