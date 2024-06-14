##pathfinding_test

import pygame
import keyboard
import math
import numpy as np
import random
import time

#lern_from_best
#Median movement line optimisation
#Retenir les mouvement et pas les position
#Montrer le chemin du vainqueur en orange alpha=122
#Alpha to Walker()
#Si il revient à un case atteignable précédement, la prendre
#list->tuple
#AI vs Human?
#Try and move in lines

screen_size=(800,500)
screen_=lambda: (screen_size,pygame.RESIZABLE)
screen=pygame.display.set_mode(*screen_())

title="pathfinding_test"
pygame.display.set_caption(title)

pygame.display.set_icon(pygame.Surface((0,0)))

g=22
grey_color=(g,g,g)

background_color=grey_color

is_loaded=False

presses={key: [None,None] for key in "rt"}
presses.update({key: [None,None] for key in ("space","enter")})

mclick=[[None,None] for i in range(3)]

vlr=15
bord=1
width,height=(round(i/vlr) for i in screen_size)

screen_size=(width*vlr,height*vlr)

grid=[]
rect_grid=[]
for y in range(height):
    grid.append([])
    rect_grid.append([])
    for x in range(width):
        grid[y].append("None")
        rect_grid[y].append(pygame.Rect(x*vlr,y*vlr,vlr,vlr))

colors={"None": (190,)*3,"wall": (0,)*3,"start": (22,222,22),"end": (222,22,22)}

def optimize(l):

    try:
        for i in range(len(l)):
            while True:
                if l[i] in l[i+1:]:
                    del l[i+1]
                else:
                    break
    except IndexError:
        pass

    return(l)

def Optimize(l):

    dirs=[(0,1),(1,0),(-1,0),(0,-1)]

    try:
        for i in range(len(l)):
            dirs_=[(l[i][0]+I[0],l[i][1]+I[1]) for I in dirs]
            for dir_ in dirs_:
                while dir_ in l[i+1:] and dir_!=l[i+1]:
                    del l[i+1]
    except IndexError:
        pass

    return(l)

def get_mouse_at():
    return(([math.floor(i/vlr) for i in pygame.mouse.get_pos()],None)[not(pygame.mouse.get_focused())])

def get_rect_at(x,y):

    if x<0 or y<0 or x>=width or y>=height:
        return(None)

    return(rect_grid[y][x])

def get_state_at(x,y):

    if x<0 or y<0 or x>=width or y>=height:
        return(None)

    return(grid[y][x])

def set_state_at(x,y,state):

    if x<0 or y<0 or x>=width or y>=height:
        return(None)

    grid[y][x]=state

def get_flat_grid():
    return(list(np.array(grid).flatten()))

def del_state(state):
    [[set_state_at(x,y,"None") for x in range(len(line)) if get_state_at(x,y)==state] for y,line in enumerate(grid)]

def presses_update():

    for key in presses:
        presses[key][-2]=presses[key][-1]
        presses[key][-1]=keyboard.is_pressed(key)

def click(key):
    return(pygame.display.get_active() and presses[key][-1] and not presses[key][-2])

def release(key):
    return(pygame.display.get_active() and presses[key][-2] and not presses[key][-1])

def mouse_click_update():
    for i in range(3):
        mclick[i][-2]=mclick[i][-1]
        mclick[i][-1]=pygame.mouse.get_pressed()[i]

def mouse_click():
    return([mclick[i][-1] and not mclick[i][-2] for i in range(3)])

def get_BPN():

    bpn=""
    for y,line in enumerate(grid):
        bpn=bpn+"/"
        for x,state in enumerate(line):
            if state=="wall":
                bpn=bpn+"w"
            elif state=="start":
                bpn=bpn+"s"
            elif state=="end":
                bpn=bpn+"e"
            else:
                bpn=bpn+"1"

    bpn=list(bpn)
    index=0

    for i in range(len(bpn)-1):
        if bpn[i+index]!=bpn[i+index+1]:
            index=index+1
            bpn.insert(i+index," ")

    bpn="".join(bpn).split()
    bpn=[f"{[len(i),''][len(i)==1]}{[i[0],'n'][i[0]=='1']}" for i in bpn]
    bpn="".join(bpn[1:])

    bpn=f"{bpn}-{vlr}"

    return(bpn)

