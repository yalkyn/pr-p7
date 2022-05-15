import random
import time
import os
import math
import sys


## Constant vars
import defines
sg_system_number = defines.SYSTEM_AMOUNT
sg_conns = defines.MAX_CONNECTIONS


## Other info
ship_index = [["TEST SHIP", "TEST SHIP"]]


## Player info
p_current_system = 3
p_balance = 2500
p_current_ship = 0



# Sysgen
sg_syllables = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def generate_systems(syllables, amount):
    system_overlist = []
    ed = len(syllables)
    for k in range(amount):
        system = ''
        for i in range(random.randint(3, 6)):
            system += syllables[random.randint(0, ed - 1)]
        system_overlist.append(system)
    return system_overlist

c_system_names = generate_systems(sg_syllables, sg_system_number)

def connect_systems(system_list):
    amount = len(system_list)
    connections_overlist = []
    for k in range(amount):
        sysl = []
        connections_overlist.append(sysl)
    for w in range(2):
        for i in range(amount):
            td = random.randint(0, amount - 1)
            if td == i:
                pass
            else:
                if td in connections_overlist[i]:
                    pass
                else:
                    connections_overlist[i].append(td)
                    connections_overlist[td].append(i)

    return connections_overlist



def handle_input():
    ln = str(input())
    if ln[0] == "!":
        if ln[1] == "l":
            print("Your current system is", 

c_system_connections = connect_systems(c_system_names))
