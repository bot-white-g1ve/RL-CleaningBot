import random
import os

class World_2D:
    def __init__(self, len):
        self.size = len
    
    def reset(self):
        while True:
            self.position = [random.randint(0, self.size-1)]
            if self.position != [self.size-1]:
                break
        self.print_world()
        return self.position

    def step(self, action):
        if action == 'LEFT' and self.position != [0]:
            self.position[0] -= 1
        elif action == 'RIGHT' and self.position != [self.size-1]:
            self.position[0] += 1
        
        step_reward = -1
        done = False
        if self.position[0] == self.size-1:
            step_reward = 10
            done = True
        
        self.print_world()
        return self.position, step_reward, done

    def print_world(self):
        os.system('cls')
        world = ['-' for _ in range(self.size)]
        world[self.position[0]] = 'R'
        world[-1] = 'T'
        print(''.join(world))
