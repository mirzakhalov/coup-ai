

class Player:
    def __init__(self, cards=[0,0], coins=2, name="Bot", is_bot=True, agent=None):
        self.cards = cards
        self.coins = coins
        self.name = name
        self.is_bot = is_bot
        self.agent = agent

    def get_action(self, state, valid_actions):
        action = self.agent.act(state, valid_actions)
        
        return action

    def get_challenge(self, state, active_player, action, target_player):
        return 1

    def lose_card(self):
        # Decides what card to lose and loses it
        card_pos = 0
        del self.cards[card_pos]

    def fake_lose_card(self, state, card):
        will_fake = False
        return will_fake

    def choose_cards(self, state):
        index1, index2 = 0, 1

        card1 = self.cards[index1]
        card2 = self.cards[index2]

        del self.cards[index1]
        del self.cards[index2]

        return [card1, card2]

    def show_card(self, card):
        if self.cards[0] == card:
            del self.cards[0]
        else:
            del self.cards[1]
