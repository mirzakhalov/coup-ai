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
        self.target_player = None
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
                # Need inster the state in here ->
                if self.players[i].get_challenge(None, active_player, action, target_player):
                    challenges.append(i)
        
        success = True

        if len(challenges) != 0:
            challenger = random.choice(challenges)

            if card is in active_player.cards:
                success = False
                
            print(challenges)
            print(challenger)
            quit()

        return success

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
    

    def play(self):
        player_index = random.randint(0, len(self.players))
        while self.alive_count > 1:
            self.active_player = self.players[player_index]
            # this means that the player is dead
            if len(self.active_player.cards) == 0:
                if player_index + 1 < len(self.players):
                    player_index = player_index + 1
                else:
                    player_index = 0    
                continue
            
            # let the active player take an action
            action_type, self.target_player = self.active_player.get_action()

            # let the challenge begin
            if not self.challenge(self.active_player, action_type, self.target_player):

                # challenge was successfull, check if the active player is still alive
                if len(self.active_player.cards) == 0:  
                    # decrement the number of players alive
                    self.alive_count = self.alive_count - 1
    
                # increment number of rounds
                self.round_count = self.round_count + 1
                
                # move to the next player
                if player_index + 1 < len(self.players):
                    player_index = player_index + 1
                else:
                    player_index = 0


            else:
                # challenge was not successfull
                if self.target_player != None:
                    counter_action_type = self.target_player.get_counter_action()
                    self.do_counter_action(counter_action_type)
                    

            



