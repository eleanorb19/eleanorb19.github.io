# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 15:44:22 2021

@author: elean
"""

import random

#Creating an Agent class
class Agent():
    def __init__(self, i, agents, environment, rows, cols, y, x):
        """
        Parameters
        ----------
        i : iteration number
        agents : list of agents 
        environment : list holding environment data
        rows : the length of the environment
        cols : the length of the environment
        y : y coordinate of agent
        x : x coordinate of agent
        """
        if (x == None):
            self._x = random.randint(0,100)
        else:
            self._x = x
        if (y == None):
            self._y = random.randint(0,100)
        else:
            self._y = y
        #self.x = x
        #self.y = y
        self.environment = environment
        self.agents = agents
        self.store = 0 
        self.rows = rows
        self.cols = cols
        self.i = i
    #Printing and naming the agents so that they display information about their location and stores
    def __str__(self):
        """
        Returns
        -------
        The agent id, its location and the store.

        """
        return "id = " + str(self.i) + ", x=" + str(self._x) \
            + ", y=" + str(self._y) \
            + ", store=" + str(self.store)
        
    def set_x(self):
        self._x = x
        
    def get_x(self):
        return self._x
    
    def set_y(self):
        self._y = y
        
    def get_y(self):
        return self._y

#Ensuring agents can wander around full environment
    def move(self): #Creating a move method within the Agent class
        """
        Creating a move method within the Agent class
        If statement against a random number between 0 and 1.
        If the number is less than 0.5 then the x or y coordinate will increase by 1
        and vice versa for greater than 0.5. 
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.rows
        else:
            self._y = (self._y - 1) % self.rows

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.cols
        else:
            self._x = (self._x - 1) % self.cols
    
    def eat(self):
    #Test by setting the environment value
    #self.environment[self._y][self._x] = 8
        if self.environment[self._y][self._x] > 10:
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            #Commented out for check
            #print("Adding a value less than 10")
            #print("Before eat", self.environment[self._y][self._x])
            #print(self)
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            #print("After eat", self.environment[self._y][self._x])
            #print(self)
        #Agents sick up in a location if they've eaten more than 100 units
        if self.store > 100:
            self.environment[self._y][self._x] += 100
            self.store = 0
            #print("Sick")
            
    def distance_between(self, b):
        """
        Finds pythagorean distance between two agents
        b : agent

        Returns:
        distance between agents

        """
        return (((self._x - b._x)**2) + ((self._y - b._y)**2))**0.5
    
    def share_with_neighbours(self, neighbourhood):
        """
        The agent searches for close neighbours and shares resources with them.
        It works out the distance to each agent and if they fall within the 
        neighbourgood dirance then it sets both it and the niehgbours stores
        equal to the average of their two stores. 
        Uses the distance_between method to work out Pythagorean distance.
        Parameters
        ----------
        neighbourhood : the distance parameter set.
        """ 
        for i in range(len(self.agents)): # Loop through the agents in self.agents .
            distance = self.distance_between(self.agents[i]) # Calculate the distance between self and the current other agent:
            if distance < neighbourhood:
                total = self.store + self.agents[i].store
                average = total / 2
                self.store = average
                self.agents[i].store = average
                #print("sharing " + str(distance) + " " + str(average))
         
    
    
        
            
            
            
            
       
