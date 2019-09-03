from player import Player
from agent import Agent
import random

class Game:

    def __init__(self, player_count):
        self.deck = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]
        self.players = []
        self.round_count = 0
        self.active_player = None
        self.alive_count = 5 

        self.alive_count = player_count

        # adding players to the game
        for i in range(0, player_count):

            # pull 2 cards from the deck and deal to each player
            cards = []
            cards.append(self.pull_card())
            cards.append(self.pull_card())

            # set the name for the player
            name = i

            # create a player
            player = Player(cards, 2, i, True, Agent())
            self.players.append(player)

    def challenge(self, active_player, action, target_player):
        challenges = []
        for i in range(0, len(self.players)):
            if len(self.players[i].cards) != 0:
                if  active_player.name != self.players[i].name:
                    # Need insert the state in here ->
                    if self.players[i].get_challenge(None, active_player, action, target_player):
                        challenges.append(i)
        
        success = True

        if len(challenges) != 0:
            challenger = self.players[random.choice(challenges)]
            card = (random.randint(0,4),True,False)
            # Need insert the state in here ->
            if card[0] not in active_player.cards or active_player.fake_lose_card(None, card[0]):
                success = False
                active_player.lose_card()
            else:
                active_player.lose_specific_card(card[0])
                active_player.cards.append(self.pull_card())
                challenger.lose_card()

        return success

    def do_action(self):
        return

    
    def reset():
        self.deck = []
        self.players = []
        self.round_count = 0
        self.active_player = None
        self.alive_count = 5 

    def pull_card(self):
        index = random.randint(0, len(self.deck)-1)
        card = self.deck[index]
        del self.deck[index]
        return card
