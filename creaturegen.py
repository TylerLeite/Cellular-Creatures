#disgusting code dont try to read

from PIL import Image, ImageFilter

import os
import sys
import random
import math

def fill(arr, x, y):
    out = []

    fill_q = set()
    fill_q.add((x,y))
    while fill_q:
        x, y = fill_q.pop()
        if (x,y) in out:
            continue
        if arr[x][y] != -1:
            out.append((x,y))
            if x > 0 and x < 31 and y > 1 and y < 31:
                fill_q.add((x,y-1))
                fill_q.add((x,y+1))
                fill_q.add((x+1,y))
                fill_q.add((x-1,y))
    return out

def randimg(filen, base):
    img = Image.open(base)
    im = img.load()

    while True:
        pic = [[-1 for x in range(32)] for y in range(32)]
        for x in range(8, 24):
            for y in range(1, 31):
                if random.randint(0, 100) < math.sqrt(x*x + y*y):
                    pic[x][y] = random.randrange(4)

        for generation in range(4):
            tmp = [[-1 for x in range(32)] for y in range(32)]
            for x in range(1, 31):
                for y in range(1, 31):
                    count = 0
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if pic[x+i][y+j] != -1:
                                count += 1

                    if pic[x][y] == -1:
                        if count > 4 or count == 0:
                            tmp[x][y] = random.randrange(4)

                    elif pic[x][y] != -1:
                        if count < 4 or count == 0:
                            tmp[x][y] = -1

            pic = [[tmp[x][y] for x in range(32)] for y in range(32)]

        face_color = (0,0,0,255)
        colors = []
        if random.randrange(2) == 0:
            for i in range(4):
                r = random.choice([0,32,64,96])
                g = random.choice([0,32,64,96])
                b = random.choice([0,32,64,96])
                colors.append((r,g,b,255))
            face_color = (255,255,255,255)
        else:
            for i in range(4):
                r = random.choice([128,160,192,224])
                g = random.choice([128,160,192,224])
                b = random.choice([128,160,192,224])
                colors.append((r,g,b,255))


        for generation in range(2):
            for x in range(1, 31):
                for y in range(1, 31):
                    if pic[x][y] == -1:
                        continue
                    else:
                        counts = [0,0,0,0]
                        for i in range(-1, 2):
                            for j in range(-1, 2):
                                color = pic[x+i][y+j]
                                if color == -1:
                                    continue
                                else:
                                    counts[color] += 1
                        color = counts.index(max(counts))
                        if color == pic[x][y]:
                            for i in range(-1, 2):
                                for j in range(-1, 2):
                                    if pic[x+i][y+j] == -1:
                                        continue
                                    if random.randrange(100) < 40:
                                        pic[x+i][y+j] = color
                        else:
                            if random.randrange(100) < 10:
                                pic[x][y] = color

        x = random.randrange(10, 22)
        y = random.randrange(10, 22)
        while (pic[x][y] == -1):
            x = random.randrange(10, 22)
            y = random.randrange(10, 22)

        save = fill(pic, x, y)

        for x in range(32):
            for y in range(32):
                if not (x,y) in save:
                    pic[x][y] = -1

        out = False
        for x in range(10, 22):
            if out:
                break
            for y in range(10, 22):
                if out:
                    break

                count = 0
                for i in range(-2, 4):
                    for j in range(-2, 4):
                        if pic[x+i][y+j] != -1:
                            count += 1

                if count == 36:
                    pic[x][y] = -2
                    pic[x+2][y] = -2
                    pic[x][y+2] = -2
                    pic[x+1][y+2] = -2
                    pic[x+2][y+2] = -2
                    out = True
                count = 0

        if out:
            break

    for x in range(32):
        for y in range(32):
            out = (0,0,0,0)
            if x >= 8 and x <= 24 and y >= 8 and y <= 24:
                if pic[x][y] >= 0:
                    out = colors[pic[x][y]]
                elif pic[x][y] == -2:
                    out = face_color
                im[x,y] = out

    img.save(filen, "PNG")

infile = sys.argv[1]
walk_dir = sys.argv[2]

for i in range(100):
    print i
    outfname = walk_dir + "/" + str(i) + ".png"
    randimg(outfname, infile)
