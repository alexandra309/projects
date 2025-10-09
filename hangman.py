import random


words = ["lantern", "blizzard", "puzzle", "whisper", "canyon", "velvet",
         "orbit", "sapphire", "cactus", "enigma", "chimney", "galaxy",
         "tornado", "violin", "mirage", "anchor", "eclipse", "meadow",
         "tundra", "potion"]

word = random.choice(words)

print("Welcome to the Hangman!")

guesses = len(word) + 2
guessed_letters = set()

for i in word:
    print("_", end="")
print()
print(f"You have {guesses} guesses left")

while guesses > 0 :
    letter = input("Guess a letter: ").lower()
    if not letter.isalpha() and len(letter) != 1 :
        print("Sorry, that's not a letter, try again.")
        continue

    if letter in word:
        if letter in guessed_letters:
            print(f"You already guessed the letter '{letter}'. Try again.")
            continue
        else:
            print(f"You guessed the letter '{letter}'")
            guessed_letters.add(letter)

        display_word = []
        for letter in word:
            if letter in guessed_letters:
                display_word.append(letter)
            else:
                display_word.append("_")
        print("".join(display_word))

        if "_" not in display_word:
            print("\nYou guessed the word!")
            print(f"The word was: {word}")
            break

    else:
        print("Sorry, that letter is not in the word.")
        guesses -= 1
        print(f"You have {guesses} guesses left")
else:
    print(f"You lose! The word was '{word}'")



            