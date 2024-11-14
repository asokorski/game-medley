from guess_the_number import guess_the_number
from rock_paper_scissors import rock_paper_scissors
from hangman import hangman

print("""
 _    _                                 _                                                 ___  
| |  | |                               | |                                               |__ \ 
| |  | | __ _ _ __  _ __   __ _   _ __ | | __ _ _   _    __ _    __ _  __ _ _ __ ___   ___  ) |
| |/\| |/ _` | '_ \| '_ \ / _` | | '_ \| |/ _` | | | |  / _` |  / _` |/ _` | '_ ` _ \ / _ \/ / 
\  /\  / (_| | | | | | | | (_| | | |_) | | (_| | |_| | | (_| | | (_| | (_| | | | | | |  __/_|  
 \/  \/ \__,_|_| |_|_| |_|\__,_| | .__/|_|\__,_|\__, |  \__,_|  \__, |\__,_|_| |_| |_|\___(_)  
                                 | |             __/ |           __/ |                         
                                 |_|            |___/           |___/                          
      """)

print("Welcome to the console game medley hub!")
print("")

while True:
    print("""Please choose a game from the list:
        0 - Close the program
        1 - Guess the number
        2 - Rock, paper, scissors
        3 - Hangman
        """)
    game = input("I want to play a game number... ")
    if game == "0":
        print("See you next time!")
        break
    elif game == "1":
        print("")
        guess_the_number()
    elif game == "2":
        print("")
        rock_paper_scissors()
    elif game == "3":
        print("")
        hangman()
