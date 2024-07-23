from env_2D import World_2D
import numpy as np
import pandas as pd
import time
from debug import d_print

total_num_episode = 100
epsilon = 0.9 # 90%选择最优
alpha = 0.1 # lr
Lambda = 0.9 # 未来奖励衰减值
fresh_time = 0.02 # 刷新时间
world_len = 10 # 世界的长度
actions = ['LEFT', 'RIGHT']
continous_or_not = True

class Q_Policy:
    def __init__(self, q_table):
        self.q_table = q_table

    def choose_action(self, curr_state):
        state_actions = q_table.iloc[curr_state, :]
        if np.random.uniform() > epsilon or state_actions.iloc[0] == state_actions.iloc[1]:
            action_chosen = np.random.choice(actions)
        else:
            action_chosen = state_actions.idxmax()
        return action_chosen
    
    def update_q_table(self, pre_state, curr_state, curr_action, curr_reward):
        curr_predict = self.q_table.loc[pre_state, curr_action]
        if curr_state != world_len - 1:
            curr_real = curr_reward + Lambda * self.q_table.loc[curr_state, :].max()
        else:
            curr_real = curr_reward

        self.q_table.loc[pre_state, curr_action] += alpha * (curr_real - curr_predict)
    


if __name__ == '__main__':
    environ = World_2D(world_len)

    if continous_or_not:
        q_table = pd.read_pickle('save.pkl')
    else:
        q_table_np = np.zeros((world_len, len(actions)))
        q_table = pd.DataFrame(
            q_table_np,
            columns = actions
        )

    policy = Q_Policy(q_table)
    d_print(policy.q_table)

    curr_episode = 0
    while curr_episode < total_num_episode:
        curr_episode += 1
        counter_step = 0

        curr_state = environ.reset()
        d_print(f"the first state: {curr_state}")
        # input("Enter to go to next step")

        done = False
        total_reward = 0
        while not done:
            time.sleep(1)
            counter_step += 1

            pre_state = curr_state[:]
            curr_action = policy.choose_action(curr_state[0])
            curr_state, curr_reward, done = environ.step(curr_action)
            total_reward += curr_reward
            d_print(f"pre_state: {pre_state}, curr_state: {curr_state}, curr_action: {curr_action}, curr_reward: {curr_reward}")
            policy.update_q_table(pre_state[0], curr_state[0], curr_action, curr_reward)
            # d_print(policy.q_table)
            # input("Enter to go to next step")
    
        print(f"=== Episode {curr_episode} ===")
        print(f"total reward = {total_reward}")
        print(f"The current q_table:")
        print(policy.q_table)
        pre_q_table = pd.read_pickle('save.pkl')
        print()
        print("The previous q_table:")
        print(pre_q_table)
        save_or_not = input("Input v to save the current q_table, k to skip the saving")
        if save_or_not == 'v':
            policy.q_table.to_pickle('save.pkl')
        else:
            pass
        