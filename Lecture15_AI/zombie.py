import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *

import server

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]


    def prepare_patrol_points(self):
        # fill here
        positions = [(43, 750), (1118, 750), (1050, 530), (575, 200), (235, 33), (575, 200), (1050, 530), (1118, 750)]
        self.patrol_points = []
        for p in positions:
            self.patrol_points.append((p[0], 1024-p[1])) #pico2d 상의 좌표계를 이용하도록 변경
        pass


    def __init__(self):
        self.prepare_patrol_points()
        self.patrol_order = 1
        self.x, self.y = self.patrol_points[0]  #초기위치
        self.load_images()
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 10.0 # change direction every 1 sec when wandering
        self.wait_timer = 2.0
        self.frame = 0
        self.build_behavior_tree()




    def wander(self):                                   #배회
        self.speed = RUN_SPEED_PPS
        self.timer -= game_framework.frame_time
        if self.timer <= 0:
            self.timer = 10.0
            self.dir = random.random() * 2 * math.pi  #방향을 라디안값으로 설정
            print('Wander Success')
            return BehaviorTree.SUCCESS
        return BehaviorTree.SUCCESS
        # else:                                       #배회중에도 찾고싶다면 RUNNING을 하면 안됨 항상 SUCCESS여야함
        #     return BehaviorTree.RUNNING

        # fill here
        pass


    def wait(self):
        # fill here
        self.speed = 0
        self.wait_timer -= game_framework.frame_time
        if self.wait_timer <= 0:
            self.wait_timer = 2.0
            print('Wait Success')
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass



    def find_player(self):
        # fill here
        distance2 = (server.boy.x - self.x)**2 + (server.boy.y - self.y)**2
        if distance2 <= (PIXEL_PER_METER*10)**2:
            print('Find Player Success')
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL

    def move_to_player(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.dir = math.atan2(server.boy.y - self.y, server.boy.x - self.x)
        return BehaviorTree.SUCCESS #일단, 소년쪽으로 움직이기만 해도 성공으로 여긴다.


    def get_next_position(self):
        # fill here
        self.target_x, self.target_y = self.patrol_points[self.patrol_order % len(self.patrol_points)] #순환되어야하기 때문에
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)
        print('Next Position Found Success')
        return BehaviorTree.SUCCESS

    def move_to_target(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        distance2 = (self.target_x - self.x)**2 + (self.target_y - self.y)**2

        if distance2 <= PIXEL_PER_METER**2: # 거리가 1미터 이내이면
            print('Moved to Target Success')
            return BehaviorTree.SUCCESS #다 왔다
        else:
            # print('Moving to Target')
            return BehaviorTree.RUNNING




    def build_behavior_tree(self):
        wander_node = LeafNode('Wander', self.wander)       #리프노드를 만듬
        wait_node = LeafNode('Wait', self.wait)

        wander_wait_node = SequenceNode('WanderAndWait')    #원더노드와 웨윗노드를 가지고 있는 시퀀스 노드
        wander_wait_node.add_children(wander_node, wait_node)  #트리구조를 만든것

        get_next_position_node = LeafNode('Get Next Position', self.get_next_position)
        move_to_target_node = LeafNode('Move to Target', self.move_to_target)
        patrol_node = SequenceNode('Patrol')
        patrol_node.add_children(get_next_position_node, move_to_target_node)

        find_player_node = LeafNode('Find Player', self.find_player)
        move_to_player_node = LeafNode('Move to Player', self.move_to_player)
        chase_node = SequenceNode('Chase')
        chase_node.add_children(find_player_node, move_to_player_node)

        chase_wander_node = SelectorNode('Chase or Wander')
        chase_wander_node.add_children(chase_node, wander_node)

        self.bt = BehaviorTree(chase_wander_node)                 #BehaviroTree에 root노드로 지정해서 bt를 만들어주면 된다.
        # fill here                                         #self.bt는 wander노드를 루트로 하는 bt이다




    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        # fill here
        self.bt.run() #매프레임마다 bt를 실행
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)


    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

    def handle_event(self, event):
        pass

