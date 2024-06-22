##tetris_bot

import pygame
import keyboard
import time
import random

#Add panick mode when too high
#Add left or right once on ground
#Creategrid texture, blit it to scren, blit current to screen, when gird and/or extra changes, update_texture()
#Score of 628 with seed 569802715.
#Score of 0 with seed 483040011?
#Make seed print a press-only thing

pygame.mixer.init()

class Audio:

    def play_sound(file,volume=1):

        sound=pygame.mixer.Sound(f"example_file_3_files/audio_files/{file}")
        sound.set_volume(volume)
        sound.play()

    def play_switch_sound(volume=0.3):
        Audio.play_sound("switch.wav",volume)

    def play_press_sound(volume=0.15):
        Audio.play_sound("press.wav",volume)

    def play_line_clear_sound(volume=0.05):
        Audio.play_sound("line_clear.wav",volume)

    def play_death_sound(volume=0.35):

        pygame.mixer.music.load("example_file_3_files/audio_files/death.wav")
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(1)

def file(mode,command):
    with open("model.txt",mode) as file:
        return(eval(command))

def setup():

    screen_size=(400,500)
    screen_=lambda: (screen_size,pygame.RESIZABLE)
    screen=pygame.display.set_mode(*screen_())

    title="tetris_bot"
    pygame.display.set_caption(title)

    pygame.display.set_icon(pygame.Surface((0,0)))

    g=150
    grey_color=(g,g,g)

    background_color=grey_color

    colors={0: (22,)*3,"t": (190,0,255),"b": (0,240,240),"s": (240,240,0),
            "e": (0,240,0),"E": (240,0,0),"l": (0,0,240),"L": (240,160,0)}

    vlr=22
    width=10
    height=20

    gap=1

    grid=[]
    rects=[]

    for y in range(height):
        grid.append([])
        rects.append([])
        for x in range(width):
            rects[y].append(pygame.Rect(x*vlr+gap,y*vlr+gap,vlr-gap,vlr-gap))
            grid[y].append(0)

    #screen_size=(width*vlr+gap,height*vlr+gap)

    rects_offset=(vlr*round(screen_size[0]/(vlr*3)),vlr*2)

    for line in rects:
        for rect in line:
            rect.x=rect.x+rects_offset[0]
            rect.y=rect.y+rects_offset[1]

    extra_offset=(vlr,vlr*2)

    extra_rects=[]
    extra_grid=[]
    for y in range(4):
        extra_rects.append([])
        extra_grid.append([])
        for x in range(4):
            extra_rects[y].append(pygame.Rect(vlr*x+gap+extra_offset[0],vlr*y+gap+extra_offset[1],vlr-gap,vlr-gap))
            extra_grid[y].append(0)

    tick_delay=0.3
    last_tick=0

    vertfact=5.9
    horfact=0.73525
    heightfact=3.768
    avrfact=4.6

    dejavu=True

    model={'vert': 2.360993244661562, 'hor': 4.718923711326337, 'height': -0.376481959028403, 'avr': 5.01237372218012}

    textures={key: pygame.image.load(f"example_file_3_files/image_files/{i}.png") for i,key in (("b","b"),("L2","L"),
                                                                          ("l","l"),("E2","E"),
                                                                          ("e","e"),("t","t"),
                                                                          ("s","s"),("bland","bland"))}

    for key in textures:
        textures[key]=pygame.transform.scale(textures[key],(vlr,)*2)

    screen_size=[round(i/vlr)*vlr for i in screen_size]
    aqua=pygame.Surface(screen_size)

    for y in range(int(screen_size[1]/vlr)):
        for x in range(int(screen_size[0]/vlr)):
            aqua.blit(textures["bland"],(x*vlr+gap,y*vlr+gap))

    vertfact=model["vert"]
    horfact=model["hor"]
    heightfact=model["height"]
    avrfact=model["avr"]
    died=False

    score=0
    abort=False
    launched=True

    random.seed(seed:=random.randrange(int(1e+9)))

    fancy=True

    pygame.font.init()
    tetris_font=pygame.font.Font("example_file_3_files/font_file/modern-tetris.ttf",13)
    font_offset=(vlr,vlr*7)
    font_rects=[]
    font_pos=(vlr*1.5,vlr*7.5)

    for y in range(int(height/10)):
        for x in range(int((width/10)*4)):
            font_rects.append(pygame.Rect(x*vlr+gap+font_offset[0],y*vlr+gap+font_offset[1],vlr,vlr))

    values=("screen","screen_","screen_size","title","g","grey_color","background_color","colors","vlr","width","height",
            "gap","grid","rects","rects_offset","extra_rects","extra_grid","tick_delay","last_tick","vertfact","horfact",
            "heightfact","score","abort","avrfact","died","textures","aqua","seed","fancy","tetris_font","font_rects",
            "font_offset","font_pos","launched","dejavu")

    for value in values:
        globals()[value]=eval(value)

