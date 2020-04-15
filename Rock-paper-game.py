#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# this a Rock Paper Scissor Game
# user get a chance to play with computer
# function to check user inputs
def usrinput(message):
 while True:
    userInput = input(message).lower()
    if (userInput == "r") or (userInput =="p") or (userInput == "s"):
     return userInput 
     break
    else:
        print(" your input is not valide, try again!")
        continue
def re(message):
 while True:
    user = input(message).lower()
    if (user == "y") or (user =="n"):
     return user 
     break
    else:
        print(" your input is not valide, try again!")
        continue
#Main program begins
# Rock paper scissors Game
import random
while True:
    in1 = usrinput('Choose (R)ock, (P)aper or (S)cissors:')
    in2 = random.choice(['r','p','s'])
# this argument check whether both chose same input. if so use will give another game automatically
    if in1 == in2 :
        print(" There is No Winers, Both choose same") 
        continue
# user wining arugmet
    elif (in1 =="r" and in2 == "s") or (in1 =="s" and in2 =="p") or (in1 =="p" and in2 =="r"):
        print (" Congratulation ! YOU WON ")
# computer wining arugment
    else:
       print("Sorry you lost")
# ask user want to play another Game
    replay = re(" Do you want to play one more game ? \n Enter Y for yes and N for NO: ")
    if replay == "y" :
        pass
    else:
        print(" Good Bye! see you another time")    
        break


# In[ ]:




