#pong

import pygame
from pygame import mixer
mixer.init()
import sys
import random

screen_size=[1000,500]
screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)#|pygame.NOFRAME)

title="pong"
pygame.display.set_caption(title)

pygame.display.set_icon(pygame.Surface((0,0)))

g=22
grey_color=(g,g,g)
red_color=(255,25,25)
white_color=(255,255,255)
background_color=grey_color

class Rect:

    def __init__(self,l,L,x,y,c,speed=10):

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

        self.speed=speed
        self.base_speed=speed

        self=pygame.Rect(L,l,x,y)

recty=Rect(93,20,10,screen_size[1]/2-10,white_color,15)

recty_bar=Rect(93,20,screen_size[0]-10-20,screen_size[1]/2-10,white_color)

recty_ball=Rect(20,20,recty.x+recty.l+5,recty.y+recty.l/2-10,white_color,10)

ml_rect=Rect(24,12,screen_size[0]/2-6,20,white_color)

frame=1
recty_ball_free=[0]
recty_ball_pnt=0
recty_ball_stop=0
l=[]
l1=[]
recty_ball_pnt_u=0
state=1
auto=[0]

if auto==1:
    recty_ball.speed=35

dec=0
color_change=1
speed_boost=0

if auto!=[1]:
    color_change=1

invert_color=0
launch=0

if invert_color==1:

    background_color=white_color
    recty.color=grey_color
    recty_bar.color=grey_color
    recty_ball.color=grey_color

if frame==0:
    screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)

elif frame==1:
    screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)

def set():

    Key_check()

    screen.fill(background_color)

    ml_rect.y=ml_rect.base_y
    for i in range(11):
        pygame.draw.rect(screen,recty.color,rect_form(ml_rect))
        ml_rect.y=ml_rect.y+44

    pygame.draw.rect(screen,recty.color,rect_form(recty))
    pygame.draw.rect(screen,recty.color,rect_form(recty_ball))
    pygame.draw.rect(screen,recty_bar.color,rect_form(recty_bar))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

key_h=[0]
key_UP=[0]
key_DOWN=[0]
key_SPACE=[0]
key_RIGHT=[0]
key_LEFT=[0]
key_z=[0]
key_s=[0]
key_g=[0]

key_f_SPACE=0

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

def Key_check():
    key_check(key_UP)
    key_check(key_DOWN)
    key_check(key_SPACE)
    key_check(key_RIGHT)
    key_check(key_LEFT)
    key_check(key_h)
    key_check(key_z)
    key_check(key_g)
    #key_check(key_)

def rect_form(recty):

    return(pygame.Rect(recty.x,recty.y,recty.L,recty.l))

def bounce(recty,recty_ball):

    if rect_form(Rect(recty_ball.l,recty_ball.L,recty_ball.x-1,recty_ball.y,recty_ball.color,recty_ball.speed)).colliderect(rect_form(recty))==True and recty_ball.x+1==recty.x+recty.L:

        if auto[0]!=1:

            px=((recty_ball.y+recty_ball.l/2)-(recty.y+recty.l/2))/2

        elif auto[0]==1:
            px=((recty_ball.y+recty_ball.l/2)-(recty.y+recty.l/2))/2
        px=-px
        return(px)

hitsound_volume=1

main_volume=0
hitsound_volume=hitsound_volume*main_volume

def hitsound():

    return(None)

    channel_0=mixer.Sound("Random_File/Audio/hitsound.wav")
    mixer.Sound.set_volume(channel_0,hitsound_volume)
    mixer.Channel(0).play(channel_0)

launched=True
print("launched==True")
print("")

