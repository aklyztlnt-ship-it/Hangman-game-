# Hangman-game-
hangman= ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
import random
words =["office","green","yellow","blue"]
random_word=random.choice(words)
spaces=["_"]*len(random_word)
print(" ".join(spaces))
photo=0
print(hangman[photo])
lives=6
guessed_before=[]
while "_" in spaces and lives>0:
    guessed=input("please enter a letter : ")
    if guessed in guessed_before:
    	print("you wrote this before")
    	continue
    if len(guessed) != 1 or not guessed.isalpha():
        print("please enter ONE letter only")
        continue
    for x in range(len(random_word)):
        if guessed==random_word[x]:
            spaces[x]=guessed
            print(f"left {lives} to try")
    guessed_before.append(guessed)
    print(" ".join(spaces))

    if guessed not in random_word:
        lives-=1
        print(f"\nleft {lives} to try")
        if lives==0:
        	print("""======
        	      you lose
        	======""")
        photo+=1
        print(hangman[photo])
if "_" not in spaces:
    print("""=======
        	         you won
        	========""")
