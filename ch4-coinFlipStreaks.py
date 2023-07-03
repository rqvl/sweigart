# Coin Flip Streaks, from Chapter 4
#
# James // rqvl@runbox.com

import random
numberOfStreaks = 0
for experimentNumber in range(10000):
    
    # create current list of flips
    flip = []
    for i in range(100):
        flip.append(random.randint(0,1))
    
    # check if there's a streak of 6 heads or 6 tails in a row
    s = ''
    for j in range(len(flip)):
        s += str(flip[j])
        
    if '000000' in s or '111111' in s:
        numberOfStreaks += 1
    
print('Chance of streak: %s%%' % (numberOfStreaks / 100))