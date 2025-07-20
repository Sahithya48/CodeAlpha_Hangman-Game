import random

def hangman():
    # 5 predefined words
    word_list = ["apple", "zebra", "house", "plant", "train"]
    
    # Randomly select a word
    word = random.choice(word_list)
    guessed = ["_"] * len(word)
    guessed_letters = []
    attempts_left = 6

    print("🎮 Welcome to Hangman!")
    print("Guess the word one letter at a time.")
    print(f"You have {attempts_left} incorrect guesses.\n")

    while attempts_left > 0 and "".join(guessed) != word:
        print("Word: " + " ".join(guessed))
        print("Guessed letters:", " ".join(guessed_letters))
        print(f"Incorrect guesses left: {attempts_left}")

        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("❗ Please enter a single valid letter.\n")
            continue

        if guess in guessed_letters:
            print("❗ You already guessed that letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!\n")
            for i, char in enumerate(word):
                if char == guess:
                    guessed[i] = guess
        else:
            print("❌ Incorrect!\n")
            attempts_left -= 1

    if "".join(guessed) == word:
        print("🎉 You guessed the word:", word)
    else:
        print("💀 Game Over! The word was:", word)

# Run the game
hangman()
