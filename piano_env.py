
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from melody_reward import TARGET_MELODY, compute_reward
from utils import play_note

class PianoEnv(gym.Env):
    def __init__(self):
        super(PianoEnv, self).__init__()
        self.notes = ['C4', 'D4', 'E4', 'F4', 'G4', 'A4', 'B4',
              'C5', 'D5', 'D#5', 'E5']
        self.n_actions = len(self.notes)
        self.action_space = spaces.Discrete(len(self.notes))
        self.observation_space = spaces.Box(low=0, high=self.n_actions, shape=(len(TARGET_MELODY),), dtype=np.int32)
        self.reset()

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.current_step = 0
        self.played_notes = []
        self.state = np.zeros(len(TARGET_MELODY), dtype=np.int32)
        return self.state, {}

    def step(self, action):
        note = self.notes[action]
        self.played_notes.append(note)
        play_note(note)
        self.state[self.current_step] = action
        self.current_step += 1
        done = self.current_step >= len(TARGET_MELODY)
        reward = compute_reward(self.played_notes)
        terminated = done
        truncated = False
        return self.state.copy(), reward, terminated, truncated, {}
