import random

word_list = ["elephant", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []

# For each letter in the chosen_word, add a "_" to 'display'.
for _ in range(len(chosen_word)):
    display.append("_")

print(display)

guess = input("Guess a letter: ").lower()

matched_letter_count = chosen_word.count(guess)
print(matched_letter_count)
for _ in range(matched_letter_count):
    display[chosen_word.index(guess)] = guess
    chosen_word = chosen_word.replace(guess, '_', 1)
    print(display)

print(display)
