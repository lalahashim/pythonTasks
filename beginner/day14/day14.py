import day14art
from day14data import data
import random

print(day14art.logo)
continue_game = True
score = 0
variant_b = random.choice(data)

while continue_game:
    variant_a = variant_b
    variant_b = random.choice(data)
    while variant_a == variant_b:
        variant_b = random.choice(data)

    def format_data(variant):
        variant_name = variant["name"]
        variant_country = variant["country"]
        variant_description = variant["description"]
        return f"{variant_name} - {variant_description} from {variant_country}"
    
    print(f"Compare A: {format_data(variant_a)}")
    print(day14art.vs)
    print(f"Against b: {format_data(variant_b)}")
    choice = input("Who has more followers? Type 'A' or 'B': ").upper
   
    if variant_a["follower_count"] > variant_b["follower_count"]:
        answer = 0
    else:
        answer = 1

    if choice == "A":
        chosen = 0
    else:
        chosen = 1

    if answer == chosen:
        score += 1
        print(f"You're right! Your current score: {score}\n")
    else:
        continue_game = False
        print(f"Sorry, that's wrong. Your final score: {score}")
