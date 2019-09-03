import random

class Agent:
    def __init__(self):
        self.model = None
        self.action_count = 0

    def act(self, state, valid_actions):
        # TODO feedforward through model
        self.action_count += 1
        # TODO add to memory
        return random.randint(0,6), random.randint(0,4)
