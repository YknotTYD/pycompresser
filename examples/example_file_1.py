#tic_tac_toe

import pygame
import sys
from pygame import mixer

#sons, IA, pause, UI, mappage des touches, déplacement au clavier

screen_size=[300,300]
screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)

title="Tic_Tac_Toe"
pygame.display.set_caption("               "+title)

launched=True
print("launched==True")

g=22
grey_color=(g,g,g)
black_color=(0,0,0)
white_color=(255,255,255)
lighter_pink_color=(255,220,255)
light_pink_color=(255,142,242)
pink_color=(255,50,180)
red_color=(254,25,25)
orange_color=(255,170,25)
yellow_color=(255,225,25)
green_color=(15,205,30)

background_color=grey_color
p1_color=yellow_color
p2_color=red_color
won=[0]
hotbar=[0]
hotbar_size=[64]

key_h=[0]
key_UP=[0]
key_DOWN=[0]
key_SPACE=[0]
key_RIGHT=[0]
key_LEFT=[0]
key_z=[0]
key_s=[0]
key_g=[0]
key_f=[0]
key_r=[0]
#key_f=[0]

key_R=[0]
key_G=[0]

frame=[0]

sp=3
l1=[]
for i in range(9):
    l1.append(None)

lg="eng"

def key_check(key):

    if key==key_h:
        if pygame.key.get_pressed()[pygame.K_h]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_s:
        if pygame.key.get_pressed()[pygame.K_s]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_z:
        if pygame.key.get_pressed()[pygame.K_z]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_g:
        if pygame.key.get_pressed()[pygame.K_g]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_UP:
        if pygame.key.get_pressed()[pygame.K_UP]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_DOWN:
        if pygame.key.get_pressed()[pygame.K_DOWN]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_RIGHT:
        if pygame.key.get_pressed()[pygame.K_RIGHT]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_LEFT:
        if pygame.key.get_pressed()[pygame.K_LEFT]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_SPACE:
        if pygame.key.get_pressed()[pygame.K_SPACE]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_f:
        if pygame.key.get_pressed()[pygame.K_f]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

    if key==key_r:
        if pygame.key.get_pressed()[pygame.K_r]==True:
            key[0]=key[0]+1
        else:
            key[0]=0

def Key_check():
    key_check(key_UP)
    key_check(key_DOWN)
    key_check(key_SPACE)
    key_check(key_RIGHT)
    key_check(key_LEFT)
    key_check(key_h)
    key_check(key_z)
    key_check(key_g)
    key_check(key_f)
    key_check(key_r)
    #key_check(key_)

def frame_check():

    if key_h[0]==2:

        if frame[0]==0:
            screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)
            frame[0]=1

        elif frame[0]==1:
            pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)
            frame[0]=0

        else:
            print("FrameError")

def screen_lock():

    if screen_size!=[pygame.display.get_window_size()[0],pygame.display.get_window_size()[1]]:

        if frame[0]==0:
            screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)

        elif frame[0]==1:
            screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)

        else:
            print("FrameError")

def color_of(x,y):

    return((screen.get_at([x,y])[0],screen.get_at([x,y])[1],screen.get_at([x,y])[2]))

click=[]

def Click_update():

    if len(click)>1:
        del click[0]
    click.append(pygame.mouse.get_pressed()[0])

def Click():

    if len(click)>0:
        if click[0]==1 and click[1]==0:
            return(True)
        else:
            return(False)

def set():

    Key_check()
    frame_check()
    screen_lock()
    cursor_update()
    Click_update()
    state_update()

    if won[0]!=1:

        for i in range(2):
            if win_update(i+1):
                print("{} won.".format(Player.p[i].name))
                won[0]=1

    screen.fill(background_color)

    if hotbar[0]==1:
        Draw(Rect(sp,sp,screen_size[0]-sp,hotbar_size[0]-sp,(255,255,255)),3)

    for i in range(len(l)):

        if cursor().colliderect(rect_form(l[i]))==True:

            if won[0]==0:
                l[i].color=Player.cp.color
            elif won[0]==1:
                l[i].color=light_pink_color

        else:
            l[i].color=white_color

        if l[i].state==1:
            l[i].color=p1.color
        elif l[i].state==2:
            l[i].color=p2.color
        elif l[i].state==-1:
            l[i].color=pink_color

        Draw(Rect(l[i].x,l[i].y,l[i].L,l[i].l,l[i].color,l[i].state),3)

    #pygame.draw.rect(screen,color_of(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]),cursor())

    pygame.display.flip()
    pygame.time.Clock().tick(60)

class Rect:

    def __init__(self,x=0,y=0,L=22,l=22,c=(0,0,0),state=0):

        self.x=x
        self.base_x=x

        self.y=y
        self.base_y=y

        self.L=L
        self.base_L=L

        self.l=l
        self.base_l=l

        self.color=c
        self.base_color=c

        self.state=state
        self.base_state=state

class Player:

    cp=None
    n=0
    p=[]

    def __init__(self,color=(255,255,255)):

        self.color=color
        self.base_color=color

        Player.n=Player.n+1
        Player.p.append(self)

    def set_name(self,name):

        self.name=name

