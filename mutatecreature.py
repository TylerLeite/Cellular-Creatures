#sloppy code, dont try to read it

import random
from termcolor import colored

class Cell:
    def __init__(self, color):
        self.rep = "#"
        self.color = color

    def to_string(self):
        return colored(self.rep, self.color)

class Tcolors:
    red = 'red'
    green = 'green'
    blue = 'blue'
    yellow = 'yellow'
    orange = 'cyan'
    purple = 'magenta'
    brown = 'grey'
    pink = 'white'

    def rand(self):
        c = random.randrange(8)
        if c == 0:
            return self.red
        elif c == 1:
            return self.green
        elif c == 2:
            return self.blue
        elif c == 3:
            return self.yellow
        elif c == 4:
            return self.orange
        elif c == 5:
            return self.purple
        elif c == 6:
            return self.brown
        elif c == 7:
            return self.pink
        else:
            return None

tcolors = Tcolors()

base_creature = [
    [None,None,None,None,Cell(tcolors.red),Cell(tcolors.blue),None,None],
    [None,Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.blue)],
    [None,Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.blue)],
    [None,Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.red)],
    [None,Cell(tcolors.red),Cell(tcolors.blue),Cell(tcolors.blue),Cell(tcolors.green),Cell(tcolors.red),None,Cell(tcolors.red)],
    [None,None,Cell(tcolors.red),Cell(tcolors.red),Cell(tcolors.green),Cell(tcolors.green),None,None],
    [None,None,None,Cell(tcolors.green),Cell(tcolors.green),Cell(tcolors.green),None,None],
    [None,None,None,Cell(tcolors.green),Cell(tcolors.green),Cell(tcolors.green),None,None],
]

def print_creature(name, creature):
    print name + ": "
    for row in creature:
        out = ""
        for cell in row:
            if cell is None:
                out += " "
            else:
                out += cell.to_string()
        print out

print_creature("Base creature", base_creature)

wd = len(base_creature[0])
hg = len(base_creature)
for i in range(3):
    # create new creature as a copy of the base
    new_creature = []

    for y in range(hg):
        row = []
        for x in range(wd):
            if base_creature[y][x] is None:
                row.append(None)
            else:
                row.append(Cell(base_creature[y][x].color))
        new_creature.append(row)

    # first alter shape
    for generation in range(1):
        for y in range(hg):
            for x in range(wd):
                ct = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nx = x + i
                        ny = y + j
                        if nx < 0 or nx >= wd or ny < 0 or ny >= hg:
                            ct += 1
                        elif not base_creature[ny][nx] is None:
                            ct += 1
                if ct == 9:
                    continue
                else:
                    if new_creature[y][x] is None:
                        if random.randrange(100) < 5:
                            new_creature[y][x] = Cell(random.choice(['red', 'green', 'blue']))
                    else:
                        if random.randrange(100) < 10:
                            new_creature[y][x] = None


    # next alter colors
    for generation in range(3):
        for y in range(hg):
            for x in range(wd):
                cts = [0,0,0] # r,g,b
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        nx = x + i
                        ny = y + j
                        if nx < 0 or nx >= wd or ny < 0 or ny >= hg:
                            continue
                        elif base_creature[ny][nx] is None:
                            continue
                        else:
                            color = base_creature[ny][nx].color
                            if color == 'red':
                                cts[0] += 1
                            elif color == 'green':
                                cts[1] += 1
                            elif color == 'blue':
                                cts[2] += 1

                c = cts.index(max(cts))
                colors = ['red', 'green', 'blue']
                if new_creature[y][x] is None:
                    continue
                elif new_creature[y][x].color == colors[c]:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            nx = x + i
                            ny = y + j
                            if nx < 0 or nx >= wd or ny < 0 or ny >= hg:
                                continue
                            elif random.randrange(100) < 90:
                                continue
                            elif new_creature[ny][nx] is None:
                                continue
                            else:
                                new_creature[ny][nx].color = colors[c]
                else:
                    if random.randrange(100) < 40:
                        new_creature[y][x].color = colors[c]

    print_creature("Similar creature #" + str(i), new_creature)
