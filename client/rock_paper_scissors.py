"""
@author: Kemoy Campbell
date: 11/03/2023
Project code name: HandBattle
Purpose:
    A program that play rock, paper, scissors
"""

import datetime
import random
import requests
from tqdm import tqdm
import time


base_url = "http://localhost/leaderboard-svp/web/api"

def send_request(endpoint, payload, method='POST'):
    uri = f"{base_url}{endpoint}"
    if method.upper() == 'GET':
        response = requests.get(uri, params=payload)
    else:
        response = requests.post(uri, json=payload)

    return response.json()


"""
    This function will register a client with the server.
    If the client is a new client then it will add a new row in the database
    If the client already exists then it will return the existing client id
    
    The server returns a json with success and if if all goes well
"""
def register_client(client_id):
    endpoint = "/add_player.php"
    payload = {
        "name": client_id
    }

    return send_request(endpoint, payload)


def update_stat(id, type):
    endpoint = "/update_stat.php"
    payload = {
        "id": id,
        "field": type
    }

    return send_request(endpoint, payload)


def update_win(id):
    return update_stat(id, "wins")


def update_losses(id):
    return update_stat(id, "losses")


#SVP CODES HERE - Challenges
def get_current_position_on_leaderboard(id):
    # CODE THE CHALLENGE HERE
    # ... 
    
    # DO NOT DELETE BELOW
    response = response[0]
    return response["rank"]
#End of SVP CODES HERE - Challenges 


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
    #SVP CODES HERE to simulate computer thinking with tqdm - Challenges
    print("Computer is thinking...")
    
    # CODE THE CHALLENGE HERE
    # ... 

    print("Computer has made a choice!")
    print("Computer's choice will not be revealed until you make your pick...")
    time.sleep(1)
    #End of SVP CODES HERE

    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


#STUDENT CODE HERE
#STUDENT FUNCTIONS HERE
def determine_winner(player_choice, computer_choice):
    player = "Player Wins"
    winner = "Computer wins!"
    if player_choice == computer_choice:
        winner = "It's a tie!"
    elif player_choice == "rock" and computer_choice == "scissors":
        winner = player
    elif player_choice == "paper" and computer_choice == "rock":
        winner = player
    elif player_choice == "scissors" and computer_choice == "paper":
        winner = player
    
    return winner


def quit():
    while True:
        choice = input('Press "Enter" to play again or type "quit": ').strip().lower()
        if choice == "quit":
            return "quit"
        if choice == "":
            return "yes"
        print("Invalid!")


def get_user_choice():
    while True:
        choice = input("Enter your choice(rock, paper, scissors): ")
        choice = choice.lower()
        if choice !="rock" and choice !="scissors" and choice !="paper":
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
    client_id = ""
    server_response = dict()

    #SVP CODES HERE
    # ...
    #END SVP CODES

    # API should always return dict with "success"
    if not isinstance(server_response, dict) or not server_response.get("success"):
        print("Error registering client:", server_response.get("error", server_response))
        exit(0)

    client_id = server_response["id"]
    print("Client ready. id:", client_id)
    
    while True:
        #STUDENT CODE HERE
        game_header()
        
        #SVP CODES HERE - Challenges
        # CODE THE CHALLENGE HERE
        # ...
        #End of SVP CODES HERE - Challenges

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
            total_player_score += 1
            total_player_xp += xp
            #SVP CODES HERE
            # ...
            #End of SVP CODES HERE
        elif winner == "Computer wins!":
            total_computer_score += 1
            total_computer_xp += xp
            #SVP CODES HERE
            # ...
            #End of SVP CODES HERE
        
        print(f"You: {user_choice} vs Computer: {computer_choice}")
        print("Winner: ", winner)
        
        round += 1
        
        play_again = quit()
        if play_again == "quit":
            print("Thank you for playing!!! Goodbye...")
            break
        
    
#PREDEFINED
main()