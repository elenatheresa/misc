'''
rock paper scissors game 

input string 
random output of rock, paper, scissors
 
rock beats scissors 
scissors beats paper
paper beats rock

'''

import random
print("Play the Game, Enter Rock, Paper, Scissors: ")
print()
player1 = str(input())
player2 = ["Rock", "Paper", "Scissors"]
player2Choice = random.choice(player2)
#print(player2Choice)


if player1 == "Rock" and player2Choice == "Rock":
    print("It's a Draw! Player 1: ", player1, "Computer: ", player2Choice)
elif (player1 == "Rock" and player2Choice == "scissors") or (player1 == "Scissors" and player2Choice == "Paper") or (player1 == "Rock" and player2Choice == "Scissors"):
    print("Player 1 wins! Player 1: ", player1, "Computer: ", player2Choice)
elif (player2Choice == "Rock" and player1 == "scissors") or (player2Choice == "Scissors" and player1 == "Paper") or (player2Choice == "Rock" and player1 == "Scissors"):
    print("Computer Wins! Player 1: ", player1, "Computer: ", player2Choice)

