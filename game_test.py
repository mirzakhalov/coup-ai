
from game import Game

game = Game(5)

for i in range(10000):
    game.reset()
    rewards = game.play()
    for i in range(0, len(game.players)):
        # don't update an random agent to test
        if i != 4:
            game.players[i].agent.next_game(rewards[i])