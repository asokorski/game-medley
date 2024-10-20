import random
import time

def response_validation(prompt, valid_responses):
    while True:
        answer = input(prompt).lower()
        if answer in valid_responses:
            return answer
        else:
            print(f"Please type one of the options: {valid_responses}")

def guess_the_number():
    print(">Welcome to Guess the Number game. The rule is to guess the integer that the other side is thinking about.")
    print(""">Do you want to be guessing or want me to guess?
    1 - I wanna guess!
    2 - I want you to guess!""")
    decision = input("Choose: ")
    if decision == str(1):
        while True:
            x = input(">Up to what number would you like to guess? ")
            try:
                int(x)
                break
            except ValueError:
                print(">Please enter a valid integer number")
        print(f">The range for the numbers to guess is between 1 and {x}")
        print(">Let me think about a number...")
        random_num = random.randint(1, int(x))
        time.sleep(1)
        print(">Ok, got it!")
        while True:
            while True:
                guess = input(">What's your guess? ")
                try:
                    int(guess)
                    break
                except ValueError:
                    print(">Please enter a valid integer number")
            guess = int(guess)
            if guess == random_num:
                print(">Congratulations! You got it!")
                print("")
                break
            elif guess > random_num:
                print(">That's too big!")
            elif guess < random_num:
                print(">That's too small!")
            else:
                print(f">Choose an integer between 1 and {x}")
    elif decision == str(2):
        while True:
            x = input(">Up to what number should I guess? ")
            try:
                int(x)
                break
            except ValueError:
                print(">Please enter a valid integer number")
        y = 1
        print(f">Your number is somewhere between {y} and {x}")
        while True:
            print(">Hmmm...")
            time.sleep(0.5)
            guess = random.randint(int(y), int(x))
            answer = response_validation(f">Is it {guess}? yes/no: ", ['yes', 'no'])
            if answer == "yes":
                print(">I got it!")
                print("")
                break
            elif answer == "no":
                guess_specify = response_validation(f">Is it higher or lower? h/l: ", ['h', 'l'])
                time.sleep(0.5)
                if guess_specify == "h":
                    if int(guess) + 1 < int(x):
                        y = int(guess) + 1
                    else:
                        print("Cannot be that high...")
                elif guess_specify == "l":
                    if int(guess) - 1 > 1:
                        x = int(guess) - 1
                    else:
                        print("Cannot be that low...")
        pass
    else:
        print("Type 1 or 2")
                      

