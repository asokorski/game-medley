import random
import time

def guess_the_number():
    print(">Welcome to Guess the Number game. The rule is to guess the intiger that the other side is thinking about.")
    print(""">Do you want to be guessing or want me to guess?
    1 - I wanna guess!
    2 - I want you to guess!""")
    decision = input("Choose: ")
    if decision == str(1):
        x = input(">Up to what number would you like to guess? ")
        print(f"The range for the numbers to guess if between 1 and {x}")
        print(">Let me think about a number...")
        random_num = random.randint(1, int(x))
        time.sleep(1)
        print(">Ok, got it!")
        while True:
            guess = int(input("What's your guess? "))
            if guess == random_num:
                print(">Congratulations! You got it!")
                print("")
                break
            elif guess > random_num:
                print(">That's too big!")
            elif guess < random_num:
                print(">That's too small!")
            else:
                print(f"Choose an intiger between 1 and {x}")
    elif decision == str(2):
        print("TO BE IMPLEMENTED")
        print("")
        pass
    else:
        print("Type 1 or 2")
                      
print('test')