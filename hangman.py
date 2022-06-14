#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 20:04:20 2022

@author: coraliakraken8
"""

import random 
from english_words import english_words_lower_alpha_set


print('''


  _                                             
 | |                                            
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                     __/ |                      
                    |___/                       


''')


stages = ['''
           +---+
           |   |
           O   |
          /|\  |
          /\   |
               |
          ========
          ''', '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
         ========
         ''', '''
         +---+
         |   |
         O   |
        /|\  |
             |
             |
        ========
        ''', '''
        +---+
        |   |
        O   |
       /|   |
            |
            |
       ========
       ''', '''
       +---+
       |   |
       O   |
       |   |
           |
           |
      ========
      ''', '''
      +---+
      |   |
      O   |
          |
          |
          |
     ========
     ''', '''
      +---+
      |   |
          |
          |
          |
          |
     ========
          ''']

# SET UP VARIABLES
chosen_word = random.choice(list(english_words_lower_alpha_set))

lives = 6

guessed_words = []

word = []

# print(chosen_word)
for letter in chosen_word:
    word.append('_')

end_of_game = False

# GUESSING LOOP
while not end_of_game:
            
    guess = input("Enter a letter: ").lower()
    
    if guess in guessed_words:
        print(f'You have already guessed "{guess}". Guess again.')
        
    guessed_words.append(guess)
    print(f'Guessed Words: {set(guessed_words)}')
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
                
        if letter == guess:
            word[position] = letter
            
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print('You lose!')
            print(f'The word was: {chosen_word}')
        
    print(stages[lives])
    print(word)
    
    
    if "_" not in word:
        end_of_game = True
        print("You Win!")
        