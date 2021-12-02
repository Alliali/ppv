import pickle

class npc:
    def __init__(self, name, x, y):
        self.name, self.x, self.y = name, x, y

yuri = npc('yuri', 100, 200)

with open('yuri.pickle', 'wb') as f:
    pickle.dump(yuri, f)

with open('yuri.pickle', 'rb') as f:
    read_yuri = pickle.load(f)


print(read_yuri)
print(read_yuri.name, read_yuri.x, read_yuri.y)