def load_BPN(bpn):

    bpn,vlr=bpn.split("-")
    bpn=bpn.split("/")
    bpn_=[]

    for text in bpn:

        text=[i if not i.isdecimal() else int(i) for i in text]

        for i in range(len(text)-1):
            if type(text[i])==int and type(text[i+1])==int:
                text[i+1]=int(str(text[i])+str(text[i+1]))
                text[i]=None

        text=list(filter(lambda x: x,text))

        for i,elm in enumerate(text):
            if type(elm)==int:
                text[i+1]=text[i]*text[i+1]

        text="".join([i for i in text if type(i)==str])

        bpn_.append(text)

    bpn=bpn_
    del bpn_

    roles={"n": "None","w": "wall","s": "start","e": "end"}
    bpn=[[roles[key] for key in line] for line in bpn]
    vlr=int(vlr)

    return(bpn,vlr)

if is_loaded:

    data="14nw15nw19nw2n/2ns11nw15nw19nw2n/14nw15nw19nw2n/14nw15nw3n11w5nw2n/5n6w3nw3n7w5nw3nw4nw10nw2n"
    data=data+"/5nw8nw9nw9nw4nw10nw2n/5nw8nw9nw9nw4nw10nw2n/5nw8nw9nw9nw4nw10nw2n/5nw8nw9nw9nw4nw10nw2n/5n15w4n7w8nw4n7w2n"
    data=data+"/8nw10nw10nw8nw4nw5nw2n/8nw10nw10nw8nw4nw5nw2n/8nw10nw10nw8nw4nw5nw2n/8nw5n6w10nw8nw4nw5nw2n"
    data=data+"/5w9nw9nw5n10w10nw2n/14nw9nw9nw15nw2n/14nw9nw9nw15nw2n/14nw9nw9nw15nw2n/6n9w9nw9nw15nw2n/19nw4n11w15nw2n"
    data=data+"/19nw9nw8n13w2n/19nw9nw20nw2n/19nw9nw20nw2n/19nw9nw20nw2n/19nw9nw20nw2n/19nw9nw20nw2n/47wnenw2n/46nw3nw6n"
    data=data+"/46nw3nw6n/46nw3nw6n/46nw3nw6n/46nw3nw6n/46nw3nw6n-15"

    grid_,vlr=load_BPN(data)
    width=len(grid[0])
    height=len(grid)

    grid=[]
    rect_grid=[]
    for y in range(height):
        grid.append([])
        rect_grid.append([])
        for x in range(width):
            grid[y].append(grid_[y][x])
            rect_grid[y].append(pygame.Rect(x*vlr,y*vlr,vlr,vlr))

    screen_size=(width*vlr,height*vlr)

    start=[[(x,y) for x,string in enumerate(line) if string=="start"] for y,line in enumerate(grid)]

    if any(start):
        start=list(filter(lambda x: x,start))[0][0]
    else:
        start=None

    end=[[(x,y) for x,string in enumerate(line) if string=="end"] for y,line in enumerate(grid)]

    if any(end):
        end=list(filter(lambda x: x,end))[0][0]
    else:
        end=None

class Walker:

    walkers=[]
    winner=[]
    ggs=0
    density=[[0 for i in I] for I in grid]
    steps=0
    os=100

    def __init__(self,x,y):

        self.x=x
        self.y=y

        self.stepped_on=[(x,y)]

        self.ID=len(Walker.walkers)

        Walker.walkers.append(self)

    def step(self):

        dirs=[(0,1),(0,-1),(1,0),(-1,0)]
        dirs=[(self.x+x,self.y+y) for x,y in dirs]

        dirs=list(filter(lambda x: get_state_at(*x) in ("None","start","end"),dirs))

        if ns:=[i for i in dirs if i not in self.stepped_on]:
            dirs=random.choice(ns)
            if tuple(end) in dirs:
                dirs=end
            self.stepped_on.append(dirs)
        elif dirs:
            dirs=random.choice(dirs)
            self.stepped_on.append(dirs)
        else:
            dirs=(self.x,self.y)
            self.stepped_on.append(dirs)

        if [self.x,self.y]!=list(start):
            Walker.density[self.y][self.x]=Walker.density[self.y][self.x]-1

        self.x,self.y=self.stepped_on[-1]

        if [self.x,self.y]!=list(end):
            Walker.density[self.y][self.x]=Walker.density[self.y][self.x]+1

        if [self.x,self.y]==list(end):

            if Walker.ggs==0:
                print("\n"+get_BPN()+"\n")

            Walker.winner.append(self)

            del Walker.walkers[Walker.walkers.index(self)]
            del self

            Walker.ggs=Walker.ggs+1
            #print(f"{Walker.ggs}/{m}.")
            pygame.display.set_caption(f"{Walker.ggs}/{m} | Press enter to finish.")

            return(None)

        if Walker.steps/Walker.os==round(Walker.steps/Walker.os) or pygame.display.get_active() and click("r"): #@steps
            self.stepped_on=Optimize(optimize(self.stepped_on))

    def take_steps():
        [walker.step() for walker in Walker.walkers]
        Walker.steps=Walker.steps+1

    def draw_rect(self):

        if [self.x,self.y]==start:
            return(None)

        if get_rect_at(*self.stepped_on[-1]):

            pygame.draw.rect(screen,"orange",get_rect_at(*self.stepped_on[-1]))
            if bord:
                pygame.draw.rect(screen,(0,)*3,get_rect_at(*self.stepped_on[-1]),bord)

    def draw_rects():

        [walker.draw_rect() for walker in Walker.walkers]

