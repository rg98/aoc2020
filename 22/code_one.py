#!/usr/bin/env python3.9

from collections import deque

def play_round(player_one, player_two):
    card_1 = player_one.popleft()
    card_2 = player_two.popleft()
    if card_1 > card_2:
        player_one.append(card_1)
        player_one.append(card_2)
    else:
        player_two.append(card_2)
        player_two.append(card_1)

def score(player):
    score = 0
    factor = 1
    while len(player) > 0:
        score += factor * player.pop()
        factor += 1
    return score

# Read decks
deck_one = deque()
deck_two = deque()
with open('in.txt', 'r') as fd:
    for line in fd:
        if line.startswith('Player 1'):
            for card in fd:
                if len(card) > 1:
                    deck_one.append(int(card[:-1]))
                else:
                    break
        elif line.startswith('Player 2'):
            for card in fd:
                if len(card) > 1:
                    deck_two.append(int(card[:-1]))
                else:
                    break

while len(deck_one) > 0 and len(deck_two) > 0:
    play_round(deck_one, deck_two)

if len(deck_one) > 0:
    print(f"Player one wins with a score of {score(deck_one)}")
else:
    print(f"Player two wins with a score of {score(deck_two)}")
