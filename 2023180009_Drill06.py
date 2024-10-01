from pico2d import *

open_canvas()
grass = load_image('TUK_GROUND.png')
character = load_image('run_animation.png')

frame = 0

for x in range(0, 800, 10):
 clear_canvas()
 grass.draw(800 // 2, 600 // 2, 800, 600)
 character.clip_draw(frame * 100, 0, 100, 100, x, 90)
 update_canvas()
 frame = (frame + 1) % 8
 delay(0.05)


close_canvas()
