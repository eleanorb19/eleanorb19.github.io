# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 10:59:22 2021

@author: elean
"""

import random
import operator
import matplotlib.pyplot
import agent_framework
import sys
import time

# Checking the time taken for the code to run
start = time.perf_counter()

'''
# Commented out test
# Checking that the model and agent_framework files are connected
a = agent_framework.Agent()
print(a)
print(a.x)
print(a.y, a.x)
# Checking that the move function works from agentframework
a.move()
print(a.y, a.x)
'''

# Setting a random seed of 0
random.seed(0)
environment = []

# Finding pythagorean distance between two agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._y - agents_row_b._y)**2) +
        ((agents_row_a._x - agents_row_b._x)**2))**0.5

# Adding variables and creating agents
num_of_agents = 10
num_of_iterations = 5
agents = []

# Make the agents
for i in range(num_of_agents):
    agents.append(agent_framework.Agent())

# Moving, eating and sharing with neighbours the agents
# Commented out code is for checking code has been successful
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # print(i, "Before move", agents[i]._x, agents[i]._y)
        agents[i].move() # Adjusting the model to use agentframework
        # print(i, "After move", agents[i]._x, agents[i]._y)

# Producing plot for agents
matplotlib.pyplot.xlim(0, 100)
matplotlib.pyplot.ylim(0, 100)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
matplotlib.pyplot.show()
 
# Finding the distance using distance_between function
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)
        
# Printing agents to provide location and store        
for i in range(num_of_agents):
    print(agents[i])
    
end = time.perf_counter()

# Printing the time taken for code
print("time = " + str(end - start))