def init():

    vects={"t": tP,"b": bP,"s": sP,"e": eP,"E": EP,"l": lP,"L": LP}
    current={"type": random.choice(tuple(vects.keys())),"pos": [4,0],"rotation": 0}
    extra=random.choice(tuple(vects.keys()))

    for value in ("vects","current","extra"):
        globals()[value]=eval(value)

    update_best()

def get_rect_at(x,y):

    if 0<=x<width and 0<=y<height:
        return(rects[y][x])

def get_grid_at(x,y):

    if 0<=x<width and 0<=y<height:
        return(grid[y][x])

tP=[[(1,1),(0,1),(1,0),(2,1)],
    [(1,1),(1,2),(1,0),(2,1)],
    [(0,1),(1,1),(2,1),(1,2)],
    [(0,1),(1,1),(1,0),(1,2)]]

bP=[[(0,i) for i in range(4)],[(i,0) for i in range(4)]]*2

sP=[[(0,0),(1,0),(1,1),(0,1)] for i in range(4)]

eP=[[(1,1),(2,1),(0,2),(1,2)],
    [(0,0),(0,1),(1,1),(1,2)]]*2

EP=[[(0,1),(1,1),(1,2),(2,2)],
    [(2,0),(1,1),(2,1),(1,2)]]*2

lP=[[(1,0),(2,0),(1,1),(1,2)],
    [(0,1),(1,1),(2,1),(2,2)],
    [(1,0),(1,1),(0,2),(1,2)],
    [(0,0),(0,1),(1,1),(2,1)]]

LP=[[(0,0),(1,0),(1,1),(1,2)],
    [(2,0),(0,1),(1,1),(2,1)],
    [(1,0),(1,1),(1,2),(2,2)],
    [(0,1),(1,1),(2,1),(0,2)]]

def maybe_go_sideways():
    return(None)
    print("\n".join(["".join(["." if i else "O" for i in line]) for line in grid]))

def try_to_go(x,y):

    current["pos"][0]=current["pos"][0]+x
    current["pos"][1]=current["pos"][1]+y

    new_rects=[]

    for vect in vects[current["type"]][current["rotation"]]:

        pos=[v+p for v,p in zip(vect,current["pos"])]
        new_rects.append(get_grid_at(*pos))

    if new_rects.count(0)!=len(new_rects):

        current["pos"][0]=current["pos"][0]-x
        current["pos"][1]=current["pos"][1]-y

        maybe_go_sideways()

        return(False)

    return(True)

def rotate():

    current["rotation"]=current["rotation"]+1

    if current["rotation"]>=4:
        current["rotation"]=0

def display_current():

    for vect in vects[current["type"]][current["rotation"]]:

        pos=[v+p for v,p in zip(vect,current["pos"])]
        rect=get_rect_at(*pos)

        if rect:
            pygame.draw.rect(screen,colors[current["type"]],rect)
            if fancy:
                screen.blit(textures[current["type"]],rect[:2])

def get_shadow_rects():

    global current

    currentstr=str(current)
    old_rects=[]

    while True:

        current["pos"][1]=current["pos"][1]+1
        new_rects=[]
        new_rects_rects=[]

        for vect in vects[current["type"]][current["rotation"]]:

            pos=[v+p for v,p in zip(vect,current["pos"])]
            new_rects.append(get_grid_at(*pos))
            new_rects_rects.append(pos)

        if new_rects.count(0)!=len(new_rects):

            current["pos"][1]=current["pos"][1]-1
            break

        old_rects=new_rects_rects.copy()

    current=eval(currentstr)

    return(old_rects)

