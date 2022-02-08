#Miniproject: (3 hours) 

#rock paper scissor

n = int(input("Please Number of games you want to play ?"))

#1 player: user  2nd player: system
'''

How to collect user input ==> input

How to collect system input ==> random
'''
import random

Li1 = ["Rock","Paper","Scissor"]

user_points = 0
system_points = 0
tie = 0
for i in range(1, n+1):
    player_1 = input("Please enter the your choice(Rock, Paper, Scissor)").capitalize()
    player_2 = random.choice(Li1)
    print("Player input", player_1)
    print("System input", player_2)
    
    if player_1 == player_2 :
        print("Tie")
        tie = tie + 1                
    elif player_1 == "Rock" :
        if player_2 == "Scissor" :
            print("Player wins! system lose! Rock wins")
            user_points = user_points + 1
        else :
            print("System wins! You lose! Paper wins")
            system_points = system_points + 1
    elif player_1 == "Paper" :
        if player_2 == "Rock":
            print("Player wins! System lose! Paper wins")
            user_points = user_points + 1
        else :
            print("System wins! You lose! Scissor wins")
            system_points = system_points + 1
    elif player_1 == "Scissor" :
        if player_2 == "Rock":
            print("Player wins! system lose! Rock wins")
            user_points = user_points + 1
        else :
            print("System wins! You lose! Scissor wins")
            system_points = system_points + 1
    else :
        print("Invalid Enter")
    print("User point:", user_points)
    print("system points:", system_points)
    print("ties:", tie)
if user_points > system_points:
    print("USER wins the game !!! Congrats !!!!")
else:
    print("You lose the game !!! Try agai!!!")
    
'''
    
    
rock + rock ==> Tie
paper + paper ==> Tie
scissor + scissor ==> Tie

rock + scissor ==> rock
paper + scissor ==> scissor 
rock + paper  ===> paper




print(random.choice(Li1))
print(random.choice(Li1))
print(random.choice(Li1))

Number of games you want to play ? collect one integer

Who wins?

Number of games you want to play ?  3

Game 1:
Give your input ["rock","paper","scissor"] : rock
System input: random 


Game 2:

Give your input ["rock","paper","scissor"] : rock
System input: random 

Game3

Give your input ["rock","paper","scissor"] : rock
System input: random 

Total of number games: 3
System points ==> 0
User point ==> 2
Tie ===> 1

USER wins the game !!! Congrats !!!!

'''