p1=Player(yellow_color)
p1.n=1
p1.set_name("Yellow")

p2=Player(red_color)
p2.n=2
p2.set_name("Red")

Player.cp=p1

x=0
y=0
l=[]
for i in range(9):
    l.append(Rect(sp+x*((sp+screen_size[0]-4*sp)/3),sp+y*((sp+screen_size[1]-4*sp)/3),(screen_size[0]-4*sp)/3,(screen_size[1]-4*sp)/3,white_color))
    x=x+1
    if x>=3:
        x=0
        y=y+1

screen_size[0]=l[8].x+l[8].L+3
screen_size[1]=l[8].y+l[8].l+3

#print(l)

def rect_form(t):

    return(pygame.Rect(t.x,t.y,t.L,t.l))

def Draw(t,L=None):

    if L!=None:
        pygame.draw.rect(screen,t.color,rect_form(t),L)
    else:
        pygame.draw.rect(screen,t.color,rect_form(t))

def tile_form(x):

    if x=="UPLEFT":
        return(l[0])
    elif x=="UP":
        return(l[1])
    elif x=="UPRIGHT":
        return(l[2])
    elif x=="LEFT":
        return(l[3])
    elif x=="CENTER":
        return(l[4])
    elif x=="RIGHT":
        return(l[5])
    elif x=="DOWNLEFT":
        return(l[6])
    elif x=="DOWN":
        return(l[7])
    elif x=="DOWNRIGHT":
        return(l[8])

    else:
        print('''tile_form(x)

isinstance(x,str)==True
x=="UPLEFT" or "UP" or "UPRIGHT" or "LEFT" or "CENTER" or "RIGHT" or "DOWNLEFT" or "DOWN" or "DOWNRIGHT"''')

def state_update():

    for i in range(len(l)):
        if cursor().colliderect(rect_form(l[i]))==True and Click() and l[i].state==0:

            if won[0]==0:
                l[i].state=Player.cp.n

                if Player.cp==p1:
                    Player.cp=p2
                else:
                    Player.cp=p1
            else:
                l[i].state=-1

def cursor_update():

    return(pygame.mouse.get_pos())

def cursor():

    return(pygame.Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1))

def win_update(i):

    if tile_form("UPLEFT").state==i and tile_form("UP").state==i and tile_form("UPRIGHT").state==i or tile_form("LEFT").state==i and tile_form("CENTER").state==i and tile_form("RIGHT").state==i or tile_form("DOWNLEFT").state==i and tile_form("DOWN").state==i and tile_form("DOWNRIGHT").state==i or tile_form("UPRIGHT").state==i and tile_form("CENTER").state==i and tile_form("DOWNLEFT").state==i or tile_form("UPLEFT").state==i and tile_form("CENTER").state==i and tile_form("DOWNRIGHT").state==i or tile_form("UPLEFT").state==i and tile_form("LEFT").state==i and tile_form("DOWNLEFT").state==i or tile_form("UP").state==i and tile_form("CENTER").state==i and tile_form("DOWN").state==i or tile_form("UPRIGHT").state==i and tile_form("RIGHT").state==i and tile_form("DOWNRIGHT").state==i:
        return(True)
    else:
        return(False)

def reboot():
    for i in range(9):
        l[i].state=0
    won[0]=0
    Player.cp=p1

def Hotbar(x):

    a=hotbar_size[0]

    if x==1:
        for i in range(9):
            l[i].y=l[i].y-a
        hotbar[0]=0
        screen_size[1]=screen_size[1]-a

    if x==0:
        for i in range(9):
            l[i].y=l[i].y+a
        hotbar[0]=1
        screen_size[1]=screen_size[1]+a

    #print(hotbar[0])

while launched==True:

    tile_form("CENTER")

    key_h=key_h[0]
    key_UP=key_UP[0]
    key_DOWN=key_DOWN[0]
    key_SPACE=key_SPACE[0]
    key_RIGHT=key_RIGHT[0]
    key_LEFT=key_LEFT[0]
    key_z=key_z[0]
    key_s=key_s[0]
    key_g=key_g[0]
    key_f=key_f[0]
    key_r=key_r[0]
    #key_f=key_f[0]

    key_R.append(key_r)
    if len(key_R)>3:
        del key_R[0]

    if key_R[0]>0 and key_R[1]>0 and key_R[2]==0:
        reboot()

    key_G.append(key_g)
    if len(key_G)>2:
        del key_G[0]

    if key_g==2:

        Hotbar(hotbar[0])

        """if hotbar[0]==0:
            hotbar[0]=1
        elif hotbar[0]==1:
            hotbar[0]=0
        else:
            print("hotbarError")"""

    key_h=[key_h]
    key_UP=[key_UP]
    key_g=[key_g]
    key_DOWN=[key_DOWN]
    key_SPACE=[key_SPACE]
    key_RIGHT=[key_RIGHT]
    key_LEFT=[key_LEFT]
    key_z=[key_z]
    key_s=[key_s]
    key_f=[key_f]
    key_r=[key_r]
    #key_f=[key_f]

    set()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            launched=False
            print("launched==False")
            pygame.quit()
            sys.exit()




