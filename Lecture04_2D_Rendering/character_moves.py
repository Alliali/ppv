from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
    

x=-90
while x<270:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(400+250*(math.cos(x*3.14/180)),330+250*(math.sin(x*3.14/180)))
    x+=2
    delay(0.01)
