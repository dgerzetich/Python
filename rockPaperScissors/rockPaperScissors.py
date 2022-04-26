'''
Created on Apr 25, 2022

@author: Daria Gerzetich

Rock, paper, scissors game for user to play against computer. 
'''
import random


keepPlaying = True
while(keepPlaying == True):
    print("Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit")
    userScore = 0
    cpuScore = 0
    while(userScore < 2 and cpuScore < 2): 
        userChoice = input("Please choose (rock, paper, scissors, or q): ").lower()
        option = ["rock", "paper", "scissors"]
        cpuChoice = random.choice(option)
        
        if((userChoice == "rock" and cpuChoice == "scissors") or (userChoice == 
            "paper" and cpuChoice == "rock") or (userChoice == "scissors" and 
            cpuChoice == "paper")):
            print("User Won!")
            userScore = userScore + 1
            print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
        elif((userChoice == "rock" and cpuChoice == "paper") or (userChoice == 
            "paper" and cpuChoice == "scissors") or (userChoice == "scissors" and 
            cpuChoice == "rock")):
            print("CPU Won!")
            cpuScore = cpuScore + 1
            print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
        elif((userChoice == "rock" and cpuChoice == "rock") or (userChoice == 
            "paper" and cpuChoice == "paper") or (userChoice == "scissors" and 
            cpuChoice == "scissors")):
            print("DRAW")
            print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
        elif(userChoice.lower() == 'q'):
            keepPlaying = False 
            break
        else:
            print("Not an option. Try again.")
    print("Thanks for playing! ")
    if(userScore == 2):
        print("You Win!")
    elif(cpuScore == 2):
        print("CPU Wins!")
    
    print("User: " + str(userScore) + ", CPU: " + str(cpuScore))
    
        
        



