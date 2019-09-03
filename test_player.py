from player import Player
from agent import Agent

p = Player(agent=Agent())

while(1):
    print(p.get_action(None))
    input()