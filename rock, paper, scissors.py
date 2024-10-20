import random
import time

print('This is a "Rock, Paper, Scissors" game where for every round the computer makes a pre-choice, then let\'s you decide and compares the result')
print("")

def cpu_turn():
    cpu__choice = random.randint(1,3)
    if cpu__choice == 1:
        cpu__choice = "Rock!"
    elif cpu__choice == 2:
        cpu__choice = "Paper!"
    elif cpu__choice == 3:
        cpu__choice = "Scissors!"
    return cpu__choice

def player_turn(input):
    if input == 1:
        player_choice = "Rock!"
    if input == 2:
        player_choice = "Paper!"
    if player_choice == 3:
        player_choice = "Scissors!"
    return player_choice

def response_validation(prompt, valid_responses):
    while True:
        answer = int(input(prompt))
        if answer in valid_responses:
            return answer
        else:
            print(f"Please type one of the options: {valid_responses}")

def round_score(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock!" and computer_choice == "Scissors!") or \
        (player_choice == "Scissors!" and computer_choice == "Paper!") or \
        (player_choice == "Paper!" and computer_choice == "Rock!"):
        return "You won this round!"
    else:
        return "Computer won this round!"

while True:
    print("Enter 1 for rock")
    print("Enter 2 for paper")
    print("Enter 3 for scissors")
    print("")
    cpu_score_counter = 0
    player_score_counter = 0
    computer_choice = cpu_turn()
    print("Computer has made its choice")
    player_choice = player_turn(response_validation("What is your choice? ", [1, 2, 3]))
    print("")
    print(f"Player choice: {player_choice}")
    print(f"Computer choice: {computer_choice}")
    print(round_score(player_choice, computer_choice))
    print("")
    if round_score(player_choice, computer_choice) == "You won this round!":
        player_score_counter += 1
    elif round_score(player_choice, computer_choice) == "Computer won this round!":
        cpu_score_counter += 1
    print(f"Current score table: \
          Player: {player_score_counter} \
          Computer: {cpu_score_counter}")
    
#score counter doesn't work correctly - to be fixed