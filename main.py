from guess_the_number import guess_the_number

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
        """)
    game = input("I want to play a game number... ")
    if game == "0":
        print("See you next time!")
        break
    elif game == "1":
        print("")
        guess_the_number()


# to be fixed - gets error when "up to what number" and "guess number" is not intiger