def get_shadow_grid_at(x):

    global current

    True_current=str(current)
    current["pos"][0]=x

    fake_grid=eval(str(grid))
    rects=get_shadow_rects()
    rects=[rect for rect in rects if rect]
    current=eval(True_current)

    if not rects:
        return(None)

    for rect in rects:
        if rect:
            fake_grid[rect[1]][rect[0]]="t"

    for y,line in enumerate(fake_grid):
        for x,n in enumerate(line):
            if n:
                fake_grid[y][x]=1

    lines=0

    for i,line in enumerate(fake_grid):

        if not line.count(0):

            fake_grid[i]=[0 for i in range(width)]
            lines=lines+1

            while True:
                try:

                    fake_grid[i-1],fake_grid[i]=fake_grid[i],fake_grid[i-1]
                    i=i-1

                    if i<=0:
                        break

                except IndexError:
                    break

    #fake_grid="\n".join([" ".join([str(I) for I in i]) for i in fake_grid])

    return(fake_grid)

def get_shadow_grids(orientation=0):

    global current

    True_current=str(current)
    current["rotation"]=orientation
    shadow_grids=[]

    for i in range(width):
        sha=get_shadow_grid_at(i)
        if sha:
            shadow_grids.append((i,sha))

    current=eval(True_current)

    return(shadow_grids)

def check_for_clears():

    global score

    lines=0

    for i,line in enumerate(grid):

        if not line.count(0):

            score=score+1

            grid[i]=[0 for i in range(width)]
            lines=lines+1

            while True:
                try:

                    grid[i-1],grid[i]=grid[i],grid[i-1]
                    i=i-1

                    if i<=0:
                        break

                except IndexError:
                    break

def eval_grid(grid):

    highest=height-1
    grid_value=0
    pillars=None
    vert_holes=0
    hor_holes=0
    average=[]

    for y,line in enumerate(grid):
        for g in line:
            if g:
                average.append(y)

    average=sum(average)/len(average) if len(average) else 0

    for x in range(10):
        b=False
        for y in range(20):
            if grid[y][x]:

                b=True

                if y<highest:
                    highest=y

            if not grid[y][x] and b:
                vert_holes=vert_holes+1

    for y in range(20):
        b=False
        for x in range(10):
            if not grid[y][x] and y>=highest:
                hor_holes=hor_holes+1

    hor_holes=1/hor_holes if hor_holes else 1
    vert_holes=1/vert_holes if vert_holes else 1

    grid_value=vert_holes*vertfact+hor_holes*horfact+(highest/20)*heightfact+average*avrfact

    return(grid_value)

display_shadow=lambda: [pygame.draw.rect(screen,"white",get_rect_at(*rect)) for rect in get_shadow_rects() if rect]

def update_best():

    global best_x
    global current_best
    global best_angle
    global toggle_best
    global current
    global extra

    True_current=str(current)

    best_x=None
    current_best=None
    best_angle=None
    toggle_best=None
    change_type=False

    for ori in range(4):
        for x,shgrid in get_shadow_grids(ori):
            if not current_best or eval_grid(shgrid)>eval_grid(current_best):
                current_best=shgrid
                best_x=x
                best_angle=ori

    current["type"]=extra

    for ori in range(4):
        for x,shgrid in get_shadow_grids(ori):
            if not current_best or eval_grid(shgrid)>eval_grid(current_best):
                current_best=shgrid
                best_x=x
                best_angle=ori
                change_type=True

    current=eval(True_current)

    if change_type:
        current["type"],extra=extra,current["type"]
        Audio.play_switch_sound()

def do_best():

    global best_x
    global current_best
    global best_angle
    global launched

    try:
        if current["pos"][0]<best_x:
            current["pos"][0]=current["pos"][0]+1
            Audio.play_press_sound()
        elif current["pos"][0]>best_x:
            current["pos"][0]=current["pos"][0]-1
            Audio.play_press_sound()
        else:
            try_to_go(0,1)
    except TypeError:
        launched=False
        best_angle=0

    current["rotation"]=best_angle

