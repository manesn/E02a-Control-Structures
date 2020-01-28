#!/usr/bin/env python3
import sys, random

assert sys.version_info >= (3,7), "This script requires at least Python 3.7"


print('Greetings!') # it's saying hi. Hi!
colors = ['red','orange','yellow','green','blue','violet','purple']
play_again = ''
best_count = sys.maxsize            # the biggest number

while (play_again != 'n' and play_again != 'no'):
    match_color = random.choice(colors)
    count = 0
    color = ''
    while (color != match_color):
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()
        count += 1
        if (color == match_color):
            print('Correct!')                   # Yaaaay
        else:
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))  # boooooo
    
    print('\nYou guessed it in {} tries!'.format(count))

    if (count < best_count):            # If the guess count is better than the previous (best) count...
        print('This was your best guess so far!') # Say you guessed the color in 10 guesses, and this time guessed it in 5... this would be your "new record" of sorts.
        best_count = count  # This new count becomes the new best count.

    play_again = input("\nWould you like to play again (yes or no)? ").lower().strip()

print('Thanks for playing!')