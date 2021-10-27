# Assignment 1

# Agent file
### agent.py
At the start of the code there are checks for checking that the model and agent_framework are connected and that the move function works. Within the model.py file the code sets a random seed, this allows me to check that the code has worked as it will produce the same random numbers each time it is run.

The function distance_between takes two arbitary agents and calculates the distance between them. The code then establishes the two variables: the number of agents and the number of iterations and the empty list for the agents. The model then makes the agents by looping the number of agents and using the Agent method in the agent_framework. The agents are then looped through the number of iterations through the move method from agent_framework. The commented out code checks that they have successfully moved.

Following this the model plots the scatter graph for the agents and prints out the location and store of the agents. 
The whole model is timed and the time taken for it to run is printed at the end. 

# agent_framework.py

This is the agent class for this model, initally the model uses the __init__ function which is a constructor in object oriented concepts, it creates the agents using the random integer function to assign values to x and y.

The model then implements a property attribute for x and y before a move method which relies on an if statement to move the x and y coordinates up or down by 1. 

To run these models within the command prompt $ python agent.py FIX THIS

# IO file
## IO.py

This code is the same as the agent.py code but does have a few additions these are:

The  commented out code about producing an output files uses the the function write_line_to_outputs which writes the number of agents out as a check. 

The addition of importing data from ([in.txt](https://github.com/eleanorb19/eleanorb19.github.io/files/7416359/in.txt)) and using this within the agent environment. It does this through creating an empty list and shifting the data into a 2D list. The commented out code is used to check that the code has been run correctly. 

The code finds the number of rows and columns of the environment and then uses this to create the agents with the method in agent_framework. 

The agents are then looped with the number of iterations through the moving and eating methods from agent_framework.

The environment is written out as a file which is called 'data.txt' which contains the agent ID, location and stores. This is also printed out to check whether all the agents have been processed.

## agent_framework.py

This is the agent class for the IO file it has a few additions/changes from the agent_framework which belongs to agent.py.

The __init__ function has 4 new parameters: the enviornment, number of rows, number of columns and the interation number of the agent. It still creates the agents using the random integer function to assign values to x and y. 

It then has a function str which displays the information about the agents ID, location and store.

It has the same move function but in this class the x and y value includes a modulo where it finds the reminder when the x and y is divided by self.cols or self.rows respectively to ensure the agents can wander round the full environment.

There is an eat method which begins with test which check that the method works by setting the environment value and then printing out if the value is less than a specific number. The agents will sick up their location if they've eaten more than 100 units.

Finally, there is a distance_between method which find the pythagorean distance between two agents.

# Communicating file

## communicating.py

This code is the same as the IO file but has the addition of a sharing with neighbours method from agent_framework. In addition, before the agents are run through the move, eat and share method they are randomally shuffled to randomised the order which the agents are processed to ensure the wealth is evenly shared amongst agents. The commented out code was the check that the agents had shuffled and that they had successfully worked through the loop.

## agent_framework.py

This is the same as the previous agent_framework but with the addition of the share_with_neighbours function which takes the parameter neighbourhood as the set distance parameter and then if the distance between the agents is less than the neighbourhood distance their total store is averaged and split between the two agents. 

# Animation  file
## animation.py

This code is the same but has the addition of animating the model. It uses a stopping condition 


Move: This method moves x and y cooridnates up or down by 1 by random numbers.
Eat: This method makes the agents eat what is left of the environment.
Sharing with neighbours: the agents search for close neighbours and then shares resources with them. 


The function distance_between takes two arbitary agents and calculates the distance between them. The code then establishes the three variables: the number of agents, the number of iterations and the size of the neighbourhood. The model then makes the agents by looping the number of agents and using the Agent method in the agent_framework. The agents are then looped with the number of iterations, being shuffled to randomised the order which the agents are processed to ensure the wealth is evenly shared amongst agents, through the moving, eating and sharing with neighbours method from agent_framework. 

Following this the model plots the scatter graph for the agents.  Finally the whole code has been timed to check how long each process takes. 

Here are some examples of the time taken for different agents, iterations which I have turned into a plot attached to this file. 

Model.py file- 
For 300 agents, 5 iterations and 20 neighbourhoods time taken = 1.99

For 200 agents, 5 iterations and 20 neighbourhoods time taken = 1.05

For 100 agents, 5 iterations and 20 neighbourhoods time taken = 0.57

For 50 agents, 5 iterations and 20 neighbourhoods time taken = 0.38

For 10 agents, 5 iterations and 20 neighbourhoods time taken = 0.304

For 300 agents, 10 iterations and 20 neighbourhoods time taken = 2.23

For 200 agents, 10 iterations and 20 neighbourhoods time taken = 1.33

For 100 agents, 10 iterations and 20 neighbourhoods time taken = 0.67

For 50 agents, 10 iterations and 20 neighbourhoods time taken = 0.41

For 10 agents, 10 iterations and 20 neighbourhoods time taken = 0.25

For 300 agents, 20 iterations and 20 neighbourhoods time taken = 3.099

For 200 agents, 20 iterations and 20 neighbourhoods time taken = 1.74

For 100 agents, 20 iterations and 20 neighbourhoods time taken = 0.75

For 50 agents, 20 iterations and 20 neighbourhoods time taken = 0.43

For 10 agents, 20 iterations and 20 neighbourhoods time taken = 0.24

![Animation run time](https://user-images.githubusercontent.com/90636185/137923678-7d9cb111-9a11-42d6-b64c-1fbbc6437fd9.png)

## agent_framework.py
This is the agent class for this model, initally the model uses the __init__ function which is a constructor in object oriented concepts, it creates the agents using the parameters of the iteration number, the empty agents list, the environment, the number of rows and columns. 

It then has a function which returns the agent ID, the location and the store of the agents and then has another function which implements a property attribute for x and y. There is then a function which moves the agents based on an if statement about a random number which is explained in the code. The code includes a modulo where it finds the reminder when the x and y is divided by self.rows to ensure the agents can wander round the full environment.

The code then creates an eat method within the agent class which begins by a test which check that the method works by setting the environment value and then printing out if the value is less than a specific number. The agents will sick up their location if they've eaten more than 100 units.

The method distance_between finds the pythagorean distance between the agents which is used within the model.py code. Finally the method share_with_neighbours takes the parameter of neighbourhood which is the set distance where agents will share resources. The method is explained within the code documentation. 


## animation.py
This model begins by initalising the model with the y and x data from the web (https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html) with the commented out code aimed to check that the data was successful inputed. The code is then the same as the model.py code until it uses the function run to plot the animation of the agents which will run until the stopping condition. The follwoing code builds the main window, sets its title, then creates and lays the canvas and the matplotlib figure. The menu is associated with the function run. The model displays in a window with a menu to then choose to run the model. 

## agentframework.py
This is the agent class for the animation model. It begins by using the __init__ function similar to the agent_framework.py model but sets x and y to random values so that they will still run if there are missing x and y values. The establishing of the x and y coordinate is the only difference between this model and the agent_framework model. 


