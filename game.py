
import random

class Game:

    self.deck = [0,0,0,1,1,1,2,2,2,3,3,3,4,4,4]
    self.players = []
    self.round_count = 0
    self.active_player = None
    self.alive_count = 5 



    def __init__(self, player_count):

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
            player = new Player(cards, 2, i, True, agent)
            self.players.append(player)




    def challenge():



    def do_action():


    
    def reset():
        self.deck = []
        self.players = []
        self.round_count = 0
        self.active_player = None
        self.alive_count = 5 

    def pull_card(self):
        index = random.randint(0, len(self.deck))
        card = self.deck[card]
        del self.deck[index]
        return card