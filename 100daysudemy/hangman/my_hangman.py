from hangman_words import word_list
import random

hangman = '''
         +---+  
         |   |  
         |   O  
         |  /|\ 
         |  / \ 
         |      
     =========  
'''


def get_hangman_part(part):
  hangmanList = list(hangman)

  if part == 0:
    hangmanList[31] = " "
    hangmanList[48] = " "
    hangmanList[64] = " "
    hangmanList[65] = " "
    hangmanList[66] = " "
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 1:
    hangmanList[48] = " "
    hangmanList[64] = " "
    hangmanList[65] = " "
    hangmanList[66] = " "
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 2:
    hangmanList[64] = " "
    hangmanList[65] = " "
    hangmanList[66] = " "
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 3:
    hangmanList[65] = " "
    hangmanList[66] = " "
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 4:
    hangmanList[66] = " "
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 5:
    hangmanList[81] = " "
    hangmanList[83] = " "
  elif part == 6:
    hangmanList[83] = " "

  return "".join(hangmanList)


def change_display(letter, word, display):
  display_list = list(display)
  for i in range(len(word)):
    if word[i] == letter:
      display_list[i*2] = letter
  return "".join(display_list)


word = random.choice(word_list)
# print(word)
length = len(word)
display = "_ " * length

attempts = 0
correct_guesses = 0

while attempts < 7:
  print(get_hangman_part(attempts))
  print(display)
  guess = input("Make a guess: ")
  if guess in word:
    display = change_display(guess, word, display)
    correct_guesses += 1
    if correct_guesses == length:
      print("Congrats, you win! :)")
      break
  else:
    attempts += 1

if attempts >= 7:
  print("\nSorry, you lose! :(")
  print(f"The word was: {word.upper()}")

