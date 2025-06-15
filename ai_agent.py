
import random

class Agent:
    def __init__(self, n_actions, epsilon=1.0):
        self.n_actions = n_actions
        self.epsilon = epsilon
        self.min_epsilon = 0.01
        self.decay = 0.995
        self.q_table = {}

    def decay_epsilon(self):
        self.epsilon = max(self.min_epsilon, self.epsilon * self.decay)

    def choose_action(self, state):
        if random.random() < self.epsilon:
            return random.randint(0, self.n_actions - 1)
        return self.best_action(state)

    def best_action(self, state):
        state_qs = self.q_table.get(state, [0] * self.n_actions)
        return int(state_qs.index(max(state_qs)))

    def learn(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = [0] * self.n_actions
        if next_state not in self.q_table:
            self.q_table[next_state] = [0] * self.n_actions

        alpha = 0.1
        gamma = 0.9
        predict = self.q_table[state][action]
        target = reward + gamma * max(self.q_table[next_state])
        self.q_table[state][action] += alpha * (target - predict)
