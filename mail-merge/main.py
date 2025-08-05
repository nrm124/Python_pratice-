# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

PLACEHOLDER = "[name]"

with open("./input/letters/starting_letter.txt", "r") as letter:
    content= letter.read()


with open("./input/Names/invited_names.txt","r") as name:
    for n in name.readlines(-1):
        striped_n = n.strip()
        le = content.replace(PLACEHOLDER, striped_n)
        with open(f"./output/ReadyToSend/{striped_n}.txt","w") as output:
            output.write(le)








# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp