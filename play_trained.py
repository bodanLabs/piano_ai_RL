
from stable_baselines3 import PPO
from piano_env import PianoEnv
import time

# Load environment and trained model
env = PianoEnv()
model = PPO.load("ppo_piano_agent")

obs = env.reset()[0]
done = False

print("🎵 Playing melody with trained AI...")

while not done:
    action, _ = model.predict(obs)
    obs, reward, done, truncated, _ = env.step(action)
    time.sleep(0.5)  # Delay to let sound and visuals sync
