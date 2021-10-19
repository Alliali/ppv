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

class Bigball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(100, 700), 599

    def update(self):   # 소년의 행위 구현.
        self.y -= random.randint(5, 15)

    def draw(self):
        self.image.clip_draw(0, 0, 43, 43, self.x, self.y)


class Smallball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(100, 700), 599

    def update(self):   # 소년의 행위 구현.
        # if self.y == 30:
        self.y -= random.randint(5, 15)

    def draw(self):
        self.image.clip_draw(0, 0, 43, 43, self.x, self.y)



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
# boy = Boy()
bigball = Bigball()
smallball = Smallball()



team = [ Boy() for i in range(11) ]

team2 = [ Bigball() for j in range(10) ]

team3 = [ Smallball() for z in range(10) ]



running = True

# game main loop code
while running:

    handle_events() # 키 입력 받아들이는 처리..

    # Game logic
    # grass에 대한 상호작용 하지만 잔디에 상호작용할게 지금은 없기에 패스
    for boy in team:
        boy.update()    #소년의 상호작용
    for bigball in team2:
        bigball.update()
    for smallball in team3:
        smallball.update()

            # Game drawing
    clear_canvas()
    grass.draw()
    for boy in team:
        boy.draw()
    for bigball in team2:
        bigball.draw()
    for smallball in team3:
        smallball.draw()
    update_canvas()

    delay(0.05)

# finalization code

