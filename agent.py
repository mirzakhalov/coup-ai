import random

class Agent:
    def __init__(self):
        self.model = None
        self.action_count = 0

    def act(self, state):
        # TODO feedforward through model
        self.action_count += 1
        # TODO add to memory
        return random.randint(0,6)
