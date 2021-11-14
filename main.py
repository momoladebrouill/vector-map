import math
from random import random,choice
import pygame as pg
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=1)
screen=(500,500)

class Ball:
    def __init__(self,x,y):
        self.x,self.y=x,y
        self.vecx,self.vecy=0,0
        self.aimx,self.aimy=choice(aims)
        self.coul=0xaaaaaa
        self.dist=0
        
    @property
    def pos(self):
        return self.x,self.y
    
    def move(self):
        self.aimx,self.aimy=mycurrentaim(self.x,self.y)
        self.vecx,self.vecy=((self.aimx-self.x)/100),((self.aimy-self.y)/100)
        
        
        self.x+=self.vecx
        self.y+=self.vecy
        self.dist+=1
        if not 0<self.x<screen[0] or not 0<self.y<screen[1] or round(self.vecx,1)==round(self.vecy,1)==0 or self.dist>50:
            balls.remove(self)
            new_ball()

    def draw(self):
        pg.draw.rect(f,self.coul,(self.x,self.y,1,1))
def closest(x,y):
    ls=[(math.sqrt((x-pos[0])**2+(y-pos[1])**2),pos) for pos in aims]
    ls.sort(key=lambda i:i[0])
    return ls[0][1]
def mycurrentaim(x,y):
    ls=[(math.sqrt((x-pos[0])**2+(y-pos[1])**2),pos) for pos in aims]
    ls.sort(key=lambda i:i[0])
    totaldist=sum([key[0] for key in ls])
    aim=[0,0]
    for dist,pos in ls:
        aim[0]+=pos[0]/dist
        aim[1]+=pos[1]/dist
    aim[0]*=10
    aim[1]*=10
    return aim
def new_ball():
    balls.append(Ball(*[int(random()*dim) for dim in screen]))

pg.init()
f=pg.display.set_mode(screen)
mask=pg.Surface(screen,0)
mask.set_alpha(1)

aims=[[int(random()*dim) for dim in screen] for _ in range(10)]
balls=[Ball(*[int(random()*dim) for dim in screen]) for _ in range(500)]
b=True
fps=pg.time.Clock()
while b:
    fps.tick(60)
    pg.display.update()
    f.blit(mask,(0,0))
    for ball in balls:
        ball.draw()
        ball.move()
    for pos in aims:
        pg.draw.circle(f,0xff60aa,pos,5)
        
    for event in pg.event.get():
        if event.type==pg.QUIT:
            b=pg.quit()
        elif event.type==pg.MOUSEBUTTONUP:
            new_ball()
            
