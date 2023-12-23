# For each name in the invite list, create a new letter using the starting_letter.txt 
# and replace the [name] placeholder with the actual name.
# Then add the letter to the readyToSend list

with open("input/names/invited_names.txt") as fnames:
    names = fnames.readlines()
    print(f"NAMES: {names}")
    for name in names:
        name = name.strip()
        with open("input/letters/starting_letter.txt") as fletter:
            letter = fletter.readlines()
            letter[0] = letter[0].replace("[name]", name)
            with open(f"output/ReadyToSend/letter_for_{name}.txt", mode="w") as f:
                f.writelines(letter)