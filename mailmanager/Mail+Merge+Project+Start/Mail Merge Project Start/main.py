# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Get names
with open(
    "./Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt",
    mode="r",
) as names:
    contents = names.readlines()

# Get file format:
with open(
    "./Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt"
) as file:
    letter = file.read()
    for name in contents:
        name = name.strip()
        new_letter = letter.replace("[name]", name)  # Doesn't actually mutate letter
        with open(
            f"./Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/letterto{name}.txt",
            mode="w",
        ) as output:
            output.write(new_letter)

# Write to file location
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
