import random

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

def select_word(word_length):
    with open("hangman_test.txt", "r") as word_list:
        words = [line.strip() for line in word_list]
        specified_words = []
        for word in words:
            if len(word) == word_length:
                specified_words.append(word)
    if specified_words == []:
        error_too_long = ">There are no words that long. Pick a smaller number of letters"
        return error_too_long
    else:
        return random.choice(specified_words)

print(f""">Welcome to Hangman game. Program will choose the word and you have to figure out what is it letter by letter.
>You can choose the difficulty by choosing the word length from 2-leter word up to 20-letter word.
>In cany case you make up to 5 mistakes. Each mistake will add the next part of hangman picture.
            """)
print("")

while True:
    select_word_output = select_word(word_length_validation(">Enter the number of the letters for the word: "))
    if select_word_output == ">There are no words that long. Pick a smaller number of letters":
        print(select_word_output) #prints error_too_long
    else:
        break
print(">Your word has been choosen:")

print(f"FOR DEBUGGING: {select_word_output}") #FOR DEBUGGING

letters_list = []
for letter in select_word_output:
    letters_list.append("_ ")
hidden_word = ''.join(letters_list)
print(f"""{hidden_word}
      """)



#Now to create the logic for guessing where for each guess the hidden word will be displayed and if guess is correct, the underscore(s) will be changed with the letter(s)
#Next to add a condition that when the whole word is guessed the game is won
#Next to add the guess counter, so if not guessed correctly it will subtract until the end of the game
#Next to add graphical hangman to be displayed piece by piece with each wrong guess


guessed_letters = []
guessed_letter = input("Make a guess: ")
for letter in select_word_output:
    if guessed_letter in select_word_output:
        guessed_letters += guessed_letter
    else:
        guessed_letters += '_ '
# for letter in select_word_output:
#     if letter in guessed_letters:
#         hidden_word = ''.join(guessed_letter)
#     else:
#         hidden_word = ''.join("_ ")
print(guessed_letters)