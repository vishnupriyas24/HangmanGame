import random
def choose_word():
    word_list = ["python", "hangman", "programming", "openai", "random", "guess"]
    return random.choice(word_list)
def display_current_state(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])
def hangman():
    word = choose_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    print("Welcome to Hangman!")
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_current_state(word, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        guess = input("Guess a letter: ").lower()
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        if guess in guessed_letters:
            print("You have already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            print("Good guess!")
        else:
            guessed_letters.add(guess)
            incorrect_guesses += 1
            print("Incorrect guess.")
        if all(letter in guessed_letters for letter in word):
            print(f"\nCongratulations! You guessed the word: {word}")
            break
    else:
        print(f"\nGame Over! The word was: {word}")
if __name__ == "__main__":
    hangman()
