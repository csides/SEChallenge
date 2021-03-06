#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 17:35:10 2017

Decide which food and drink options to buy for the party
SE Challenge

@author: Chris
"""

import numpy as np

# This function will plan which food and drinks to buy for
# A party given peoples preferences and a total budget
# Input: budget (integer), drinkFile, foodFile, peopleFile (string filename) 
def planParty(budget,drinkFile,foodFile,peopleFile):
    #Person class for storing information about them
    class Person:
        # Store persons preferences in food and drink, and their relative value
        name = ''
        drinks = set()
        food = set()
        foodVal = 0
        drinkVal = 0
    
    # Load in food, drink, and people
    drinks = open('drinks.txt','r')
    food = open('food.txt','r')
    # Hacky way to get the text lines into people variable
    # and ensure to close file
    people = open('people.txt','r')
    temp = people.readlines()
    people.close();
    people=temp

    
    foodMap = {foodItem.split(':')[0]:[int(foodItem.split(':')[1]), 0, 0] for foodItem in food.readlines()}
    drinkMap = {drinkItem.split(':')[0]:[int(drinkItem.split(':')[1]), 0, 0] for drinkItem in drinks.readlines()}
    drinks.close()
    food.close()
    
    peopleList = []
    #Read in all people
    for i in range(int(len(people)/3)):
        newPerson = Person()
        newPerson.name = people[i*3]
        newPerson.drinks = set(people[i*3+1].strip().split(','))
        newPerson.drinkVal = (1/len(newPerson.drinks))+1/(len(people)**.3)
        newPerson.food = set(people[i*3+2].strip().split(','))
        newPerson.foodVal = (1/len(newPerson.food))+1/(len(people)**.3)
        peopleList.append(newPerson)
        for foodItem in newPerson.food:
            foodMap[foodItem][1]+=newPerson.foodVal
            foodMap[foodItem][2]+=1
        for drinkItem in newPerson.drinks:
            drinkMap[drinkItem][1]+=newPerson.drinkVal
            drinkMap[drinkItem][2]+=1
    
    # Find and buy most popular food and drink based on number of people that like it
    # Simple approach to ensures at least 1 food item and 1 drink item
    totalValue = 0
    allOptions = {}
    bestDrink = ['',0]
    for item in drinkMap:
        allOptions[item] = [0,drinkMap[item][0],drinkMap[item][1]]
        if drinkMap[item][2]>bestDrink[1]:
            bestDrink = [item,drinkMap[item][2]]
        totalValue +=drinkMap[item][2]
    
    bestFood = ['',0]
    for item in foodMap:
        allOptions[item] = [1,foodMap[item][0],foodMap[item][1]]
        if foodMap[item][2]>bestFood[1]:
            bestFood = [item,foodMap[item][2]]
        totalValue +=foodMap[item][2]
            
    drinkChoice = [bestDrink[0]]
    foodChoice = [bestFood[0]]
    del allOptions[bestDrink[0]]
    del allOptions[bestFood[0]]
    budget-=drinkMap[bestDrink[0]][0]-foodMap[bestFood[0]][0]
    
    # Knapsack 0-1 FPTAS Algorithm (Dynamic Algorithm turned Polynomial)
    eps = .05
    k = eps*totalValue/len(allOptions)
    # Scale all items based on total value
    for item in allOptions:
        allOptions[item][2]/=k
    
    #Standard Dynamic Programming Approahc ~O(N^2)
    valTab = np.zeros((len(allOptions)+1,budget+1)) 
    itemList = list(allOptions.keys())
    # Create our maximum value matrix
    for i in range(1,len(allOptions)+1):
        for j in range(1,budget+1):
            if allOptions[itemList[i-1]][1]>j:
                valTab[i][j]=valTab[i-1][j]
            else:
                valTab[i][j]=max(valTab[i-1][j],allOptions[itemList[i-1]][2]+valTab[i-1][j-allOptions[itemList[i-1]][1]])
   
    # Recover which items we picked above
    i = len(allOptions)
    j = budget
    while i>0:
        if abs(valTab[i][j]-valTab[i-1][j-allOptions[itemList[i-1]][1]]-allOptions[itemList[i-1]][2])<.001:
            if allOptions[itemList[i-1]][0]:
                foodChoice.append(itemList[i-1])
            else:
                drinkChoice.append(itemList[i-1])
            j -= allOptions[itemList[i-1]][1]
        i -=1
        
    # Post Processing Statistics
    drinkSet = set(drinkChoice)
    foodSet = set(foodChoice)
    noDrink = 0
    noFood = 0
    nothing = 0
    averageDrink = 0
    averageFood = 0
    for person in peopleList:
        drinkOption = 0
        foodOption = 0
        for drink in person.drinks:
            if drink in drinkSet:
                drinkOption+=1
        for item in person.food:
            if item in foodSet:
                foodOption+=1
        averageFood += foodOption
        averageDrink+=drinkOption
        if drinkOption == 0:
            noDrink+=1
        if foodOption == 0:
            noFood+=1
        if foodOption == 0 and drinkOption == 0:
            nothing+=1      
    averageDrink/=len(peopleList)
    averageFood/=len(peopleList)
    
    #Print statistics based on our algorithm
    print(str(noDrink) + ' people with no drink preferences chosen.\n')
    print(str(noFood) + ' people with no food preferences chosen.\n')
    print(str(nothing) + ' people with no food or drink preferences chosen.\n')
    print(str(averageDrink) + ' average preferenced drinks per person.\n')
    print(str(averageFood) + ' average preferenced food items per person.\n')
    print(str(len(drinkSet))+' total drinks chosen for the party.\n')
    print(str(len(foodSet))+' total food items chosen for the party.\n')
    return [drinkChoice,foodChoice]

# Run default if main file
if __name__ == "__main__":
    # 100 drinks, foods, and 1000 people
    budget = 150
    partyPlan = planParty(budget,'drinks.txt','food.txt','people.txt')
    drinks = partyPlan[0]
    food = partyPlan[1]
