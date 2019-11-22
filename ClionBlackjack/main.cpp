/*
 * Author: TJ Baesman
 * CSCI 261 - Section B
 * Final Project
 * Blackjack
 */

#include "Gameplay.h"
#include <ctime>

int main() {

    srand(time(0));
    rand();

    // Create full deck of cards (possibly multiple)
    const int NUM_DECKS = 3;
    vector<int> deck(52);
    for(int i = 0; i < 52; i++){
        deck.at(i) = NUM_DECKS;
    }

    Hand dealerHand(deck, true);

    Hand playerHand(deck, false);

    bool gameRunning = true;
    while(gameRunning) {
        makeBets(playerHand);
        dealNewHands(playerHand, dealerHand, deck);
        choices(playerHand, dealerHand, deck);
        dealerChoices(dealerHand, deck);
        playerHand.payout(dealerHand);
        gameRunning = endGame(playerHand);
    }

    return 0;
}