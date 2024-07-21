import random
class World_2D:
    def __init__(self, len):
        self.size = len
    
    def reset(self):
        while True:
            self.position = [random.randint(0, self.size-1)]
            if self.position != [self.size-1]:
                break
        return self.position

    def step(self, action):
        if action == '0' and self.position != [0]:
            self.position[0] -= 1
        elif action == '1' and self.position != [self.size-1]:
            self.position[0] += 1
        
        step_reward = 1
        done = False
        if self.position[0] == 