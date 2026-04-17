import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def make_phonetic():
    user_name = input("Enter your name: ").upper()
    try:
        code_name = [alphabet_dict[letter] for letter in user_name]
        print(code_name)
    except KeyError:
        print("Sorry, only letters in the alphabet.")
        make_phonetic()


make_phonetic()
