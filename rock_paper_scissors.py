import random


def cpu_turn():
    cpu__choice = random.randint(1,3)
    cpu_turn_dict = {1:"Rock!", 2:"Paper!", 3:"Scissors!"}
    return cpu_turn_dict[cpu__choice]

def player_turn(input):
    return {"1":"Rock!", "2":"Paper!", "3":"Scissors!"}[input]

def response_validation(prompt, valid_responses):
    while True:
        answer = input(prompt)
        if answer in valid_responses:
            return answer
        else:
            print(f">Please type one of the options: {valid_responses}")


def round_score(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == "Rock!" and computer_choice == "Scissors!") or \
        (player_choice == "Scissors!" and computer_choice == "Paper!") or \
        (player_choice == "Paper!" and computer_choice == "Rock!"):
        return "You won this round!"
    else:
        return "Computer won this round!"

def rock_paper_scissors():
    print(f""">This is a "Rock, Paper, Scissors" game where for every round the computer makes a pre-choice, it let\'s you make your choice and compares the results
    The game modes are:
    1 - Best of 3
    2 - Best of 5
    3 - Best of 10
    """)
    game_mode = response_validation(">Choose your game mode: ", ["1", "2", "3"])
    print("")
    modes_dict = {"1":"Best of 3", "2":"Best of 5", "3":"Best of 10"}
    print(f">You've choosen {modes_dict[game_mode]}. Good luck!")
    print("")

    total_rounds = {"1":3, "2":5, "3":10}
    rounds_needed = total_rounds[game_mode]
    cpu_score_counter = 0
    player_score_counter = 0
    while True:
        print(f"""Enter 1 for rock
Enter 2 for paper
Enter 3 for scissors
    """)
        computer_choice = cpu_turn()
        print("Computer has made its choice")
        player_choice = player_turn(response_validation(">What is your choice? ", ["1", "2", "3"]))
        print("")
        print(f"Player choice: {player_choice}")
        print(f"Computer choice: {computer_choice}")
        result = round_score(player_choice, computer_choice)
        print(result)
        print("")
        if result == ">You won this round!":
            player_score_counter += 1
        elif result == ">Computer won this round!":
            cpu_score_counter += 1
        print(f""">Current score table: 
            Player: {player_score_counter} 
            Computer: {cpu_score_counter}""")
        if player_score_counter == rounds_needed:
            print(">Player has won the game!")
            print("")
            break
        if cpu_score_counter == rounds_needed:
                print(">Computer has won the game!")
                print("")
                break