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
        self.action_to_char = {
            '0': -1,
            '1': -1,
            '2': -1,
            '3': 0,
            '4': 1,
            '5': 2,
            '6': 4,
        }

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
                active_player.show_card(card[0])
                active_player.cards.append(self.pull_card())
                challenger.lose_card()

        return success

    def do_action(self, action_type):
        action_type = self.active_player.get_action()
        
        # Take a coin (-)
        if action_type == 0:
            self.active_player.coins += 1
        # Take foreign aid (-, c)
        elif action_type == 1:
            self.active_player.coins += 2
        # Coup (+)
        elif action_type == 2:
            self.active_player.coins -= 7
            if len(self.target_player.cards) > 0:
                self.target_player.remove_card()
        # Use Ambassador (-, c)
        elif action_type == 3:
            self.active_player.cards.append(self.pull_card())
            self.active_player.cards.append(self.pull_card())
            self.active_player.remove_card()
            self.active_player.remove_card()

        # Use Assassin (+, c)
        elif action_type == 4:
            self.active_player.coins -= 3
            if len(self.target_player.cards) > 0:
                self.target_player.remove_card()
        # Use Captain (+, c)
        elif action_type == 5:
            return
        # Use Duke (-, c)
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
                    

            



