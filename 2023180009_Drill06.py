import random
from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')
curser = load_image('hand_arrow.png')


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass

def make_random():
    global  curserX, curserY
    curserX, curserY = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)

running = True
arrive = True

x, y = TUK_WIDTH//2, TUK_HEIGHT//2
curserX, curserY = random.randint(0, TUK_WIDTH), random.randint(0, TUK_HEIGHT)
frame = 0
dir = 0
dir2 = 0

arrive = False

while running:
    dir_x = curserX - x
    dir_y = curserY - y
    clear_canvas()
    if curserX> x:
        dir = 1
    elif curserX < x :
        dir = -1
    if curserY > y:
        dir2 = 1
    elif curserY <y:
        dir2 = -1

    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    curser.draw(curserX, curserY)
    if arrive == False:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif arrive == True:
        make_random()
    update_canvas()
    frame = (frame + 1) % 8
    if dir_x !=0 or dir_y != 0:
        x += dir * 5
        y += dir2 * 5
    else:
        arrive = True
    delay(0.05)
    handle_events()

close_canvas()




