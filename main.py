'''
Cows N Bulls
Programmed by Quinten Konyn
April 2017
'''


# ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████
# ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██
# █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████
# ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██
# ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████
# %%

import numpy as np
import itertools as itr
import random as rnd

def genKey(baseKey,lenKey):
    key = np.random.choice(baseKey, lenKey)
    return key

def getInput(bHint):
    prompt = "Your Guess: "
    if bHint==True: prompt = "Try one of those: "
    my_in = input(prompt)
    return my_in

def processIn(raw_in):
    if raw_in == 'hint':
        sample = 4 if len(possibilities) >= 4 else len(possibilities)
        print(rnd.sample(possibilities,sample))
        raw_in = getInput(True)
    guess = np.array(list(raw_in), dtype=int)
    #later do sanity checking here
    return guess

def giveFeedback(guess,answer):
    if np.array_equal(guess,answer):
        return (1,'u win??? maybe i guess :///')
    bulls, cows = countBullsCows(guess,answer)
    #bulls = countBulls(guess,answer)
    #cows = countCows(guess,answer,bulls)
    return (0,'u fail as always\nbulls: ' + str(bulls) + '\ncows: ' + str(cows))

def countBullsCows(g,a):
    b = 0; c = 0
    list_a = list(a)
    for i in range(len(a)):
        if g[i] == a[i]: b += 1
    for ch in g:
        if ch in list_a:
            c += 1
            list_a.remove(ch)
    c = c - b
    return (b,c)

# ███    ███  █████  ████████ ██   ██     ███████ ██    ██ ███    ██
# ████  ████ ██   ██    ██    ██   ██     ██      ██    ██ ████   ██
# ██ ████ ██ ███████    ██    ███████     █████   ██    ██ ██ ██  ██
# ██  ██  ██ ██   ██    ██    ██   ██     ██      ██    ██ ██  ██ ██
# ██      ██ ██   ██    ██    ██   ██     ██       ██████  ██   ████
# %%

def genCombos(length,base):
    combos = list(itr.product(range(length),repeat=base))
    #for i in combos:
    #    print(i)
    return combos

def narrowDown(combos,guess,fb):
    b=fb[0] ; c=fb[1]
    new_combos = list(combos)
    #print(new_combos)
    for ans in combos:
        if countBullsCows(guess,ans) != fb:
            #print('combo removed:',ans)
            new_combos.remove(ans)
    #print(new_combos)
    return new_combos

def countBits(combos):
    return np.log2(len(combos))

# ███████ ████████  █████  ██████  ████████
# ██         ██    ██   ██ ██   ██    ██
# ███████    ██    ███████ ██████     ██
#      ██    ██    ██   ██ ██   ██    ██
# ███████    ██    ██   ██ ██   ██    ██
# %%

lenKey = 4 #how many slots
baseKey = 6 #how many different each slot can be
key = genKey(baseKey,lenKey)
print('Guess something',lenKey,'numbers long with numbers 0 thru',baseKey-1)
print('Type "hint" for a hint.')
#print('the answer is',key)
possibilities = genCombos(baseKey,lenKey)
#print(possibilities)
print('Mystery Points:',round(countBits(possibilities),3))

# ███    ███  █████  ██ ███    ██
# ████  ████ ██   ██ ██ ████   ██
# ██ ████ ██ ███████ ██ ██ ██  ██
# ██  ██  ██ ██   ██ ██ ██  ██ ██
# ██      ██ ██   ██ ██ ██   ████
# %%

bQuit = False
while bQuit == False:
    unknown = countBits(possibilities)
    #print("lily is a cutie")
    aGuess = processIn(getInput(False))
    #print(aGuess)
    feedback = giveFeedback(aGuess,key)
    if feedback[0] == 1: bQuit = True
    print(feedback[1])
    possibilities = narrowDown(possibilities,aGuess,countBullsCows(aGuess,key))
    newUnknown = countBits(possibilities)
    print('You destroyed',round(unknown-newUnknown,3),'Mystery Points!\n')
    print('Mystery Points:',round(countBits(possibilities),3))
    #for i in possibilities: print(i)
