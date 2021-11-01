# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 09:41:40 2021

@author: elean
"""
import random
import operator
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot
import matplotlib.animation 
import agent_framework
import csv
import fileinput
import sys
import matplotlib
import tkinter
import requests
import bs4
import time
from tkinter import ttk
import sys

# Checking the time taken for the code to run
start = time.perf_counter()


# Initialise our model with the y and x data.
# Commented out code aimed to check code was successful
page = requests.get("https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html")
content = page.text
soup = bs4.BeautifulSoup(content, 'html.parser')
# print(soup)
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})
# print(td_ys)
# print(td_xs)

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


# Setting random seed to 0
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

# Finding pythagorean distance between two agents
def distance_between(agents_row_a, agents_row_b):
    return (((agents_row_a._y - agents_row_b._y)**2) +
        ((agents_row_a._x - agents_row_b._x)**2))**0.5

# Adding variables and creating agents using sys for command line
num_of_agents = int(sys.argv[1])
num_of_iterations = int(sys.argv[2])
neighbourhood = int(sys.argv[3])
# num_of_agents = 20
# num_of_iterations = 10
# neighbourhood = 20
agents = []

# Make the agents
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agent_framework.Agent(i, agents, environment, rows, cols, 
    y, x))

# Checks whether agents have been successfully initalised 
# for i in range(num_of_agents):
#     print(agents[i])
 
# Creating animation plot
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, 
    frames=gen_function, repeat=False)
    canvas.draw()    
 
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])

# This builds the main window ("root"); sets its title, then creates and 
# lays out a matplotlib canvas 
# embedded within our window and associated with fig, our matplotlib figure.
root = tkinter.Tk()
root.wm_title("Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

menu = tkinter.Menu(root)
root.config(menu=menu)
model_menu = tkinter.Menu(menu)
menu.add_cascade(label="Model", menu=model_menu)
model_menu.add_command(label="Run model", command=run)
model_menu.add_command(label="End model", command=root.quit)


carry_on = True	
	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    
    # Plot the environment
    matplotlib.pyplot.imshow(environment)
    matplotlib.pyplot.xlim(0, cols)
    matplotlib.pyplot.ylim(0, rows)
    
    # Moving, eating and sharing the agents
    for j in range(num_of_iterations):
        #print("Iteration", j) 
        random.shuffle(agents) #Randomising the order in which agents are 
        # processed
        for i in range(num_of_agents):
            # print(i, "Before move", agents[i]._x, agents[i]._y)
            agents[i].move() #Adjusting the model to use agentframework
            # print(i, "After move", agents[i]._x, agents[i]._y)
            # print(i, "Store before eat", agents[i].store)
            agents[i].eat() #Eating what is left
            # print(i, "Store after eat", agents[i].store)
            agents[i].share_with_neighbours(neighbourhood)    
    
    # Creating a stopping condition for animation
    #if random.random() < 0.1:
        #carry_on = False
        #print("stopping condition")
    
    # Plotting the agents
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i]._x,agents[i]._y)  
		
def gen_function(b = [0]):
    a = 0
    global carry_on 
    while (a < num_of_iterations) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
        
# Printing agents to provide location and store        
for i in range(num_of_agents):
    print(agents[i])
    
end = time.perf_counter()

# Printing the time taken for code
print("time = " + str(end - start))

# Code to end the code after animation

tkinter.mainloop()

'''
# Finding the distance using distance_between function
for agents_row_a in agents:
    for agents_row_b in agents:
        distance = distance_between(agents_row_a, agents_row_b)

# Writing out environment as a file
with open("data.txt", "w") as f:
    for i in range(num_of_agents):
        f.write(str(agents[i]))
        f.write("\n")
'''