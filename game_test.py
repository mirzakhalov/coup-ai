
from game import Game

game = Game(5)

for i in range(51*10*100):
    game.reset()
    rewards = game.play()
    #print(i, rewards)
    #print(i)
    for i in range(0, len(game.players)):
        game.players[i].agent.next_game(rewards[i])