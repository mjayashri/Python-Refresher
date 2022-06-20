# Step 2
import random
import hangman_words
import hangman_art

chosen_word = random.choice(hangman_words.word_list)
lives = 6
end_of_game = False

print(hangman_art.logo)
# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = [];
guessed_letters = []
for letter in chosen_word:
    display.append("_")

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    if guess in guessed_letters:
        print("You already guessed it!")
        continue
    guessed_letters.append(guess)
    for i in range(0, len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = chosen_word[i]
    print(display)
    if guess not in chosen_word:
        lives -= 1
        print(hangman_art.stages[lives])
        if lives == 0:
            end_of_game = True
            print("You Lose!!")
    if "_" not in display:
        end_of_game = True
        print(f"letter is {''.join(display)}, you guessed it right")
