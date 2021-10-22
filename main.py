import pygame as pg
from utis import *
from dee import Table
from random import random
pg.init()
f=pg.display.set_mode((500,500),pg.RESIZABLE)
fps=pg.time.Clock()
B=True


class Particule:
    def __init__(self,pos):
        self.anchor=Pos(pos[0],pos[1])
        self.pos=Pos(pos[0]+random()-.5,pos[1]+random()-.5)
        self.vec=Vec(x=0,y=0)
    def __repr__(self):
        return "P"
    
Map=Table(size=(10,10),default=lambda x,y:Particule((x,y)))


while B:
    pg.display.flip()
    f.fill(0)
    fps.tick(60)
    
    for pouss,pos in Map:
        """grav=Vec(a=pouss.pos,b=pouss.anchor)
        grav.long/=2
        pouss.vec+=grav
        pouss.pos+=pouss.vec"""
        pg.draw.circle(f,0xffffff,(pouss.pos.x*50,pouss.pos.y*50),5)
        
    mousepos=pg.mouse.get_pos()
    
    try:
        victim=Map[mousepos[0]//50,mousepos[1]//50]
        repou=Vec(a=Pos(mousepos[0],mousepos[1]),b=victim.pos)
        repou.long=1
        victim.vec+=repou
    except IndexError:
        pass
    
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            B=False
            
