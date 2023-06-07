import random, os, time
from wordbank import HANGMANPICS, words
def main():

    chosenWord = random.choice(words).lower()

    display = popWord(chosenWord)
    guesses = []
    # main game loop
    lives = 6
    stage = 0
    while True:
        print(f"The word is {chosenWord}")
        print(HANGMANPICS[stage])
        print(display)
        guess = input("Guess a letter: ").lower()
        if guess in guesses:
            print(f"You have already guessed the letter {guess}!")
            time.sleep(1)
        elif guess not in chosenWord:
            lives -= 1
            stage += 1
            guesses += guess
        else:
            for letter in range(len(chosenWord)):
                if chosenWord[letter] == guess:
                    display[letter] = guess
            guesses += guess

        # Exit conditions
        if lives == 0:
            print(HANGMANPICS[stage])
            print(f"Game over. You ran out of lives! The word was {chosenWord}")
            break
        elif not "_" in display:
            print(display)
            print(f"Game over! You guessed the word {chosenWord} correctly with {lives} lives remaining!\n")
            break
        os.system('cls')

def popWord(word):
    display = []
    for letter in word:
        display += "_"
    return display


if __name__ == "__main__":
    main()