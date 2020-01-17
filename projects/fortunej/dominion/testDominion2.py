# -*- coding: utf-8 -*-
"""
Created on January 15, 2020

@author: Julian Fortune (fortunej)
"""

import Dominion
import random
from collections import defaultdict

import testUtility

# Get player names
player_names = ["Annie", "*Ben"]

# Initial state
players = testUtility.create_players(player_names)
supply = testUtility.create_supply(len(player_names))
trash = []
turn  = 0

# Test scenario: 0 Players
players = []

#Play the game
while not Dominion.gameover(supply):
    turn += 1
    print("\r")
    for value in testUtility.supply_order:
        print (value)
        for stack in testUtility.supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)


#Final score
testUtility.score_game(players)