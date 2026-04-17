with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()
with open("./Input/Letters/starting_letter.txt") as letter:
    let = letter.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = let.replace("[name]", stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
