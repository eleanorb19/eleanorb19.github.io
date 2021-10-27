# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 11:05:20 2021

@author: elean
"""

import random
# Creating an Agent class
class Agent():
    def __init__(self):
        self._x = random.randint(0,100)
        self._y = random.randint(0,100)
    
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
            self._y = (self._y + 1) % 100 # Ensuring agents can wander around 
            # full environment
        else:
            self._y = (self._y - 1) % 100

        if random.random() < 0.5:
            self._x = (self._x + 1) % 100
        else:
            self._x = (self._x - 1) % 100
    
