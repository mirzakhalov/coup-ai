
from game import Game

game = Game(5)
wins = [0 for i in range(5)]

train = False
if not train:
    print("Loaded Model")
    game.players[1].agent.get_model('./saved_100_episodes/checkpoint1.pth')

for i in range(51*10*100):
    game.reset()
    rewards = game.play()
    #print(i, rewards)
    #print(i)

    if train:
        for k in range(0, len(game.players)):
            game.players[k].agent.next_game(rewards[k])
    else:
        for k in range(5):
            if rewards[k] == 1:
                wins[k] += 1
        print([wins[k]/(i+1) for k in range(5)])
        