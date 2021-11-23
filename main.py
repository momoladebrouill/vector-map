import math
from random import random,choice,seed
import pygame as pg
import noise
from colorsys import hsv_to_rgb
screen=(500,500)
sizeXspeed=5
depx=0
alpha=1
class Ball:
    def __init__(self,x,y):
        self.x,self.y=x,y
        self.vecx,self.vecy=0,0
 
        
        self.dist=0
        
    @property
    def pos(self):
        return self.x,self.y
    
    def move(self):
        val=noise.pnoise2(self.x/screen[0],self.y/screen[1],octaves=10,base=depx)
        self.coul=hsv_to_rgb(0,1,(val+.5)*255)
        self.vecx=math.cos(val*math.pi)*sizeXspeed
        self.vecy=math.sin(val*math.pi)*sizeXspeed
                
        
        self.x+=self.vecx
        self.y+=self.vecy
        self.dist+=1
        if not 0<self.x<screen[0] or not 0<self.y<screen[1] or round(self.vecx,1)==round(self.vecy,1)==0 or self.dist>50:
            balls.remove(self)
            new_ball()

    def draw(self):
        pg.draw.circle(f,self.coul,self.pos,sizeXspeed)


def new_ball():
    balls.append(Ball(*[int(random()*dim) for dim in screen]))

pg.init()
f=pg.display.set_mode(screen,pg.RESIZABLE)
mask=pg.Surface(screen,0)
mask.set_alpha(alpha)

balls=[Ball(*[int(random()*dim) for dim in screen]) for _ in range(500)]
b=True
fps=pg.time.Clock()
while b:
    #fps.tick(60)
    pg.display.update()
    f.blit(mask,(0,0))
    for ball in balls:
        
        ball.move()
        ball.draw()

        
    for event in pg.event.get():
        match event.type:
            case pg.QUIT:
                b=pg.quit()
            case pg.MOUSEBUTTONUP:
                if event.button==4 or event.button==5:
                    sizeXspeed+=1 if event.button==4 else -1
                new_ball()
                seed()
            case pg.KEYUP:
                if event.key==pg.K_UP:
                    depx+=1
                elif event.key==pg.K_DOWN:
                    depx-=1
            case pg.VIDEORESIZE:
                screen=event.w,event.h
                mask=pg.Surface(screen,0)
                mask.set_alpha(alpha)
                balls=[Ball(*[int(random()*dim) for dim in screen]) for _ in range(1000)]
              
                
            
