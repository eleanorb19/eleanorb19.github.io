# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:10:55 2021

@author: elean
"""

import random
# Creating an Agent class
class Agent():
    def __init__(self, i, environment, rows, cols):
        """
        
        Parameters
        ----------
        environment : List holding environment data
        rows : the length of the environment
        cols : the length of the first row of the environment
        i : iteration number

        """
        
        self._x = random.randint(0,100)
        self._y = random.randint(0,100)
        self.environment = environment
        self.store = 0 
        self.rows = rows
        self.cols = cols
        self.i = i
    
    # Printing and naming the agents so that they display information about 
    # their location and stores
    def __str__(self):
        """
        Returns
        -------
        The agent id, its location and the store.

        """
        return "id = " + str(self.i) + ", x=" + str(self._x) \
            + ", y=" + str(self._y) \
            + ", store=" + str(self.store) 
    
    # Implementing a property attribute for x and y
    def set_x(self):
        self._x = x 
    def get_x(self):
        return self._x
    def set_y(self):
        self._y = y
    def get_y(self):
        return self._y

    def move(self): # Creating a move method within the Agent class    
        """
        Creating a move method within the Agent class
        If statement against a random number between 0 and 1.
        If the number is less than 0.5 then the x or y coordinate will 
        increase by 1
        and vice versa for greater than 0.5. 
        """
        if random.random() < 0.5:
            self._y = (self._y + 1) % self.rows # Ensuring agents can wander 
            # around full environment
        else:
            self._y = (self._y - 1) % self.rows

        if random.random() < 0.5:
            self._x = (self._x + 1) % self.cols
        else:
            self._x = (self._x - 1) % self.cols
    
    def eat(self): # Creating an eat method within the Agent class
    # Test by setting the environment value
    # self.environment[self._y][self._x] = 8
        if self.environment[self._y][self._x] > 10: # Eating the last few pieces
            self.environment[self._y][self._x] -= 10
            self.store += 10
        else:
            # Commented out for check
            # print("Adding a value less than 10")
            # print("Before eat", self.environment[self._y][self._x])
            # print(self)
            self.store += self.environment[self._y][self._x]
            self.environment[self._y][self._x] = 0
            # print("After eat", self.environment[self._y][self._x])
            # print(self)
        # Agents sick up their store in a location if they've eaten more 
        # than 100 units
        if self.store > 100:
            self.environment[self._y][self._x] += 100
            self.store = 0
            #print("Sick")
    
    # Calculating distance between agents 
    def distance_between(self, b):
        """
        Finds pythagorean distance between two agents
        b : agent

        Returns:
        distance between agents

        """
        return (((self._x - b._x)**2) + ((self._y - b._y)**2))**0.5
    
