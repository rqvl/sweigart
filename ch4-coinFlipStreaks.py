# Coin Flip Streaks, from Chapter 4
#
# James // rqvl@runbox.com

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    
    # create current list of flips
    choices = ('H','T',)
    flip = []
    for i in range(100):
        flip.append(random.choice(choices))
    
    # check if there's a streak of 6 heads or 6 tails in a row
    s = ''
    for j in range(len(flip)):
        s += flip[j]
    if 'TTTTTT' in s or 'HHHHHH' in s:
        numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))