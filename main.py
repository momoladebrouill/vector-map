import pygame as pg
from utis import *
from dee import Table

pg.init()
f=pg.display.set_mode((500,500))
fps=pg.time.Clock()
B=True
Map=Table()
Map[0,0]=0xff0000
Map[50,50]=0x00ff00
while B:
    pg.display.flip()
    fps.tick(60)
    for val,pos in Map:
        pg.draw.rect(f,val,(pos[0]*10,pos[1]*10,10,10))
    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
            B=False
        elif event.type==pg.MOUSEBUTTONUP:
            Map[int(event.pos[0]/50)*50,
                int(event.pos[1]/50)*50]=0xffff00
