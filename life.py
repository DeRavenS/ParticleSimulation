
# Importing the library
import math
import random
from tkinter import S
import pygame
pygame.init()

def particle(x,y,c):
    return {"x":x,"y":y,"vx":0,"vy":0,"color":c}

particles=[]
surface = pygame.display.set_mode((800,800))

def create(number,color):
    group=[]
    for i in range(0,number):
        group.append(particle(random.randrange(100,700), random.randrange(100,700), color))
        particles.append(group[i])
    return group

def rule(p1,p2,g):
    for i in range(0,p1.__len__()):

        fx = 0
        fy = 0
        for j in range(0,p2.__len__()):
            a = p1[i]
            b = p2[j]
            dx = a["x"] - b["x"]
            dy = a["y"] - b["y"]

            d = math.sqrt(dx*dx + dy*dy)

            if d > 0 and d<80:
             F = g * 1/d
             fx += (F * dx)
             fy += (F * dy)
            # else:
            #     fx=0
            #     fy=0

        a["vx"] = (a["vx"] + fx)*0.5
        a["vy"] = (a["vy"] + fy)*0.5
        a["x"] += a["vx"] 
        a["y"] += a["vy"]

        if(a["x"]<=100 or a["x"]>=700):a["vx"]*=-1
        if(a["y"]<=100 or a["y"]>=700):a["vy"]*=-1

def draw(x,y,c,s):
    pygame.draw.rect(surface,c,pygame.Rect(x,y,s,s))



run = True

red = create(100,(255,0,0))
green = create(100,(0,255,0))
blue = create (100,(0,0,255))
white = create (100,(255,255,255))

while run: 
    surface.fill((0,0,0))
    
    rule(green,green,-0.32)
    rule(green,red,-0.17)
    rule(green,blue,0.34)

    rule(red,red,-0.1)
    rule(red,green,-0.34)

    rule(blue,blue,0.15)
    rule(blue,green,-0.2)
    rule(blue,white,-0.32)

    rule(white,white,-0.32)
    rule(white,green,0.32)
    rule(white,blue,-0.32)
    for i in particles:
        draw(i["x"],i["y"],i["color"],4)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False



