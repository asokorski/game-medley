import random

# def guess(x):
#     random_number = random.randint(1, x)

def guess(x):
    random_number = random.randint(1, 999)
    while True:
        if int(guess) == random_number:
            print("You got it!")
            break
        elif int(guess) > random_number:
            print("Too high!")
        elif int(guess) < random_number:
            print("Too low!")


decision = input("Wanna play a game? ")
if decision == "no":
    print("Well, ok")
elif decision == "yes":
    print("MUAHAHAHA")
    number_guess = input("Guess the number... ")
    guess(int(number_guess))
else:
    print("Speak human")
