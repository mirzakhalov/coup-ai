from player import Player
from agent import Agent
import random
import player

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
<<<<<<< HEAD
            player = player.Player(cards=cards, coins=2, name=i, is_bot=True, agent=None)
=======
            player = Player(cards, 2, i, True, Agent())
>>>>>>> 86a85ca628acc49ab990ce4a2bac5028bdd1cf4a
            self.players.append(player)

    def challenge(self, active_player, action, target_player):
        challenges = []
        for i in range(0, len(self.players)):
            if len(self.players[i].cards) != 0:
                # Need inster the state in here ->
                if self.players[i].get_challenge(None, active_player, action, target_player):
                    challenges.append(i)
        
        success = True

<<<<<<< HEAD
    def challenge(self):
        return
=======
        if len(challenges) != 0:
            challenger = random.choice(challenges)

            if card is in active_player.cards:
                success = False
                
            print(challenges)
            print(challenger)
            quit()

        return success
>>>>>>> 86a85ca628acc49ab990ce4a2bac5028bdd1cf4a

    def do_action(self):
        action_type = self.active_player.get_action(state=None) # get from player object
        
        # Take a coin (-)
        if action_type == 0:
            return
        # Take foreign aid (-)
        elif action_type == 1:
            return
        # Coup (+)
        elif action_type == 2:
            return
        # Use Duke (-, c)
        elif action_type == 3:
            return
        # Take Ambassador (-, d)
        elif action_type == 4:
            return
        # Take foreign aid
        elif action_type == 5:
            return
        # Take foreign aid
        else:
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
