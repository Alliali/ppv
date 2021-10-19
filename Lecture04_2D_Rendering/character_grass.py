from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')
while True:
    x = 400
    while x < 800:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x+=2
        delay(0.01)

    y = 90
    while y < 600:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y)
        y+=2
        delay(0.01)

    x = 780
    while x > 20:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 600)
        x-=2
        delay(0.01)

    y = 600
    while y > 90:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(20, y)
        y-=2
        delay(0.01)
    
    x = 20
    while x < 400:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x+=2
        delay(0.01)
    
    x=-90
    while x<270:
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(400+250*(math.cos(x*3.14/180)),330+250*(math.sin(x*3.14/180)))
        x+=2
        delay(0.01)
    




