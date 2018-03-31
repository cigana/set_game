# -*- coding: utf-8 -*-
"""
Created on Sat Mar 31 12:16:54 2018

@author: cigana
"""
import itertools
from pprint import pprint
import random
import re


a = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
deck = set(itertools.permutations(a, 4))
print(len(deck))

print((1,1,1,1) in deck)

deck_list = list(deck)
#deck_list.sort()
random.shuffle(deck_list)


# Das erste Mal 12 Karten aufdecken
cards_on_display = []

i = 0
while i < 12:
    cards_on_display += [deck_list.pop()]
    i = i+1
    
# Der verbleibende Kartenstapel wird runtergezählt 
# (d.h. Karten werden daraus entfernt)
print(len(deck_list))    
pprint(cards_on_display)

# zeigt die 3 gewählten Karten 
def group_cards(sample, choice):
    # wandelt choice-string in index um
    index = [int(s) for s in re.findall(r'\d+', choice)]
    
    triple = []
    for i in index:
        triple += [sample[i]]
    return triple
    

def is_set(three_cards):
    true = 1
    while true:
        if three_cards[0][0] == three_cards[1][0] and three_cards [0][0] != three_cards[2][0]:
            true = 0
        elif three_cards[0][0] == three_cards[1][0] and three_cards [1][0] != three_cards[2][0]:
            true = 0    
        elif three_cards[0][0] != three_cards[1][0] and three_cards [0][0] == three_cards[2][0]:
            true = 0
        elif three_cards[0][0] != three_cards[1][0] and three_cards [1][0] == three_cards[2][0]:
            true = 0              
                
        if three_cards[0][1] == three_cards[1][1] and three_cards [0][1] != three_cards[2][1]:
            true = 0
        elif three_cards[0][1] == three_cards[1][1] and three_cards [1][1] != three_cards[2][1]:
            true = 0
        elif three_cards[0][1] != three_cards[1][1] and three_cards [0][1] == three_cards[2][1]:
            true = 0
        elif three_cards[0][1] != three_cards[1][1] and three_cards [1][1] == three_cards[2][1]:
            true = 0
            
        if three_cards[0][2] == three_cards[1][2] and three_cards [0][2] != three_cards[2][2]:
            true = 0
        elif three_cards[0][2] == three_cards[1][2] and three_cards [1][2] != three_cards[2][2]:
            true = 0
        elif three_cards[0][2] != three_cards[1][2] and three_cards [0][2] == three_cards[2][2]:
            true = 0
        elif three_cards[0][2] != three_cards[1][2] and three_cards [1][2] == three_cards[2][2]:
            true = 0
            
        if three_cards[0][3] == three_cards[1][3] and three_cards [0][3] != three_cards[2][3]:
            true = 0
        elif three_cards[0][3] == three_cards[1][3] and three_cards [1][3] != three_cards[2][3]:
            true = 0
        elif three_cards[0][3] != three_cards[1][3] and three_cards [0][3] == three_cards[2][3]:
            true = 0
        elif three_cards[0][3] != three_cards[1][3] and three_cards [1][3] == three_cards[2][3]:
            true = 0
        
        is_set = "Nooooope"
        
        if true == 1:
            is_set = "You've found a set"
            true = 0           

    return is_set
    
def find_set(sample):
    
    for card1 in sample:
        for card2 in sample:
            if card1 != card2:
                if card1[0] == card2[0]:
                    a = card1[0]
                elif card1[0] != card2[0]:
                    a = 6 - card1[0] - card2[0]
                if card1[1] == card2[1]:
                    b = card1[1]
                elif card1[1] != card2[1]:
                    b = 6 - card1[1] - card2[1]
                if card1[2] == card2[2]:
                    c = card1[2]
                elif card1[2] != card2[2]:
                    c = 6 - card1[2] - card2[2]
                if card1[3] == card2[3]:
                    d = card1[3]
                elif card1[3] != card2[3]:
                    d = 6 - card1[3] - card2[3]
                
                card3 = (a, b, c, d)
                
                if card3 in sample:
                    print(card1, card2, card3) # macht er 6x für jedes Set
    pass

find_set(cards_on_display)

choice = input('Choose 3 cards: ')
test = group_cards(cards_on_display, choice)
print(is_set(test))

choice = input('Choose 3 cards: ')
test = group_cards(cards_on_display, choice)
print(is_set(test))

choice = input('Choose 3 cards: ')
test = group_cards(cards_on_display, choice)
print(is_set(test))

choice = input('Choose 3 cards: ')
test = group_cards(cards_on_display, choice)
print(is_set(test))


    