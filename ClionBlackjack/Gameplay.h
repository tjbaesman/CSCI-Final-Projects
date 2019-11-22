//
// Created by tj on 11/9/19.
//

#ifndef BLACKJACK_GAMEPLAY_H
#define BLACKJACK_GAMEPLAY_H

#include "Hand.h"

void dealNewHands(Hand& playerHand, Hand& dealerHand, vector<int>& deck);
void choices(Hand& playerHand, Hand& dealerHand, vector<int>& deck);
void splitChoices(Hand& playerHand, vector<int>& deck);
void dealerChoices(Hand& dealerHand, vector<int>& deck);
void makeBets(Hand& playerHand);
bool endGame(Hand playerHand);

#endif //BLACKJACK_GAMEPLAY_H