while launched==True:

    l1.append(pygame.time.get_ticks())

    pygame.mouse.set_visible(False)
    keys=pygame.key.get_pressed()

    try:

        if recty_ball.speed<=17:
            recty_ball.speed=recty_ball.speed+0.2/60
            #recty_ball.speed=round(recty_ball.speed,2)
        #print(recty_ball.speed)

        if dec==15 or 1==1:
            recty_bar.y=recty_ball.y-recty_bar.l/2+recty_ball.l/2

        if dec==0 and 1==2:
            pass
            recty_bar.y=recty_ball.y

        if recty_bar.y+recty_bar.l>=screen_size[1]:
            recty_bar.y=screen_size[1]-recty_bar.l

        if recty_bar.y<=0:
            recty_bar.y=0

        if recty.y+recty.l>=screen_size[1]:
            recty.y=screen_size[1]-recty.l

        if recty.y<=0:
            recty.y=0

        set()

        key_h=key_h[0]
        key_UP=key_UP[0]
        key_DOWN=key_DOWN[0]
        key_SPACE=key_SPACE[0]
        key_RIGHT=key_RIGHT[0]
        key_LEFT=key_LEFT[0]
        key_z=key_z[0]
        key_s=key_s[0]
        key_g=key_g[0]
        #key_g=key_g[0]

        if auto[0]==1:

            recty_ball_free[0]=1

            if dec==15 or 1==1:
                recty=Rect(93,20,10,recty_ball.y,recty.color,15)

            if dec==0 and 1==2:
                recty=Rect(93,20,10,recty_ball.y-recty_bar.l/2+recty_ball.l/2-20,recty.color,15)

            if len(l1)==1:
                screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)
                frame=0

            if recty_ball_pnt==0:
                recty_ball_pnt=1

            dec=dec+1
            if dec==30:
                recty_ball.speed=recty_ball.base_speed+random.randint(-22,35)
                dec=0

        l.append(recty_ball.x)
        if len(l)>=6:
            l.remove(l[0])

        if bounce(recty,recty_ball)!=None:
            recty_ball_pnt_u=bounce(recty,recty_ball)

        if launch==0:

            if random.randint(0,1)==1:
                recty_ball_pnt_u=random.randint(6,10)

            else:
                recty_ball_pnt_u=random.randint(-10,-6)

        if recty_ball.y-1<=0:
            recty_ball_pnt_u=-recty_ball_pnt_u

            hitsound()

            if color_change==1:

                if background_color==grey_color:
                    background_color=white_color
                elif background_color==white_color:
                    background_color=grey_color

                if recty.color==white_color:
                    recty.color=grey_color
                elif recty.color==grey_color:
                    recty.color=white_color

                if recty_bar.color==white_color:
                    recty_bar.color=grey_color
                elif recty_bar.color==grey_color:
                    recty_bar.color=white_color

                if recty_ball.color==white_color:
                    recty_ball.color=grey_color
                elif recty_ball.color==grey_color:
                    recty_ball.color=white_color

        if recty_ball.y+recty_ball.l+1>=screen_size[1]:
            recty_ball_pnt_u=-recty_ball_pnt_u

            hitsound()

            if color_change==1:

                if background_color==grey_color:
                    background_color=white_color
                elif background_color==white_color:
                    background_color=grey_color

                if recty.color==white_color:
                    recty.color=grey_color
                elif recty.color==grey_color:
                    recty.color=white_color

                if recty_bar.color==white_color:
                    recty_bar.color=grey_color
                elif recty_bar.color==grey_color:
                    recty_bar.color=white_color

                if recty_ball.color==white_color:
                    recty_ball.color=grey_color
                elif recty_ball.color==grey_color:
                    recty_ball.color=white_color

        try:

            if recty_ball_pnt_u>0:
                for i in range(int(round(recty_ball_pnt_u,1))):

                    if recty_ball.y-1>=0:
                        recty_ball.y=recty_ball.y-1

            if recty_ball_pnt_u<0:
                for i in range(int(round(-recty_ball_pnt_u,1))):

                    if recty_ball.y+1+recty_ball.l<=screen_size[1]:
                        recty_ball.y=recty_ball.y+1

        except NameError:
            pass

        if key_SPACE==1 and key_f_SPACE==0:
            key_f_SPACE=1
            recty_ball_free[0]=1
            recty_ball_pnt=1

        a=-1
        for i in range(len(l)):
            try:
                if l[0-a]==l[1-a] and recty_ball_free[0]==1 and recty_ball.x<2 or l[0-a]==l[1-a] and recty_ball_free[0]==1 and recty_ball.x>screen_size[0]-recty_ball.L-2:
                    recty_ball_stop=1
                a=a+1
            except IndexError:
                pass

        if recty_ball_stop==1:
            if recty_ball.x<5:
                pass#rint("mort()")
                state=0
            if recty_ball.x>screen_size[0]-5:
                pass#rint("victoire()")

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                pygame.quit()
                launched=False
                print("launched==False")
                sys.exit()

            elif event.type==pygame.VIDEORESIZE:

                pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

                if frame==0:
                    screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)

                elif frame==1:
                    screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)

        if recty_ball_pnt>0 and rect_form(Rect(recty_ball.l,recty_ball.L,recty_ball.x+1,recty_ball.y,recty_ball.color,recty_ball.speed)).colliderect(rect_form(recty_bar))==True:
            recty_ball_pnt=-1

            hitsound()

            if color_change==1:

                if background_color==grey_color:
                    background_color=white_color
                elif background_color==white_color:
                    background_color=grey_color

                if recty.color==white_color:
                    recty.color=grey_color
                elif recty.color==grey_color:
                    recty.color=white_color

                if recty_bar.color==white_color:
                    recty_bar.color=grey_color
                elif recty_bar.color==grey_color:
                    recty_bar.color=white_color

                if recty_ball.color==white_color:
                    recty_ball.color=grey_color
                elif recty_ball.color==grey_color:
                    recty_ball.color=white_color

        if rect_form(Rect(recty_ball.l,recty_ball.L,recty_ball.x-1,recty_ball.y,recty_ball.color,recty_ball.speed)).colliderect(rect_form(recty))==True and recty_ball_pnt<0 and recty.y+recty.l>recty_ball.y>recty.y-recty_ball.l:
            recty_ball_pnt=1

            hitsound()

            if color_change==1:

                if background_color==grey_color:
                    background_color=white_color
                elif background_color==white_color:
                    background_color=grey_color

                if recty.color==white_color:
                    recty.color=grey_color
                elif recty.color==grey_color:
                    recty.color=white_color

                if recty_bar.color==white_color:
                    recty_bar.color=grey_color
                elif recty_bar.color==grey_color:
                    recty_bar.color=white_color

                if recty_ball.color==white_color:
                    recty_ball.color=grey_color
                elif recty_ball.color==grey_color:
                    recty_ball.color=white_color

        if recty_ball_free[0]==1:

            for i in range(int(round(recty_ball.speed,0))):

                if launch==0:
                    launch=1

                if recty_ball.x<=screen_size[0]-recty_ball.L and recty_ball_pnt>0 and rect_form(recty_ball).colliderect(rect_form(recty_bar))==False:
                    recty_ball.x=recty_ball.x+recty_ball_pnt
                    if recty_ball.x>screen_size[0]-recty_ball.L or rect_form(recty_ball).colliderect(rect_form(recty_bar))==True:
                        recty_ball.x=recty_ball.x-recty_ball_pnt

                if recty_ball.x>=0 and recty_ball_pnt<0 and rect_form(recty_ball).colliderect(rect_form(recty))==False:
                    recty_ball.x=recty_ball.x+recty_ball_pnt
                    if recty_ball.x<0 or recty_ball.x+recty.L>recty_bar.x+1:
                        recty_ball.x=recty_ball.x-recty_ball_pnt

        if keys[pygame.K_h] and frame==1 and key_h==1:
            screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE|pygame.NOFRAME)
            frame=0

        elif keys[pygame.K_h] and frame==0 and key_h==1:
            screen=pygame.display.set_mode((screen_size[0],screen_size[1]),pygame.RESIZABLE)
            frame=1

        if key_UP>1 or key_LEFT>1:
            for i in range(recty.speed):
                if recty.y>0:
                    recty.y=recty.y-1

        if key_DOWN>1 or key_RIGHT>1:
            for i in range(recty.speed):
                if recty.y<screen_size[1]-recty.l:
                    recty.y=recty.y+1

        if recty_ball_free[0]==0:
            recty_ball=Rect(20,20,recty.x+recty.L+5,recty.y+recty.l/2-10,white_color,recty_ball.speed)

        if key_g==1 or state==0:
            #print("-Reboot-")

            recty=Rect(93,20,10,screen_size[1]/2-10,recty.color,15)
            recty_bar=Rect(93,20,screen_size[0]-10-20,screen_size[1]/2-10,recty_bar.color)
            recty_ball=Rect(20,20,recty.x+recty.L+5,recty.y+recty.l/2-10,recty_bar.color,recty_ball.speed)
            strtd=0
            recty_ball_free[0]=0
            key_f_SPACE=0
            recty_ball_pnt_u=0
            state=1
            launch=0

        key_h=[key_h]
        key_UP=[key_UP]
        key_DOWN=[key_DOWN]
        key_SPACE=[key_SPACE]
        key_RIGHT=[key_RIGHT]
        key_LEFT=[key_LEFT]
        key_z=[key_z]
        key_s=[key_s]
        key_g=[key_g]
        #key_g=[key_g]

    except pygame.error:
        pass