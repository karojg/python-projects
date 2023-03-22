NAME_PLACEHOLDER = "[name]"

with open("Input/Letters/starting_letter.txt") as letter:
    letter = letter.read()

with open("Input/Names/invited_names.txt") as names:
    names = names.readlines()

    for name in names: 
        stripped_name = name.strip()
        with open(f"Output/ReadyToSend/{stripped_name}", mode="w") as completed_letter:
            completed_letter.write(letter.replace(NAME_PLACEHOLDER, stripped_name))
