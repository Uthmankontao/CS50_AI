#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:39:44 2020

@author: berar
"""
import numpy as np
import sys


def main():
    pass

class Grid:
    def __init__(self, GRID_SIZE:int, TERMINAL_STATES:list):
        self.GRID_SIZE = GRID_SIZE
        self.TERMINAL_STATES = TERMINAL_STATES

        try:
            self.states = np.arange(0, self.GRID_SIZE * self.GRID_SIZE)
            self.actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
            self.discount = 1.

            # Politique uniforme initiale
            self.uniform_policy = {
                int(s): {a: 1/len(self.actions) for a in self.actions}
                for s in self.states
            }

            self.P = {s: {} for s in self.states}
            self.P = self.uniformize(self.P)

        except Exception as e:
            sys.exit(e)

    def uniformize(self, P):
        for s in self.states:
            P[s] = {a: () for a in self.actions}
            if s in self.TERMINAL_STATES:
                reward = 0.
                for action in self.actions:
                    P[s][action] = (s, reward, True)
            else:
                reward = -1.
                for action in self.actions:
                    next_s = self.next_state(self.GRID_SIZE, s, action)
                    P[s][action] = (next_s, reward, self.is_done(next_s, self.TERMINAL_STATES))
        return P

    def next_state(self, grid_size, state, action):
        i, j = np.unravel_index(state, (grid_size, grid_size))
        if action == 'UP':
            i = max(0, i-1)
        elif action == 'DOWN':
            i = min(grid_size-1, i+1)
        elif action == 'RIGHT':
            j = min(grid_size-1, j+1)
        elif action == 'LEFT':
            j = max(0, j-1)
        return int(np.ravel_multi_index((i, j), (grid_size, grid_size)))

    def is_done(self, state, terminal_states):
        return state in terminal_states

    # ===================== POLICY EVALUATION =====================
    def policy_evaluation(self, policy=None, theta=1e-5):
        if policy is None:
            policy = self.uniform_policy
        V = np.zeros(len(self.states))
        while True:
            delta = 0
            for s in self.states:
                v = V[s]
                new_v = 0
                for a, action_prob in policy[s].items():
                    next_s, reward, done = self.P[s][a]
                    new_v += action_prob * (reward + self.discount * V[next_s])
                V[s] = new_v
                delta = max(delta, abs(v - V[s]))
            if delta < theta:
                break
        return V

    # ===================== POLICY ITERATION =====================
    def policy_iteration(self):
        policy = {s: {a: 1/len(self.actions) for a in self.actions} for s in self.states}
        stable = False
        while not stable:
            V = self.policy_evaluation(policy)
            stable = True
            for s in self.states:
                if s in self.TERMINAL_STATES:
                    continue
                old_action = max(policy[s], key=policy[s].get)
                action_values = {}
                for a in self.actions:
                    next_s, reward, done = self.P[s][a]
                    action_values[a] = reward + self.discount * V[next_s]
                best_action = max(action_values, key=action_values.get)
                policy[s] = {a: 1.0 if a == best_action else 0.0 for a in self.actions}
                if old_action != best_action:
                    stable = False
        return policy, V

    # ===================== VALUE ITERATION =====================
    def value_iteration(self, theta=1e-5):
        V = np.zeros(len(self.states))
        while True:
            delta = 0
            for s in self.states:
                if s in self.TERMINAL_STATES:
                    continue
                v = V[s]
                V[s] = max(self.P[s][a][1] + self.discount * V[self.P[s][a][0]] for a in self.actions)
                delta = max(delta, abs(v - V[s]))
            if delta < theta:
                break

        # Politique optimale
        policy = {}
        for s in self.states:
            if s in self.TERMINAL_STATES:
                policy[s] = {a: 1/len(self.actions) for a in self.actions}
            else:
                action_values = {a: self.P[s][a][1] + self.discount * V[self.P[s][a][0]] for a in self.actions}
                best_action = max(action_values, key=action_values.get)
                policy[s] = {a: 1.0 if a == best_action else 0.0 for a in self.actions}
        return V, policy

    # ===================== AFFICHAGE =====================
    def print_values(self, V):
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                s = np.ravel_multi_index((i,j), (self.GRID_SIZE, self.GRID_SIZE))
                print(f"{V[s]:6.2f}", end=" ")
            print()

    def print_policy(self, policy):
        arrow = {'UP':'↑','DOWN':'↓','LEFT':'←','RIGHT':'→'}
        for i in range(self.GRID_SIZE):
            for j in range(self.GRID_SIZE):
                s = np.ravel_multi_index((i,j), (self.GRID_SIZE, self.GRID_SIZE))
                if s in self.TERMINAL_STATES:
                    print(" T ", end=" ")
                else:
                    a = max(policy[s], key=policy[s].get)
                    print(f" {arrow[a]} ", end=" ")
            print()


def main():
    GRID_SIZE = 4
    TERMINAL_STATES = [0, GRID_SIZE*GRID_SIZE - 1]
    env = Grid(GRID_SIZE, TERMINAL_STATES)

    print("=== Policy Evaluation (uniform) ===")
    V = env.policy_evaluation()
    env.print_values(V)
    print()

    print("=== Policy Iteration ===")
    policy_pi, V_pi = env.policy_iteration()
    env.print_values(V_pi)
    env.print_policy(policy_pi)
    print()

    print("=== Value Iteration ===")
    V_vi, policy_vi = env.value_iteration()
    env.print_values(V_vi)
    env.print_policy(policy_vi)


if __name__ == "__main__":
    main()

# class Grid:
#     def __init__(self, GRID_SIZE:int, TERMINAL_STATES:list):
#         self.GRID_SIZE = GRID_SIZE
#         self.TERMINAL_STATES = TERMINAL_STATES

#         try:
#             self.states = np.arange(0, self.GRID_SIZE * self.GRID_SIZE - 1)
#             self.actions = ['UP', 'RIGHT', 'DOWN', 'LEFT']
#             self.discount = 1.

#             # The unifom policy, policy veut dire strategie --> strategie uniforme       
#             self.uniform_policy = {int(s): {a: 1/len(self.actions) for a in self.actions } for s in self.states} # on donne une probabilité à chaque action
            
#         except Exception as e:
#             sys.exit(e)
            

#     # def __str__(self):
#     #     return f"{self.P}"

#     def uniformize(self, P):
#         for s in range(len(self.states)):
#             P[s] = {a : () for a in self.actions}
#             if s in self.TERMINAL_STATES:
#                 # if terminal state, stay where you are
#                 # instead of next_state
#                 reward = 0.
#                 for action in self.actions:
#                     P[s][action] = (s, reward, True)
#             else:
#                 # transition
#                 reward = -1.
#                 for action in self.actions:
#                     next_s = self.next_state(self.GRID_SIZE, s, action)
#                     P[s][action] = (next_s,reward,self.is_done(next_s, self.TERMINAL_STATES))
#         return P
        
#     def next_state(self, grid_size, state, action):
#             i,j = np.unravel_index(state, (grid_size, grid_size))
#             if action == 'UP':
#                 i = np.maximum(0,i-1)
#             elif action == 'DOWN':
#                 i = np.minimum(i+1,grid_size-1)
#             elif action == 'RIGHT':
#                 j = np.minimum(j+1,grid_size-1)
#             elif action == 'LEFT':
#                 j = np.maximum(0,j-1)    
#             new_state = np.ravel_multi_index((i,j), (grid_size, grid_size))
#             return int(new_state)
    
#     def is_done(self, state, terminal_states):
#         return state in terminal_states
    