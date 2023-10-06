import random

from hangman_words import word_list

from stages import HANGMAN, logo

print(logo)

lives = 6

end_of_game = False

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(chosen_word)

display = []

for _ in range(word_length):
  display += "_"

while not end_of_game:
  guess = input("Guess a letter : \n").lower()

  if guess in display:
    print(f"you already have guessed the letter {guess} chose another one")

  for position in range(word_length):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives = lives - 1
    print("you entered the wrong letter and lose life")
    if lives == 0:
      end_of_game = True
      print("you lose")

  print(f"{' '.join(display)}")

  if '_' not in display:
    end_of_game = True
    print("you win")

  print(HANGMAN[lives])
