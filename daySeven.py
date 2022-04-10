# Step 1
import random
# Ascii art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
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
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

# word list and choosign 
word_lists = ["ardvark","baboon","camel"]
chosen_word = random.choice(word_lists)
# print(f'Pssst, the solution is {chosen_word}')
# display the blanks for the words
display = []
for i in range(len(chosen_word)):
    display+= "_"
print(display)

# Check lives
lives = 6

# State of the game:
end_of_game = False
# loop to continue for the game
print(stages[lives])
while not end_of_game:
    print(f"Number of lives left {lives}")
    if lives >= 1:
        if ("_" in display):
            # guess and check 
            guess = input("Make a letter: ").lower()
            for position in range(len(chosen_word)):
                letter = chosen_word[position]
                if letter == guess:
                    display[position] = letter
            # check for incorrect input and reducing lives
            if guess not in chosen_word:
                lives-= 1
                    
            print(stages[lives])
            print(display)
        else: 
            # state change 
            end_of_game = True
            print("You win!")
            exit
    else: 
        # state change 
        end_of_game = True
        print(stages[lives])
        print("Out of lives you lose")
        exit()