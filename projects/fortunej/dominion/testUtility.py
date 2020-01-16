# -*- coding: utf-8 -*-
"""
Created on January 15, 2020

@author: Julian Fortune (fortunej)
"""

import Dominion
import random
from collections import defaultdict

# All cards in box mapped by price
supply_order = {0:['Curse','Copper'],
                2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],
                8:['Province']}

def number_of_victory_cards(player_count):
    if player_count > 2:
        return 12
    else:
        return 8

def number_of_curse_cards(player_count):
    return -10 + 10 * player_count

def create_box(player_count):
    box = {}

    box["Woodcutter"]=[Dominion.Woodcutter()]*10
    box["Smithy"]=[Dominion.Smithy()]*10
    box["Laboratory"]=[Dominion.Laboratory()]*10
    box["Village"]=[Dominion.Village()]*10
    box["Festival"]=[Dominion.Festival()]*10
    box["Market"]=[Dominion.Market()]*10
    box["Chancellor"]=[Dominion.Chancellor()]*10
    box["Workshop"]=[Dominion.Workshop()]*10
    box["Moneylender"]=[Dominion.Moneylender()]*10
    box["Chapel"]=[Dominion.Chapel()]*10
    box["Cellar"]=[Dominion.Cellar()]*10
    box["Remodel"]=[Dominion.Remodel()]*10
    box["Adventurer"]=[Dominion.Adventurer()]*10
    box["Feast"]=[Dominion.Feast()]*10
    box["Mine"]=[Dominion.Mine()]*10
    box["Library"]=[Dominion.Library()]*10
    box["Gardens"]=[Dominion.Gardens()]*number_of_victory_cards(player_count)
    box["Moat"]=[Dominion.Moat()]*10
    box["Council Room"]=[Dominion.Council_Room()]*10
    box["Witch"]=[Dominion.Witch()]*10
    box["Bureaucrat"]=[Dominion.Bureaucrat()]*10
    box["Militia"]=[Dominion.Militia()]*10
    box["Spy"]=[Dominion.Spy()]*10
    box["Thief"]=[Dominion.Thief()]*10
    box["Throne Room"]=[Dominion.Throne_Room()]*10

    return box

def create_supply(player_count):
    box = create_box(player_count)

    #Pick 10 cards from box to be in the supply.
    boxlist = [k for k in box]
    random.shuffle(boxlist)
    random10 = boxlist[:10]

    supply = defaultdict(list,[(k,box[k]) for k in random10])

    #The supply always has these cards
    supply["Copper"]=[Dominion.Copper()]*(60-player_count*7)
    supply["Silver"]=[Dominion.Silver()]*40
    supply["Gold"]=[Dominion.Gold()]*30
    supply["Estate"]=[Dominion.Estate()]*number_of_victory_cards(player_count)
    supply["Duchy"]=[Dominion.Duchy()]*number_of_victory_cards(player_count)
    supply["Province"]=[Dominion.Province()]*number_of_victory_cards(player_count)
    supply["Curse"]=[Dominion.Curse()]*number_of_curse_cards(player_count)

    return supply

def create_players(player_names):
    players = []

    for name in player_names:
        if name[0]=="*":
            players.append(Dominion.ComputerPlayer(name[1:]))
        elif name[0]=="^":
            players.append(Dominion.TablePlayer(name[1:]))
        else:
            players.append(Dominion.Player(name))

    return players
