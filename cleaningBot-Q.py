import numpy as np
import random
from env import GridWorld

def d_print(str):
    print(f"{str}")

def train_q_learning(episodes, alpha=0.1, gamma=0.99, epsilon=0.1):
    q_table = np.zeros((10, 10, 4))
    for episode in range(episodes):
        state = environ.reset()
        done = False
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.randint(0, 3)
            else:
                action = np.argmax(q_table[state[0], state[1]])

            new_state, reward, done = environ.step(action)
            old_value = q_table[state[0], state[1], action]
            future_optimal_value = np.max(q_table[new_state[0], new_state[1]])
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * future_optimal_value)
            q_table[state[0], state[1], action] = new_value
            state = new_state

    return q_table

if __name__ == '__main__':
    environ = GridWorld(size=10)
    print("最优值函数：")
    print(V_optimal)