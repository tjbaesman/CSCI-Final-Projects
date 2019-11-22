cmake_minimum_required(VERSION 3.14)
project(Blackjack)

set(CMAKE_CXX_STANDARD 14)

add_executable(Blackjack main.cpp Hand.cpp Hand.h Gameplay.cpp Gameplay.h)