def display_extra():

    global extra

    for y,line in enumerate(extra_rects):
        for x,rect in enumerate(line):
            pygame.draw.rect(screen,colors[0],rect)

    for vect in vects[extra][0]:
        pygame.draw.rect(screen,colors[extra],extra_rects[vect[1]][vect[0]])
        if fancy:
            screen.blit(textures[extra],extra_rects[vect[1]][vect[0]][:2])

def display_score():

    for rect in font_rects:
        pygame.draw.rect(screen,colors[0],rect)

    screen.blit(tetris_font.render(str(score),False,(255,)*3),font_pos)

def screen_lock():
    screen=pygame.display.set_mode(*screen_())

def title_screen():

    global abort
    global launched

    big_font=pygame.font.Font("example_file_3_files/font_file/modern-tetris.ttf",vlr*2)
    smol_font=pygame.font.Font("example_file_3_files/font_file/modern-tetris.ttf",int(vlr/1.5))

    screen_lock()

    n=0
    color=colors[random.choice(tuple(colors.keys())[1:])]
    while not keyboard.is_pressed("enter"):

        title_frame_start=time.perf_counter()

        n=n+1

        if not n%int(60/7):
            color=colors[random.choice([i for i in tuple(colors.keys())[1:] if colors[i]!=color])]

        screen.blit(aqua,(0,0))
        screen.blit(big_font.render("Tetris",False,color),(vlr*4.2,vlr*7))
        screen.blit(smol_font.render("Press ENTER",False,color),(vlr*6,vlr*12))

        pygame.display.flip()

        for event in pygame.event.get():

            if event.type==pygame.QUIT:

                abort=True
                launched=False
                pygame.quit()
                quit()

                break

            if event.type==pygame.VIDEORESIZE:
                screen_lock()

        while time.perf_counter()-title_frame_start<1/60:
            pass

Set=0
def main():

    global last_tick
    global launched
    global died

    if not Set:

        screen.fill(background_color)
        if fancy:
            screen.blit(aqua,(0,0))

        do_best()

        if last_tick<=time.perf_counter():
            last_tick=time.perf_counter()+tick_delay
            try_to_go(0,1)

        check_for_clears()

        if not display_shadow():

            for vect in vects[current["type"]][current["rotation"]]:

                pos=[v+p for v,p in zip(vect,current["pos"])]

                if grid[pos[1]][pos[0]]:
                    launched=False
                    died=True

                grid[pos[1]][pos[0]]=current["type"]

            current["pos"]=[4,0]
            current["type"]=random.choice(tuple(colors.keys())[1:])

            check_for_clears()
            update_best()

        for y,line in enumerate(rects):
            for x,rect in enumerate(line):
                pygame.draw.rect(screen,colors[grid[y][x]],rect)
                if grid[y][x] in tuple(textures.keys()) and fancy:
                    screen.blit(textures[grid[y][x]],(rect[:2]))

        display_current()
        display_extra()
        display_score()

        pygame.display.flip()

        if keyboard.is_pressed("r"):
            print(seed)

def launch():

    global launched
    global abort

    if launched is not False:
        launched=True
        print(f"[{launched=}]")

    try:
        while launched:

            frame_start=time.perf_counter()
            main()
            while not dejavu and time.perf_counter()-frame_start<1/20:
                pass

            if any([event.type==pygame.QUIT for event in pygame.event.get()]):
                launched=False
    except KeyboardInterrupt:
        print("*** Manual Shutdown ***")
        launched=False
        abort=True

    print(f"[{launched=}]")
    pygame.quit()

    if died:
        pygame.mixer.init()
        Audio.play_death_sound()
    else:
        pygame.quit()
        quit()

    vects={"t": tP,"b": bP,"s": sP,"e": eP,"E": EP,"l": lP,"L": LP}
    current={"type": random.choice(tuple(colors.keys())[1:]),"pos": [4,0],"rotation": 0}
    extra=random.choice(tuple(colors.keys())[1:])

if __name__=='__main__':

    while True:

        setup()
        title_screen()
        init()
        launch()

        print(f"Score of {score} with seed {seed}.")