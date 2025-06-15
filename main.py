
from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env
from piano_env import PianoEnv
import os
from threading import Thread
from visual_piano import visual_loop
from stable_baselines3.common.callbacks import EvalCallback



Thread(target=visual_loop, daemon=True).start()

env = PianoEnv()
check_env(env)

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=2_500_000)

model.save("ppo_piano_agent")
