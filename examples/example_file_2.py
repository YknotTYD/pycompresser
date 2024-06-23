##pi_approximation

import pygame
import random
import time
import asyncio
import numpy as np

#cache bound surface
#color points in and out differently
#make it two surfaces
#store results in a file?
#don't put a pixel if there is already one?
#simplify the math expression

pygame.init()

screen_size=(800,500)
screen_=lambda: (screen_size,pygame.RESIZABLE)
screen=pygame.display.set_mode(*screen_())

title="pi_approximation"
pygame.display.set_caption(title)

pygame.display.set_icon(pygame.Surface((0,0)))

g=22
grey_color=(g,g,g)

background_color=(25,40,60)

frames=[0 for i in range(60)]

class Bound:

    base_sample_size=15_000

    def __init__(self,pos,size,color=(255,)*3,point_color_out=(200,0,100),point_color_in=(255//2,255,0)):

        self.pos=pos
        self.size=size
        self.color=color
        self.point_color_out=point_color_out
        self.point_color_in=point_color_in

        self.center=tuple(i+self.size/2 for i in self.pos)

        self.fired=0
        self.is_in=0
        self.pi=None
        self.sample_size=Bound.base_sample_size

        self.colors_ways_in=[1,-1,1]
        self.colors_ways_out=[-1,1,-1]

        self.surface=pygame.Surface((self.size,)*2,pygame.SRCALPHA)

    def spawn_point(self):

        self.fired+=self.sample_size

        points=np.random.random((self.sample_size,2))*self.size
        lengths=points-np.array(self.size)/2
        lengths=np.linalg.norm(lengths,axis=1)
        lengths=lengths<=self.size/2

        points_in=points[lengths]
        points_out=points[~lengths]
        self.is_in+=len(points_in)

        import keyboard

        if not keyboard.is_pressed("enter"):

            for point in points_in:
                self.surface.set_at(point,self.point_color_in)
            for point in points_out:
                self.surface.set_at(point,self.point_color_out)

        self.pi=((self.is_in/self.fired)*self.size**2)/(self.size/2)**2

    def update_colors(self):

        self.colors_ways_in=[-i if color>=255 or color<=0 else i
                             for i,color in zip(self.colors_ways_in,self.point_color_in)]
        self.point_color_in=[max(min(i+i_,255),0) for i,i_ in zip(self.point_color_in,self.colors_ways_in)]

        self.colors_ways_out=[-i if color>=255 or color<=0 else i
                             for i,color in zip(self.colors_ways_out,self.point_color_out)]
        self.point_color_out=[max(min(i+i_,255),0) for i,i_ in zip(self.point_color_out,self.colors_ways_out)]

    def display(self,surface=screen):

        surface.blit(self.surface,self.pos)

        pygame.draw.rect(surface,self.color,(*self.pos,*(self.size,)*2),1)
        pygame.draw.circle(surface,self.color,self.center,self.size/2,1)

bound=Bound((175,25),450)

def screen_lock():
    screen=pygame.display.set_mode(*screen_())

scene="main"
def main():

    global scene

    if scene=="main":

        bound.spawn_point()
        bound.update_colors()

        pass#print(f"{bound.fired:_}".replace("_"," "))

        screen.fill(background_color)
        bound.display()

        pygame.display.flip()

async def run():

    launched=True
    print(f"[{launched=}]")

    try:

        while launched:

            frame_start=time.perf_counter()
            main()

            for event in pygame.event.get():

                if event.type==pygame.QUIT:
                    launched=False
                elif event.type==pygame.VIDEORESIZE:
                    screen_lock()
                elif event.type==pygame.MOUSEWHEEL:
                    pass

            frames.append(time.perf_counter()-frame_start)
            del frames[0]

            caption=f"{title} | Fps: {round(1/(sum(frames)/len(frames)))} |"
            caption+=f" Max fps: {round(1/max(frames))}. | bound.pi: {bound.pi}."
            pygame.display.set_caption(caption)

            await asyncio.sleep(0)

            while time.perf_counter()-frame_start<1/60:
                break

    except KeyboardInterrupt:
        print("*** Manual Shutdown ***")
        launched=False

    print(f"[{launched=}]")
    pygame.quit()

asyncio.run(run())