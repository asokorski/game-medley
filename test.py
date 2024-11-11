
plain = "apple"
hidden = ["_ _ _ _ _"]
guessed = []
display_word = ""
incorrect_counter = 0

while True:
    guessed_letter = input("Guess the letter: ")
    if guessed_letter in plain:
        guessed.append(guessed_letter)
    for letter in plain:
        if letter in guessed:
            display_word += ''.join(f"{letter} ")
        else:
            incorrect_counter += 1
            display_word += ''.join("_ ")
    print(display_word)
    if display_word.replace(" ", "") == plain:
        print(f'Congrats! You guessed the word "{plain}"! Incorrect guesses: {str(incorrect_counter)}')
        break
    else:
        display_word = ""

#incorrect counter doesnt work