def screen_lock():
    screen=pygame.display.set_mode(*screen_())
screen_lock()

frame=0
frames=None
ppl=int(2.222e+3)
m=max(round(ppl/1),1)

if not is_loaded:
    start=None
    end=None
elif start:
    [Walker(*start) for i in range(ppl)]

Set=0
def main():

    global Set
    global start
    global end
    global frame
    global frames
    global m
    global bord

    if not Set:

        presses_update()
        mouse_click_update()

        if keyboard.is_pressed("shift") and click("t"):
            print(get_BPN())

        if len(Walker.winner)<m:
            Walker.take_steps()

        if click("r") and not (start and end):
            [del_state(key) for key in colors]

        screen.fill(background_color)

        srtd=np.array(Walker.density).flatten()
        srtd=sorted(srtd)[::-1]
        rtd=srtd[int(len(srtd)/10):]

        #print(srtd)

        for y,line in enumerate(rect_grid):
            for x,rect in enumerate(line):
                pygame.draw.rect(screen,colors[grid[y][x]],rect_grid[y][x])
                if bord:
                    pygame.draw.rect(screen,background_color,rect_grid[y][x],bord)

        if click("enter") and len(Walker.winner):
            m=len(Walker.winner)

        if len(Walker.winner)<m:
            Walker.draw_rects()
        else:

            if not frames:

                frames=[i.stepped_on+[end] for i in Walker.winner]
                print(f"\n{min([len(i) for i in frames])}/{max([len(i) for i in frames])}.")

                frames=[Optimize(optimize(i)) for i in frames]
                frames=sorted(frames,key=lambda x: len(x))[0]

                print(f"{len(frames)}.")

            for i in range(frame):

                if tuple(frames[i])!=tuple(start):
                    pygame.draw.rect(screen,"orange",get_rect_at(*frames[i]))
                    if bord:
                        pygame.draw.rect(screen,(0,)*3,get_rect_at(*frames[i]),bord)

            frame=frame+1

            frame=min(frame,len(frames)-1)

            if click("r"):
                frame=0

        if (current:=get_mouse_at()) and get_rect_at(*current):

            pygame.draw.rect(screen,"red",get_rect_at(*current),2)

            if pygame.mouse.get_pressed()[2] and not (start and end):

                if tuple(current)==start:
                    start=None
                elif tuple(current)==end:
                    end=None

                set_state_at(*current,"None")

            if pygame.mouse.get_pressed()[0] and get_state_at(*current)=="None" and not (start and end):
                set_state_at(*current,"wall")

            if mouse_click()[1] and get_state_at(*current)=="None" and not (start and end):

                if "start" not in get_flat_grid():
                    set_state_at(*current,"start")
                    start=current
                else:
                    del_state("end")
                    set_state_at(*current,"end")
                    end=current

                    [Walker(*start) for i in range(ppl)]

        pygame.display.flip()

launched=True
print(f"{launched=}.")

try:
    while launched:

        started=time.perf_counter()
        while not len(Walker.winner)<m and time.perf_counter()-started<1/32:
            pass

        main()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                launched=False
            elif event.type==pygame.VIDEORESIZE:
                screen_lock()

except KeyboardInterrupt:
    print("*** Manual Shutdown ***")
    launched=False

print(f"{launched=}.")
pygame.quit()