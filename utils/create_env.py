import gym
from gym import Env
from gym.spaces import Discrete, Box, Dict, Tuple, MultiBinary, MultiDiscrete
import numpy as np
import random
import os


class FarmEnv(Env):
    def __init__(self):
        # Actions we can take, change temperature, pH, and water individually
        self.action_space = Box(low=np.array([-1, -0.5, -5]), high=np.array([1, 0.5, 5]))
        # Observation space (temperature, pH, water)
        self.observation_space = Box(low=np.array([0, 0, 0]), high=np.array([100, 14, 100]))
        # Set start values
        self.state = np.array([38 + random.randint(-3, 3), 7 + random.uniform(-0.5, 0.5), 50 + random.uniform(-10, 10)])
        # Set day length
        self.day_length = 60

    def step(self, action):
        # Clip action values to be within action space
        action = np.clip(action, self.action_space.low, self.action_space.high)

        # Apply action
        self.state += action

        # Clip values to be within observation space
        self.state = np.clip(self.state, self.observation_space.low, self.observation_space.high)

        # Reduce length by 1 second
        self.day_length -= 1

        # Calculate reward
        temp_reward = 1 if 37 <= self.state[0] <= 39 else -1
        ph_reward = 1 if 6.5 <= self.state[1] <= 7.5 else -1
        water_reward = 1 if 45 <= self.state[2] <= 55 else -1
        reward = temp_reward + ph_reward + water_reward

        # Check if day is done
        done = self.day_length <= 0

        # Set placeholder for info
        info = {}

        # Return step information
        return self.state, reward, done, info

    def render(self):
        # Implement viz
        pass

    def reset(self):
        # Reset farm values
        self.state = np.array([38 + random.randint(-3, 3), 7 + random.uniform(-0.5, 0.5), 50 + random.uniform(-10, 10)])
        # Reset day time
        self.day_length = 60
        return self.state


# Create environment
def create_env():
    return FarmEnv()
