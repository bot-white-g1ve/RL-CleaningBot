# 环境设置
class GridWorld:
    def __init__(self, size=10):
        self.size = size
        self.reset()

    def reset(self):
        # 初始化起点，确保不是右下角
        while True:
            self.position = [random.randint(0, self.size-1), random.randint(0, self.size-1)]
            if self.position != [self.size-1, self.size-1]:
                break
        return self.position
    
    def step(self, action):
        # action: 0=上, 1=下, 2=左, 3=右
        if action == 0 and self.position[0] > 0:
            self.position[0] -= 1
        elif action == 1 and self.position[0] < self.size - 1:
            self.position[0] += 1
        elif action == 2 and self.position[1] > 0:
            self.position[1] -= 1
        elif action == 3 and self.position[1] < self.size - 1:
            self.position[1] += 1

        reward = -1
        done = False
        if self.position == [self.size-1, self.size-1]:
            reward = 10
            done = True

        return self.position, reward, done