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

#def get_hangman_part()




words = ["hello", "goodbye", "tomorrow"]
word = random.choice(words)
length = len(word)


hangmanList = list(hangman)
hangmanList[31] = "."
hangmanList[48] = "."
hangmanList[64] = "."
hangmanList[65] = "."
hangmanList[66] = "."
hangmanList[81] = "."
hangmanList[83] = "."
hangman = "".join(hangmanList)
# hangman = hangman.replace("/", " ")
# hangman = hangman.replace("\\", " ")
# hangman = hangman.replace("O", " ")
# hangman = hangman.replace("!", " ")

print(hangman + '\n')
print("WORD: ", end="")
print("_ " * length)
