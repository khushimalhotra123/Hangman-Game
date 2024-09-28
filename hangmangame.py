import random

# List of words to guess
words = ["python", "java", "kotlin", "swift", "ruby", "go", "rust"]

# Choose a random word from the list
word_to_guess = random.choice(words)

# Create a list to store the guessed letters
guessed_letters = ["_"] * len(word_to_guess)

# Create a set to store the incorrect guesses
incorrect_guesses = set()

# Maximum number of incorrect guesses allowed
max_incorrect_guesses = 6

# Game loop
while True:
    # Print the current state of the word
    print(" ".join(guessed_letters))

    # Print the number of incorrect guesses
    print(f"Incorrect guesses: {len(incorrect_guesses)}/{max_incorrect_guesses}")

    # Ask the user for a guess
    guess = input("Guess a letter: ")

    # Check if the guess is a single letter
    if len(guess) != 1:
        print("Please guess a single letter!")
        continue

    # Check if the guess is already guessed
    if guess in guessed_letters or guess in incorrect_guesses:
        print("You already guessed this letter!")
        continue

    # Check if the guess is in the word
    if guess in word_to_guess:
        # Reveal the correct letter
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_letters[i] = guess
    else:
        # Add the incorrect guess to the set
        incorrect_guesses.add(guess)

    # Check if the user won
    if "_" not in guessed_letters:
        print("Congratulations, you won!")
        break

    # Check if the user lost
    if len(incorrect_guesses) == max_incorrect_guesses:
        print(f"Game over! The word was {word_to_guess}.")
        break
