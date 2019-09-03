

class Player:
    def __init__(self, cards=[0,0], coins=2, name="Bot", is_bot=True, agent=None):
        self.cards = cards
        self.coins = coins
        self.name = name
        self.is_bot = is_bot
        self.agent = agent

    def get_action(self, state, valid_actions):
        state = [self.name] + state
        #print("Valid actions: " + str(valid_actions))
        action, _ = self.agent.act(state, valid_actions)
        
        return action

    def get_challenge(self, state, active_player, action, target_player):
        state = [self.name] + state
        if target_player != -1 and not(target_player is None):
            valid_actions = [[active_player.name, action, target_player.name, i] for i in range(2)]
        else:
            valid_actions = [[active_player.name, action, -1, i] for i in range(2)]
        _, is_challenge = self.agent.act(state, valid_actions)
        return is_challenge

    def lose_card(self):
        # TODO Decides what card to lose and loses it
        card_pos = 0
        card = self.cards[card_pos]
        del self.cards[card_pos]
        return card

    def fake_lose_card(self, state, card):
        state = [self.name] + state
        valid_actions = [[-1, card, -1, i] for i in range(2)]
        _, is_challenge = self.agent.act(state, valid_actions)
        return is_challenge

    def choose_cards(self, state):
        # TODO 
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
        

