#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 15:42:06 2017

Generate test cases for SE challenge

@author: Chris
"""

import random
import string

def genAll(n,cFood,cDrink):
    genFood(n,cFood)
    genDrinks(n,cDrink)
    genNames(n)

# In order to generate people.txt we
# need already populated food and drink files
# Generate 10*n people 
# (so that we have more people than food/drink options)
def genNames(n):
    peopleFile = open('people.txt','w')
    try:
        drinks = open('drinks.txt','r').readlines()
        food = open('food.txt','r').readlines()
    except:
        print('Needed drinks.txt and/or food.txt file not found')
        return 0
    drinkOptions = [line.split(':')[0].strip() for line in drinks]
    foodOptions = [line.split(':')[0].strip() for line in food]
    for i in range(10*n):
        # Random string for each drink, n/5 characters long to minimize collision 
        peopleFile.write("".join([random.choice(string.ascii_letters) for i in range(int(n/5))])+'\n')
        peopleFile.write(','.join([random.choice(drinkOptions) for i in range(random.randint(1,int(n/5)))])+'\n')
        peopleFile.write(','.join([random.choice(foodOptions) for i in range(random.randint(1,int(n/5)))])+'\n')
    peopleFile.close()

# Generate n different drinks with int cost (0,c)
def genDrinks(n,c):
    drinkFile = open('drinks.txt','w')
    for i in range(n):
        # Random string for each drink, n/10 characters long to minimize collision 
        newDrink = "".join([random.choice(string.ascii_letters) for i in range(int(n/10))])
        newCost = random.randint(1,c)
        drinkFile.write(newDrink+':'+str(newCost)+'\n')
    drinkFile.close()

# Generate n different foods with int cost (0,c)
def genFood(n,c):
    foodFile = open('food.txt','w')
    for i in range(n):
        # Random string for each food, n/10 characters long to minimize collision 
        newFood = "".join([random.choice(string.ascii_letters) for i in range(int(n/10))])
        newCost = random.randint(1,c)
        foodFile.write(newFood+':'+str(newCost)+'\n')
    foodFile.close()

# Generate all if run as main file
if __name__ == "__main__":
    # 100 drinks, foods, and 1000 people
    n = 100
    cFood = 30
    # Drinks are cheaper than food
    cDrink = 10
    genAll(n,cFood,cDrink)
