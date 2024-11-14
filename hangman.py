import random

def hangman():
    phases = {1 : """





    _______""", 
    2 : """




    |
    |
    _______""",
    3 : """

    ------
    |    
    |    
    |    
    |
    |
    _______""",
    4 : """
    ------
    |    |
    |    O
    |    
    |
    |
    _______""",
    5 : """
    ------
    |    |
    |    O
    |    |
    |
    |
    _______""",
    6 : """
    ------
    |    |
    |    O
    |   /|
    |
    |
    _______""",
    7 : """
    ------
    |    |
    |    O
    |   /|\\
    |
    |
    _______""",
    8 : """
    ------
    |    |
    |    O
    |   /|\\
    |   / \\
    |
    _______"""
    }

    #function to choose the length of the word correctly - so gives error output if it's not integer or it's 0,1,2 because word would be to easy to guess
    def word_length_validation(prompt):
        while True:
            answer = input(prompt)
            try:
                answer = int(answer)
                if answer not in [0, 1, 2]:
                    return answer
                elif answer == 0:
                    print(">How do you imagine a 0-letters word?")
                else:
                    print(">C'mon, pick a longer word")
            except ValueError:
                print(">Enter an integer number")

    def validate_if_single(prompt):
        while True:
            letter = input(prompt)
            if len(letter) == 1 and letter.isalpha(): #checks is it's a single letter of latin alphabet
                return letter
            else:
                print("")
                print(">Type a single letter!")
                print("")


    print(f""">Welcome to Hangman game. Program will choose the word and you have to figure out what is it letter by letter.
    >You can choose the difficulty by choosing the word length from 2-leter word up to 20-letter word.
    >In any case you make up to 8 mistakes. Each mistake will add the next part of hangman picture.
                """)
    print("")

    #it will open the dictionary where each word is in a separate rows and convert it to a list of words
    #then pick all words of the given length into a separate list of specified_words and make a random choice from it
    while True:
        word_length = word_length_validation(">Enter the number of the letters for the word: ")
        with open("hangman_words.txt", "r") as word_list:
            words = [line.strip() for line in word_list]
            specified_words = []
            for word in words:
                if len(word) == word_length:
                    specified_words.append(word)
        if specified_words == []:
            print(">There are no words that long. Pick a smaller number of letters")
        else:
            chosen_word = random.choice(specified_words)
            break
    print(f">You've chosen a {word_length}-letter word. Good luck!")
    print("")

    #uncomment for debugging
    # print(f"FOR DEBUGGING: {chosen_word}")

    obfuscated_word = ""
    for letter in chosen_word:
        obfuscated_word += '_ '
    print(obfuscated_word)
    print("")

    wrong_guesses_counter = 0
    guessed_letters = []
    while True:
        guessed_letter = validate_if_single(">Guess the letter: ")
        if guessed_letter in chosen_word:
            if guessed_letter not in guessed_letters:
                guessed_letters.append(guessed_letter)
                print("Correct guess!")
            else:
                print("You've already guessed that letter!")
        else:
            wrong_guesses_counter += 1
            print(">Wrong guess!")
            print(phases[wrong_guesses_counter])
            print('')
        if wrong_guesses_counter == 8:
            print(f'>Sorry to say, but you didn\'t make it! The word you were looking for was "{chosen_word}".')
            print('')
            break
        display_word = ' '.join([letter if letter in guessed_letters else "_" for letter in chosen_word]) #will get the currently guessed letters and _ together
        print("")
        print(f'Guessed: {display_word}')
        print("")
        if display_word.replace(" ", "") == chosen_word:
            print(f'>Congrats! You guessed the word "{chosen_word}"! Incorrect guesses: {str(wrong_guesses_counter)}')
            print('')
            break