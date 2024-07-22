from env_2D import World_2D
import numpy as np
import pandas as pd
import time
from debug import d_print

total_num_episode = 100
epsilon = 0.9 # 90%选择最优
alpha = 0.1 # lr
Lambda = 0.9 # 未来奖励衰减值
fresh_time = 0.3 # 刷新时间
world_len = 10 # 世界的长度
actions = ['LEFT', 'RIGHT']

class Q_Policy:
    def init(self, q_table):
        self.q_table = q_table

    def choose_action(self, curr_state):
        state_actions = q_table.iloc[curr_state, :]
        if np.random.uniform() > epsilon or state_actions


if __name__ == '__main__':
    environ = World_2D(world_len)

    q_table_np = np.zeros((world_len, len(actions)))
    q_table = pd.DataFrame(
        q_table_np,
        columns = actions
    )
    
    d_print(q_table)

    # curr_episode = 0
    # while curr_episode < total_num_episode:
    #     curr_episode += 1
    #     counter_step = 0

    #     start_position = environ.reset()