"""
@author: Kemoy Campbell
date: 11/03/2023
Project code name: HandBattle
Purpose:
    A program that play rock, paper, scissors
"""

import datetime
import random

#PREDEFINED
"""
    This function will print the header containing 
    Rock, paper,scissors as well as today's date and time
"""
def game_header():
    print("==============================")
    rock = "Rock:🗿"
    paper = "Paper:📃"
    scissors = "Scissors:✂️"
    print(f"{rock} {paper} {scissors}")
    print("\n\tGame Version 0.1")
    print("==============================\n")
    now = datetime.datetime.now()
    print("Date and Time:",now.strftime("%d/%m/%Y %H:%M:%S"))

#PREDEFINED
"""
    This function generate an xp.
    The function first generate an xp
    then multiply that by the round number

    Parameter:
        round: The current round in the game

    returns the xp for the round
"""
def generate_xp(round):
    min_xp = 1
    max_xp = 30
    xp = random.randint(min_xp, max_xp)
    return xp * round

#PREDEFINED
"""
    This function will randomly pick a choice for the computer.
    This will return one of the following, "rock", "paper" or "scissor"
"""
def get_computer_choice():
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)


#STUDENT CODE HERE
#STUDENT FUNCTIONS HERE
def determine_winner(player_choice, computer_choice):
    player = "Player Wins"
    winner = "Computer wins!"
    if player_choice == computer_choice:
        winner = "It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissor":
        winner = player
    elif player_choice == "paper" and computer_choice == "rock":
        winner = player
    elif player_choice == "scissor" and computer_choice == "paper":
        winner = player
    
    return winner

def quit():
    while True:
        choice = input("Play again? (yes/quit):").lower()
        if choice!="quit" and choice!="yes":
            print("Invalid!")
            continue
        return choice
    

def get_user_choice():
    while True:
        choice = input("Enter your choice(rock, paper, scissor):")
        choice = choice.lower()
        if choice!="rock" and choice!="scissor" and choice!="paper":
            print("Invalid choice!")
            continue
        return choice




#PREDEFINED
def main():
    #STUDENT CODE HERE - VARIABLES DECLARATION
    round = 0
    computer_choice = ""
    user_choice = ""
    winner = ""
    total_computer_score = 0
    total_player_score = 0
    total_computer_xp = 0
    total_player_xp = 0
    while True:
        #STUDENT CODE HERE
        game_header()
        print("Previous round result\n============")
        print("Previous computer choice:",computer_choice)
        print("Previous user's choice:", user_choice)
        print("Previous winner:", winner)
        
        print("\nScores:\n==========")
        print("Total computer score:", total_computer_score)
        print("Total computer XP:", total_computer_xp)
        print("\nTotal player score:", total_player_score)
        print("Total player xp:", total_player_xp)
        
        
        
        computer_choice = get_computer_choice()
        user_choice = get_user_choice()
        winner = determine_winner(user_choice, computer_choice)
        xp = generate_xp(round)
        
        if winner == "Player Wins":
            total_player_score +=1
            total_player_xp+=xp
        elif winner == "Computer wins!":
            total_computer_score+=1
            total_computer_xp +=1
        
        print(f"You:{user_choice} vs Computer:{computer_choice}")
        print("Winner:", winner)
        
        round+=1
        
        play_again = quit()
        if play_again == "quit":
            print("Thank you for playing!!! Goodbye...")
            break
        
        


#PREDEFINED
main()