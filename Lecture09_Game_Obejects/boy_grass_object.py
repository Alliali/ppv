import random
from pico2d import *

# Game object class here

class Grass:
    def __init__(self):     # 생성자 객체에 대한 초기값
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.image = load_image('animation_sheet.png')
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)

    def update(self):   # 소년의 행위 구현.
        self.x += 5 # 속성값을 바꿈으로써, 행위(오른쪽으로 이동)를 구현.
        self.frame = (self.frame + 1) % 8

    def draw(self):
        self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)





def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code

open_canvas()

grass = Grass() # 잔디 객체를 생성
boy = Boy()


team = [ Boy() for i in range(11) ]



running = True

# game main loop code
while running:

    handle_events() # 키 입력 받아들이는 처리..

    # Game logic
    # grass에 대한 상호작용 하지만 잔디에 상호작용할게 지금은 없기에 패스
    for boy in team:
        boy.update()    #소년의 상호작용

    # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    update_canvas()

    delay(0.05)

# finalization code

