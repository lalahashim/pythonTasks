import day12art
import random

print(day12art.logo)
print("Welcome to the Number Guessing Game!")

def restart():
    print("I'm thinking of a number between 1 and 100.")
    comp_guess = random.randint(1, 100)

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty_level == "easy":
        attempt = 10
        print("You have 10 attempts remaining to guess the number.")
    else:
        attempt = 5
        print("You have 5 attempts remaining to guess the number.")

    continue_guessing = True
    while continue_guessing == True:
        players_guess = int(input("Make a guess: "))
        if players_guess != comp_guess:
            attempt -= 1
            if players_guess > comp_guess:
                print("Too high.")
            else:
                print("Too low.")
            print(f"Guess again.\nYou have {attempt} attempts remaining to guess the number.")
        elif players_guess == comp_guess:
            continue_guessing = False
            print(f"You got it! The answer was {comp_guess}.")
        
        if attempt == 0:
            continue_guessing = False
            print(f"You've run out of guesses, you lose.")

    while input("Do you want to restart? Type 'yes' or 'no': ") == "yes":
        restart()

restart()