

class Player:
    def __init__(self, cards=[0,0], coins=2, name="Bot", is_bot=True, agent=None):
        self.cards = cards
        self.coins = coins
        self.name = name
        self.is_bot = is_bot
        self.agent = agent

    def get_action(self, state):
        if self.is_bot:
            return self.agent.act(state)
        else:
            return int(input("Action [0,6] >> "))