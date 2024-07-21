import numpy as np
import random
from env import GridWorld

def d_print(str):
    print(f"{str}")

# Use State-Value Function
def value_iteration(env, gamma=0.99, threshold=0.001, log_every=5):
    total_step = 0
    V = np.zeros((env.size, env.size))
    while True:
        delta = 0
        for i in range(env.size):
            for j in range(env.size):
                if [i, j] == [env.size-1, env.size-1]:
                    continue
                v = V[i, j]
                V[i, j] = max(compute_value(env, V, i, j, gamma))
                delta = max(delta, abs(v - V[i, j]))
        total_step += 1
        if total_step % log_every == 0:
            log_V_Matrix(total_step, V)
        if delta < threshold:
            print('Final Step')
            log_V_Matrix(total_step, V)
            break
    d_print(f'total_step used: {total_step}')
    return V

def compute_value(env, V, i, j, gamma):
    actions = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 下、右、上、左
    values = []
    for di, dj in actions:
        ni, nj = i + di, j + dj
        if 0 <= ni < env.size and 0 <= nj < env.size:
            reward = -1 if [ni, nj] != [env.size-1, env.size-1] else 10
            values.append(reward + gamma * V[ni, nj])
        else:
            values.append(-1)
    return values

def log_V_Matrix(total_step, V):
    with open("log.txt", "a") as file:
        file.write(f"After {total_step} steps, V-matrix is:\n{V}\n\n")

if __name__ == '__main__':
    env = GridWorld(size=10)
    V_optimal = value_iteration(env)
    print("最优值函数：")
    print(V_optimal)