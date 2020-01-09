#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random 
moves=["Rock", "Paper", "Scissors"]
keep_playing= "true"
while keep_playing== "true":
    cmove=random.choice(moves)
    pmove=input("Rock, Paper or Scissors")
    print("The computer chose",cmove)
    if pmove==cmove:
        print("Tie")
    elif pmove== "Rock" and cmove== "Scissors":
        print("Player wins")
    elif pmove== "Rock" and cmove== "Paper":
        print("Computer wins")
    elif pmove== "Paper" and cmove== "Rock":
        print("Player wins")
    elif pmove== "Paper" and cmove== "Scissors":
        print("Computer wins")
    elif pmove== "Scissors" and cmove== "Paper":
        print("Player wins")
    elif pmove== "Scissors" and cmove== "Rock":
        print("Computer wins")
        
    
        


# In[ ]:




