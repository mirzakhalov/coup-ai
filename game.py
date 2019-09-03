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

    def challenge(self, active_player, card, target_player):
        challenges = []
        success = True
        
        if card != -1:
            for i in range(0, len(self.players)):
                if  active_player.name != self.players[i].name and len(self.players[i].cards) != 0:
                    # Need insert the state in here ->
                    if self.players[i].get_challenge(None, active_player, card, target_player):
                        challenges.append(i)
            
            if len(challenges) != 0:
                challenger = self.players[random.choice(challenges)]
                
                # Need insert the state in here ->
                if card not in active_player.cards or active_player.fake_lose_card(None, card):
                    success = False
                    self.deck.append(active_player.lose_card())
                else:
                    active_player.show_card(card)
                    active_player.cards.append(self.pull_card())
                    self.deck.append(challenger.lose_card())
                    if card == 4:
                        print("Challenger: " + str(challenger.name))

        return success



    def do_action(self, action_type):
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
                self.deck.append(self.target_player.lose_card())

        # Use Ambassador (-, c)
        elif action_type == 3:
            self.active_player.cards.append(self.pull_card())
            self.active_player.cards.append(self.pull_card())
            cardList = self.active_player.choose_cards(state=None)
            self.deck += cardList

        # Use Assassin (+, c)
        elif action_type == 4:
            self.active_player.coins -= 3
            if len(self.target_player.cards) > 0:
                self.deck.append(self.target_player.lose_card())

        # Use Captain (+, c)
        elif action_type == 5:
            coins = 0
            if self.target_player.coins == 1:
                coins = 1
            else:
                coins = 2
            
            self.target_player.coins -= coins
            self.active_player.coins += coins

        # Use Duke (-, c)
        else:
            self.active_player.coins += 3
        

    
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
    
    def get_valid_actions(self):
        output = []
        # if coins more than 10, we HAVE TO coup
        if self.active_player.coins >= 10:
            for i in range(0, len(self.players)):
                if i != self.active_player.name and len(self.players[i].cards) != 0:
                    output.append([2,i,-1,-1])
            return output
        #
        output.append([0,-1,-1,-1])
        output.append([1,-1,-1,-1])
        output.append([3,-1,-1,-1])
        output.append([6,-1,-1,-1])
        for i in range(0, len(self.players)):
            if i != self.active_player.name and len(self.players[i].cards) != 0:
                if self.players[i].coins > 0:
                    output.append([5,i,-1,-1])
                if self.active_player.coins >= 3:
                    output.append([4,i,-1,-1])
                if self.active_player.coins >= 7:
                    output.append([2,i,-1,-1])

        return output

    def get_valid_counter_actions(self, action_type):
        if action_type != 4 and action_type != 5 and action_type != 1:
            return []
        
        output = []
        # if the action is steal, this is an extra option of stealing with captain
        if action_type == 5:
            output.append([action_type,self.active_player.name,2,-1])

        # if the action is steal, this is an option for an ambassador, 
        # else if this is an assassination, this represents not counteracting
        output.append([action_type,self.active_player.name,1,-1])
        output.append([action_type,self.active_player.name,0,-1])

        return output

    def render(self):

        for player in self.players:
            print("Player " + str(player.name) + ": " + str(player.cards))
            print("Player " + str(player.name) + " coins: " + str(player.coins))
            print("-"*30)
        print('\n')
            
            
    

    def play(self):
        player_index = random.randint(0, len(self.players)-1)
        print(len(self.players))
        while self.alive_count > 1:
            self.active_player = self.players[player_index]
            # this means that the player is dead
            if len(self.active_player.cards) == 0:
                if player_index + 1 < len(self.players):
                    player_index = player_index + 1
                else:
                    player_index = 0    
                continue
            
            self.render()
            
            print('Player ' + str(player_index) + ' turn')
            # let the active player take an action
            action_type, target_player = self.active_player.get_action(None, self.get_valid_actions())
            print('Action ' + str(action_type) + ' was chosen. Targeted player ' + str(target_player))

            # assign a target player if the action permits
            if target_player != -1:
                self.target_player = self.players[target_player]
            else:
                self.target_player = None

            # let the challenge begin
            if self.challenge(self.active_player, self.action_to_char[str(action_type)], self.target_player):
                print('Challenge was not successful. Action taking place...')
                # challenge was not successfull
                if action_type == 1:
                    challenges = []
                    for i in range(0, len(self.players)):
                        if self.players[i].name != self.active_player.name and len(self.players[i].cards) != 0:
                            if self.players[i].get_challenge(None, self.active_player, self.action_to_char[str(action_type)], self.players[i]):
                                challenges.append(i)

                    if len(challenges) != 0:
                        challenger = self.players[random.choice(challenges)]
                        if not self.challenge(challenger, 4, self.active_player):
                            self.do_action(action_type)


                elif self.target_player != None and len(self.target_player.cards) != 0 and action_type != 2:
                    # return -1 if the counteraction doesn't exist, otherwise returns the index of the card
                    counter_action, person = self.target_player.get_action(None, self.get_valid_counter_actions(action_type))
                    print('Targeted player wants to counteract with ' + str(self.action_to_char[str(counter_action)]))
                    # everyone has a chance to challenge the counteraction card
                    if self.challenge(self.target_player, self.action_to_char[str(counter_action)], self.active_player):
                        self.do_action(action_type)
                else:
                    self.do_action(action_type)
                    


             # challenge was successfull, check how many players are still alive
            count = 0
            for i in range(0, len(self.players)):
                if len(self.players[i].cards) != 0:
                    count += 1
                self.alive_count = count
            print('Remaining alive count: ' + str(count))

            # increment number of rounds
            self.round_count = self.round_count + 1
            
            # move to the next player
            if player_index + 1 < len(self.players):
                player_index = player_index + 1
            else:
                player_index = 0

            



