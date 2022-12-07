# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input).
# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack.
# Crates are moved one at a time
# After the rearrangement procedure completes, what crate ends up on top of each stack?

# Read in starting stack configuration
# %%
from pathlib import Path

# %%
inputfile = open(Path.cwd() / "gri_input.txt")
# inputfile = open('day5_input.txt')
content = inputfile.readlines()
flag = True
i = 0
while flag:
    if content[i][1] == "1":  # search for the line with the stack number
        flag = False
    i = i + 1
spltln1 = i
flag = True
while flag:
    if content[i][0] == "m":  # search for line with 1st 'move to'
        flag = False
    i = i + 1
spltln2 = i
print(spltln1)
print(spltln2)

# %%
pos = []
crate = []
layerpos = [[]]
layercrate = [[]]
for i in range(spltln1 - 1):
    for j in range(len(content[i])):
        if content[i][j] == "[":
            c = content[i][j + 1]
            j = int(j / 4) + 1
            pos.append(j)
            crate.append(c)
    layerpos.append(pos)
    layercrate.append(crate)
    pos = []
    crate = []

#%%
layerpos.remove([])  # create the layers conternt position
layercrate.remove([])  # create the layer content

# %%
# fill the stacks basically ned to transpose the layer matrix into stack matrix
stck = []  # single stack
tstck = [[]]  # all stacks
n = 0
for i in range(9):  # number of stacks
    for j in range(len(layerpos)):  # number of layers
        j = len(layerpos) - j  # inverted LiFO
        for k in range(len(layerpos[j - 1])):  # content of each layer
            if layerpos[j - 1][k] == i + 1:
                stck.append(layercrate[j - 1][k])
    tstck.append(stck)
    stck = []
tstck.remove([])

#%%
# read the rearranging sequence removing worlds
move = []
for i in range(spltln2 - 1, len(content)):
    content[i] = content[i].replace("move", "")
    content[i] = content[i].replace("from", "")
    content[i] = content[i].replace("to", "")
    content[i] = content[i].replace(" ", "")
    content[i] = content[i].replace("\n", "")
    move.append(content[i])  # position 0 : how many # position 1: from, position2 :to

# %%
# finally starting the move sequence!

for i in range(len(move)):
    h = len(move)
    l = move[0]
    ncrates = int(move[i][:-2])
    frm = int(move[i][-2])
    to = int(move[i][-1])
    for j in range(ncrates):
        tstck[to - 1].append(tstck[frm - 1][-1])
        tstck[frm - 1].remove(tstck[frm - 1][-1])
print(i)

#%%
# top layer
tlayer = []
for i in range(9):
    tlayer.append(tstck[i][-1])
print(move[0], move[-1])
print(tlayer)


# Follow the steps for re-arranging
# Submit the top layer as answer

# %%
