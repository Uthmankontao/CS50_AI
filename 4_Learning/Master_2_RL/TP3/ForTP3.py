#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:02:58 2020

@author: berar
"""
import numpy as np
import matplotlib.pyplot as plt
from Maze_generating_interface import App

actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
def get_actions(state,actions):
    # list of possible actions 
    local_actions = list()
    for a in actions :
        m = [0,0]
        if a == "UP" :
            m[0] = -1   
        elif a == "DOWN" :
            m[0] = +1
        elif a == "LEFT" :
            m[1] = -1
        else : # a=="RIGHT"
            m[1] = +1
        if Maze[state[0]+m[0],state[1]+m[1]] == 1.0 :    
            local_actions.append(a)
    return local_actions
            
def next_state(state, action, exit_state, Maze):
    # give the resulting state end reward 
    new_state = np.copy(state)
    if action == "UP" :
        new_state[0] -= 1   
    elif action == "DOWN" :
        new_state[0] += 1
    elif action == "LEFT" :
        new_state[1] -= 1
    else : # a=="RIGHT"
        new_state[1] += 1
    
    if all(new_state == exit_state) :
        reward = 1
    else:
        reward = 0
    return new_state,reward

def generate_episode(init_state,actions,M,exit_state,itermax=1000) :
     #from init_state to exit_state in maze M
     # list of (state, action, reward, next_state)
     i=0
     current_state = np.copy(init_state)
     episode = list()
     while  i < itermax and not all(current_state == exit_state)  :      
         current_actions = get_actions(current_state,actions)
         action = current_actions[np.random.randint(len(current_actions))]
         new_state, reward= next_state(current_state, action, exit_state, Maze)
         #
         episode.append((current_state,action, reward, new_state))
         #
         current_state = new_state
         i=i+1
     return episode

def get_states_from_Maze(Maze) :
    # return states, exit_state, init_states,  
    states = list(np.argwhere(Maze == 1))
    M = np.zeros(Maze.shape)
    M[:,0]=1
    M[:,-1] = 1
    M[0,:]=1
    M[-1,:]=1
    
    exit_state = np.argwhere(Maze*M)[0]
    init_states = list(np.copy(states))
    init_states.pop(np.argwhere((init_states == exit_state).sum(axis =1) == 2)[0][0])
    return states,exit_state,init_states

if 1 :
    app = App()
    app.mainloop()
    Maze=app.A

plt.imshow(Maze,cmap='Blues')
states,exit_state,init_states = get_states_from_Maze(Maze)


init_state = init_states[np.random.randint(len(init_states))]
episode = generate_episode(init_state,actions,Maze,exit_state, itermax=100*len(states))






