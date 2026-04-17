import random
import day7art
import day7words

print(day7art.logo)
print("Welcome to the 'Hangman' game!")

chosen_word = random.choice(day7words.word_list)
end_of_game = False
lives = 6

display = []
for letter in chosen_word:
    display += "_"

while end_of_game:
    guess = input("Guess a letter:\n").lower()

    if guess in display:
        print("You already entered this letter")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed '{guess}'. It is not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    print(day7art.stages[lives])
