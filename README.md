# Assignment 1

To return to [home](https://eleanorb19.github.io/) page

### Running the code
The following two codes can be run within the command line using
```
python agent.py  
```
or
``` 
python IO.py
```

## Agent file
### agent.py
At the start of the code there are checks for checking that the model and agent_framework are connected and that the move function works. Within the model.py file the code sets a random seed, this allows me to check that the code has worked as it will produce the same random numbers each time it is run.

The function distance_between takes two arbitary agents and calculates the distance between them. The code then establishes the two variables: the number of agents and the number of iterations and the empty list for the agents. The model then makes the agents by looping the number of agents and using the Agent method in the agent_framework. The agents are then looped through the number of iterations through the move method from agent_framework. The commented out code checks that they have successfully moved.

Following this the model plots the scatter graph for the agents and prints out the location and store of the agents. 
The whole model is timed and the time taken for it to run is printed at the end. 

### agent_framework.py

This is the agent class for this model, initally the model uses the __init__ function which is a constructor in object oriented concepts, it creates the agents using the random integer function to assign values to x and y.

The model then implements a property attribute for x and y before a move method which relies on an if statement to move the x and y coordinates up or down by 1. 

## IO file
### IO.py

This code is the same as the agent.py code but does have a few additions these are:

The  commented out code about producing an output files uses the the function write_line_to_outputs which writes the number of agents out as a check. 

The addition of importing data from ([in.txt](https://github.com/eleanorb19/eleanorb19.github.io/files/7416359/in.txt)) and using this within the agent environment. It does this through creating an empty list and shifting the data into a 2D list. The commented out code is used to check that the code has been run correctly. 

The code finds the number of rows and columns of the environment and then uses this to create the agents with the method in agent_framework. 

The agents are then looped with the number of iterations through the moving and eating methods from agent_framework.

The environment is written out as a file which is called 'data.txt' which contains the agent ID, location and stores. This is also printed out to check whether all the agents have been processed.

### agent_framework.py

This is the agent class for the IO file it has a few additions/changes from the agent_framework which belongs to agent.py.

The __init__ function has 4 new parameters: the enviornment, number of rows, number of columns and the interation number of the agent. It still creates the agents using the random integer function to assign values to x and y. 

It then has a function str which displays the information about the agents ID, location and store.

It has the same move function but in this class the x and y value includes a modulo where it finds the reminder when the x and y is divided by self.cols or self.rows respectively to ensure the agents can wander round the full environment.

There is an eat method which begins with test which check that the method works by setting the environment value and then printing out if the value is less than a specific number. The agents will sick up their location if they've eaten more than 100 units.

Finally, there is a distance_between method which find the pythagorean distance between two agents.

## Running the code

The following codes are all run the command line using:
```
python animation.py 50 10 20 
```
where in this example 50 is the number of agents, 10 is the number of iterations and 20 is the size of the neighbourhood. If no values are added, too many or too few values are added or something is typed which cannot be an integer then the code will produce an exception and use the values 10, 3 and 20 as provided in the code.
## Communicating file

### communicating.py

This code is the same as the IO file but has the addition of a sharing with neighbours method from agent_framework. In addition, before the agents are run through the move, eat and share method they are randomally shuffled to randomised the order which the agents are processed to ensure the wealth is evenly shared amongst agents. The commented out code was the check that the agents had shuffled and that they had successfully worked through the loop.

### agent_framework.py

This is the same as the previous agent_framework but with the addition of the share_with_neighbours function which takes the parameter neighbourhood as the set distance parameter and then if the distance between the agents is less than the neighbourhood distance their total store is averaged and split between the two agents. 

## Animation  file
### animation.py

This code is the same but has the addition of animating the model. It uses a stopping condition based on the size of the store for the agents. 
 
The agent_framework is the same as for communicating.

## GUI files
### GUI.py

This code builds a GUI where the model plays in a window with a menu to run the model. This is completed through the def run() and then the root and menu to create the canvas. 

The agent_framework is the same as for communicating.

## Web Scraping
### webscraping.py

This model is the same as the GUI code but begins by adjusting the agent initialisation loop with the y and x data from the web (https://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html). The commented code prints the agents to check that the data was successful initalised.

### agent_framework.py
This follows the same method as the communicating agent_framework but has additional y and x parameters within the __init__ function. This is to check that the code will still run even if there are missing x and y values from the data. This is the only difference from the previous agent_framework model.


The basis of the code is:
Move: This method moves x and y cooridnates up or down by 1 by random numbers.
Eat: This method makes the agents eat what is left of the environment.
Sharing with neighbours: the agents search for close neighbours and then shares resources with them. 


Here are some examples of the time taken for different agents, iterations which I have turned into a plot attached to this file for the communicating.py file.

communicating.py file- 
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


