//
// Created by tj on 11/6/19.
//

#ifndef BLACKJACK_HAND_H
#define BLACKJACK_HAND_H

#include <vector>
#include <string>
#include <iostream>
#include <fstream>

using namespace std;

class Hand {
public:
    Hand(vector<int>& deck, bool isTheDealer);
    vector<int> getHand();
    int getFunds();
    int getBet();
    int getValue();
    bool getAcePresent();
    void hit(vector<int>& deck);
    void randHand(vector<int>& deck);
    void setFunds(int inputFunds);
    void setBet(int inputBet);
    void setValue();
    void displayHand();
    bool isBlackjack();
    bool isBust();
    bool canSplitHand();
    void splitHand();
    bool canDoubleDown();
    void doubleDown(vector<int>& deck);
    void outputCards();
    void outputCard(int idx);
    void payout(Hand dealerHand);

private:
    bool acePresent;
    bool handSplit;
    bool isDealer;
    vector<int> cards;
    vector<int> split_L;
    vector<int> split_R;
    string owner;
    string handFile;
    int value;
    int funds;
    int currentBet;
};


#endif //BLACKJACK_HAND_H
