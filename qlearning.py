import random
import pickle
import numpy as np

class Agent:
    def __init__(self, actions, alpha=0.4, gamma=1, epsilon=1.0, epsilon_decay=0.98, epsilon_min=0.05):
        self.q_table = {}
        self.actions = actions
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.epsilon_min = epsilon_min

    def get_key(self, state):
        return str(state)

    def choose_action(self, state):
        state_key = self.get_key(state)
        self.q_table.setdefault(state_key, [0] * len(self.actions))
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(self.actions)

        return int(np.argmax(self.q_table[state_key]))

    def learn(self, state, action, reward, next_state):
        state_key = self.get_key(state)
        next_key = self.get_key(next_state)
        self.q_table.setdefault(state_key, [0] * len(self.actions))
        self.q_table.setdefault(next_key, [0] * len(self.actions))

        predict = self.q_table[state_key][action]
        target = reward + self.gamma * max(self.q_table[next_key])
        self.q_table[state_key][action] += self.alpha * (target - predict)

    def decay_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def save(self, filename='trained_q_table.pkl'):
        with open(filename, 'wb') as file:
            pickle.dump(self.q_table,file)

    def load(self, filename='trained_q_table.pkl'):
        with open(filename, 'rb') as file:
            self.q_table = pickle.load(file)



