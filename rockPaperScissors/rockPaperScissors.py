'''
Created on Apr 25, 2022

@author: Daria Gerzetich

The Objective of this program is to make a Rock, Paper, Scissors game for the user to play against the computer. The tasks to complete are:
There should be a loop to repeat the game. And the game should go as follows:
Welcome the user with "Welcome to Rock Paper Scissors! Best two out of three. Press 'q' to quit"
Create variables to keep track of score
Begin a loop to repeat rounds until somebody wins. Someone wins when they have won 2 rounds. (Rounds are outlined below).
Once someone has won, print "Thanks for playing!", print out the final scores, and if the user wins: print "You win!"; if the cpu wins: print "CPU wins!"
Repeat the whole game once someone wins. And until the user chooses to quit.
A round should go as follows:
Have the user choose rock, paper, scissors, or q
Generate a random choice from the computer
Check the users input against the computers choice to see who won the round:
if the user won, add one to the users score, then print out the scores: "User: [#], Computer [#]”
else if the computer won, add one to the computer’s score, then print out the scores: "User: [#], Computer [#]"
else if it was a draw, print "DRAW", then print out the scores: "User: [#], Computer [#]"
else if the user entered "q", then end the round, and the game loop.
else the user didn't enter an accepted input, and prompt them to try again: "Not an option try again."
repeat the round until someone wins.
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
    
        
        



