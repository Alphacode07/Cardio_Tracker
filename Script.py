# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:19:11 2019

@author: Surface
"""
"""
Welcome to the Cardio Tracker. This is a supplement to your excercises and helps you with data analytics,
goal setting and to stay on track with your routine

The user is created by inputing data such as:
    first - first name
    last -  last name
    age - age
    gender - gender
    weight - current weight of the user
    goal - weight to be reached in given time
"""

#imports
from datetime import datetime as dt

class User:
    
    no_of_users = 0
    active_users = 0
    registered_users ={}
    
    def __init__(self, first, last, username, password, age, gender):
        self.first = first
        self.last = last
        self.age  =age
        self.gender = gender
        self.username = username
        self.password = password
        User.registered_users[self.username]=self.password
        User.no_of_users +=1
        
 