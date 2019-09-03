
import math
import numpy as np
from collections import deque
import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

from operator import itemgetter

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

np.random.seed(101)

class Agent(nn.Module):
    def __init__(self, name, h_size=16, gamma=1.0, print_every=1, pop_size=50, elite_frac=0.2, sigma=0.5):
        super(Agent, self).__init__()
        self.name = name
        self.action_count = 0

        # state, hidden layer, action sizes
        self.s_size = 19 + 4
        self.h_size = h_size
        self.a_size = 1
        # define layers
        self.fc1 = nn.Linear(self.s_size, self.h_size)
        self.fc2 = nn.Linear(self.h_size, self.a_size)

        self.game_count = 0
        self.episode_return = 0

        self.weights_to_evaluate = []
        self.rewards = []
        self.curr_rewards = []

        self.n_elite=int(pop_size*elite_frac)

        self.scores_deque = deque(maxlen=100)
        self.scores = []
        self.best_weight = sigma*np.random.randn(self.get_weights_dim())
        self.i_iteration = 0
        self.weights_pop = [self.best_weight + (sigma*np.random.randn(self.get_weights_dim())) for i in range(pop_size)]
        self.weight_num = 0

        self.print_every = print_every
        self.sigma = sigma
        self.pop_size = pop_size

        self.evaluate_best = False

    def act(self, state, valid_actions):
        # TODO feedforward through model
        self.action_count += 1
        # TODO add to memory
        qmap = []
        for action in valid_actions:
            qval = self.forward(torch.from_numpy(np.array(state + action)).float().to(device)).detach().numpy()[0]
            qmap.append([action, qval])

        #print("***")
        #print(state)
        #print(qmap)
        qmap = sorted(qmap, key=itemgetter(1))
        qmap.reverse()
        action_type, target_player, _, is_challenge = qmap[0][0]

        return ([action_type, target_player], is_challenge)
        
    def set_weights(self, weights):
        s_size = self.s_size
        h_size = self.h_size
        a_size = self.a_size
        # separate the weights for each layer
        fc1_end = (s_size*h_size)+h_size
        fc1_W = torch.from_numpy(weights[:s_size*h_size].reshape(s_size, h_size))
        fc1_b = torch.from_numpy(weights[s_size*h_size:fc1_end])
        fc2_W = torch.from_numpy(weights[fc1_end:fc1_end+(h_size*a_size)].reshape(h_size, a_size))
        fc2_b = torch.from_numpy(weights[fc1_end+(h_size*a_size):])
        # set the weights for each layer
        self.fc1.weight.data.copy_(fc1_W.view_as(self.fc1.weight.data))
        self.fc1.bias.data.copy_(fc1_b.view_as(self.fc1.bias.data))
        self.fc2.weight.data.copy_(fc2_W.view_as(self.fc2.weight.data))
        self.fc2.bias.data.copy_(fc2_b.view_as(self.fc2.bias.data))
    
    def get_weights_dim(self):
        return (self.s_size+1)*self.h_size + (self.h_size+1)*self.a_size
        
    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.sigmoid(self.fc2(x))
        return x.cpu().data

    def next_game(self,reward):
        self.game_count += 1
        self.curr_rewards.append(reward)
        if self.game_count >= 11:
            if self.evaluate_best != True:
                self.rewards.append(np.array(self.curr_rewards).mean())
            self.weight_num += 1
            if self.weight_num >= len(self.weights_pop):
                self.finished_iter(np.array(self.curr_rewards).mean())
            else:
                self.set_weights(self.weights_pop[self.weight_num])
            
            self.game_count = 0
            self.curr_rewards = []


    def finished_iter(self, reward):
        elite_idxs = np.array(self.rewards).argsort()[-self.n_elite:]

        elite_weights = [self.weights_pop[i] for i in elite_idxs]
        
        # don't update an random agent to test
        if self.name != 4:
            self.best_weight = np.array(elite_weights).mean(axis=0)

        if self.evaluate_best == True:
            self.scores_deque.append(reward)
            self.scores.append(reward)

            torch.save(self.state_dict(), 'checkpoint' + str(self.name) + '.pth')
            self.i_iteration += 1

            self.weights_pop = [self.best_weight + (self.sigma*np.random.randn(self.get_weights_dim())) for i in range(self.pop_size)]
            self.weight_num = 0
            self.rewards = []

            #TODO Need to evaluate against random bots to verify

            if self.i_iteration % self.print_every == 0:
                print('Agent {}: Episode {}\tAverage Score: {:.2f}'.format(self.name, self.i_iteration, np.mean(self.scores_deque)))
            
            self.evaluate_best = False
        else:
            self.evaluate_best = True
            self.set_weights(self.best_weight)

            
