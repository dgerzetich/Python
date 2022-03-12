'''
Created on Mar 11, 2022
The Objective of this program is to quiz the user on basic high school
trivia. The user will be asked questions.The user should input a letter for each
question. (A, B, or C). The program will check the users answer, and tell the 
user if it is correct or not. The program will track correct and incorrect 
answers..
@author: Daria
'''
#Make a variable called score to keep track of the correct answers. And set
#it to 0.
score = 0
#Ask the user question one. And store the users answer.
science = input("1) What is the powerhouse of the cell? A)mitochondria B)nucleus C)ribosome")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(science.upper() == "A"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is A")
#Ask the user question two. And store the users answer.
geo = input(" 2) How many states comprise the United States? A)13 B)45 C)50")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(geo.upper() == "C"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is C")
#Ask the user question three. And store the users answer.
m = input("3) In y = mx + b, what does m stand for? A)slope B)output C)I don't understand math")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is A."
if(m.upper() == "A"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is A")
#Ask the user question four. And store the users answer.
e = input("4) In English, a person, place or thing is called: A)verb B)adjective C)noun")
#Check if the answer is correct, if it is add one to score and print out
#"Correct"
#Else, print out "Incorrect, the correct answer is C."
if(e.upper() == "C"):
    print("Correct")
    score = score + 1
else:
    print("Incorrect, the correct answer is C")
#Calculate the percentage the user got. And store it in a variable called p
if(score == 0):
    p = 0
elif(score == 1):
    p = 25
elif(score == 2):
    p = 50
elif(score == 3):
    p = 75
else:
    p = 100
#Print out the users score: "You got a [score]/4. Or a [p]%."
if(score == 0):
    print("You got a 0/4 or a 0%.") 
elif(score == 1):
    print("You got a 1/4 or a 25%.") 
elif(score == 2):
    print("You got a 2/4 or a 50%.") 
elif(score == 3):
    print("You got a 3/4 or a 75%.") 
else:
    print("You got a 4/4 or a 100%.") 
