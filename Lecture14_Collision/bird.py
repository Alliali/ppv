import game_framework
from pico2d import *
import random

import game_world

#
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

#
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14



class Bird:
    image = None
    def __init__(self):
        if Bird.image == None:
            Bird

        self.x, self.y = random.randint(100, 1400), random.randint(400, 550)
        self.image = load_image('bird100x100x14.png')
        self.frame = 0
        self.dir = 1
        self.velocity = RUN_SPEED_PPS
        self.x = clamp(25, self.x, 1600 - 25)


    def update(self):
        self.x += self.velocity * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

    def get_bb(self):
        return 0, 0, 0, 0
