import random

class Agent:
    def __init__(self):
        self.model = None
        self.action_count = 0

    def act(self, state, valid_actions):
        # TODO feedforward through model
        self.action_count += 1
        # TODO add to memory
        action_type, target_player, _, is_challenge = random.choice(valid_actions)
        
        return ([action_type, target_player], is_challenge)
