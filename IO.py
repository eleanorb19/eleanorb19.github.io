# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:09:34 2021

@author: elean
"""

import random
import operator
import matplotlib
import matplotlib.pyplot
import agent_framework
import csv
import fileinput
import sys
import time

# Checking the time taken for the code to run
start = time.perf_counter()

'''
# Commented out for check
# Checking that the model and agent_framework files are connected
a = agent_framework.Agent()
print(a)
print(a.x)
print(a.y, a.x)
# Checking that the move function works from agentframework
a.move()
print(a.y, a.x)
'''

'''
#Producing an output file
def write_line_to_output(s):
    with open("output.txt", "a+") as f:
        for i  in range(num_of_agents):
            f.write(s)
            f.write("\n")
'''

# Setting a random seed of 0
random.seed(0)
environment = []

# Reading the csv file into the environment list
with open('in.txt', newline='') as f:
    reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        rowlist = []
        for value in row:
            rowlist.append(value)
        environment.append(rowlist)

'''
# Commented out for check
# Checking the data has been read in correctly
matplotlib.pyplot.imshow(environment)
matplotlib.pyplot.show()
'''

rows = len(environment)
cols = len(environment[0])
#print("rows", rows)
#print("cols", cols)


def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._y - agents_row_b._y)**2) +
        ((agents_row_a._x - agents_row_b._x)**2))**0.5


# Adding variables and creating agents
num_of_agents = 10
num_of_iterations = 5
neighbourhood = 20
agents = []

# Make the agents
for i in range(num_of_agents):
    agents.append(agent_framework.Agent(i, environment, rows, cols))

# Moving, eating and sharing with neighbours the agents
# Commented out code is for checking code has been successful
for j in range(num_of_iterations):
    for i in range(num_of_agents):
        # print(i, "Before move", agents[i]._x, agents[i]._y)
        agents[i].move() # Adjusting the model to use agentframework
        # print(i, "After move", agents[i]._x, agents[i]._y)
        # print(i, "Store before eat", agents[i].store)
        agents[i].eat() # Eating what is left
        # print(i, "Store after eat", agents[i].store)

# Producing plot for agents
matplotlib.pyplot.xlim(0, cols)
matplotlib.pyplot.ylim(0, rows)
matplotlib.pyplot.imshow(environment)
for i in range(num_of_agents):
    matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)
    matplotlib.pyplot.show()
 
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

# Writing out environment as a file
with open("data.txt", "w") as f:
    for i in range(num_of_agents):
        f.write(str(agents[i]))
        f.write("\n")
        
# Printing agents to provide location and store        
for i in range(num_of_agents):
    print(agents[i])
    
end = time.perf_counter()
print("time = " + str(end - start))

