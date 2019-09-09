# Coup: The Dystopian Universe + Reinforcement Learning

This project was an attempt to create an AI bot to play the game of Coup in 5 player setting. Are you wondering what is Coup? It is basically a multi-player game where a player has to manipulate, bluff and damage others with the goal of being the last one alive. It is a fast-paced and highly unpredictable game that we just love to play in our free time. You can learn about the rules more [here](https://boardgamegeek.com/boardgame/131357/coup)

## Setting up Game Environment

We do this in terms of these processes:

- Rule identification
- Standardization
- Game flow setup
- Testing (random agent)

First step before starting to code up the environment is to strictly define the rules and actions once more. In the context of Coup, we identified all `Actions` any particular player can perform at any given time. For example, it would include Play card X, Play card Y, Challenge a play etc. Once identified, we through the process of `Standardization`. `Standardization`, by our own definition, would involve coming up with a standardized way of representing all actions in a uniform way. This is a crucial step and actually enables a very intuitive transition when we move to `Reinforcement Learning` phase of our development.  


