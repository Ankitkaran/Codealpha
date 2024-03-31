# Codealpha
import random

def choose_word():
    words = ["hangman", "python", "programming", "computer", "game", "coding", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display

def hangman():
    word = choose_word()
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")
    print("The word has {} letters.".format(len(word)))

    while True:
        print("\nAttempts left:", attempts_left)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue
        elif len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if all(letter in guessed_letters for letter in word):
                print("Congratulations, you've guessed the word:", word)
                break
        else:
            print("Incorrect guess.")
            attempts_left -= 1
            if attempts_left == 0:
                print("Out of attempts! The word was:", word)
                break

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        hangman()
    else:
        print("Thanks for playing!")

hangman()
