import math

from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print('CIRCLE')
    pass                                #일단은 그대로 두고 패스하자

def run_rectangle():
    print('RECTANGLE')
    pass

while True:                             
    run_circle()                        
    run_rectangle()
    break


close_canvas()

    




