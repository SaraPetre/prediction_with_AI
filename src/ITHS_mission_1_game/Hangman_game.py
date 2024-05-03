import random


def read_name_list(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def choose_word(word_list):
    return random.choice(word_list)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    max_attempts = 6
    word_list = read_name_list("names.txt")
    word_to_guess = choose_word(word_list)
    guessed_letters = []
    attempts = 0

    print("Welcome to Hangman! Lets play a game where you quess the name\nof one of the top 10 ranking femala names in Sweden!")

    while True:
        print("\nThis is the secret word: " + display_word(word_to_guess, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"\nGood guess! {guess} is in the secret word!")
        else:
            print("\nWrong guess! Guess again!")
            attempts += 1

        if display_word(word_to_guess, guessed_letters) == word_to_guess:
            print("\nCongratulations! You've guessed the word: " + word_to_guess)
            break

        if attempts >= max_attempts:
            print("You've run out of attempts. The word was: " + word_to_guess)
            break


if __name__ == "__main__":

    hangman()
