#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!') # Displays Greetings! in the first line of the terminal 
colors = ['red','orange','yellow','green','blue','violet','purple'] # This line shows the different color options the user has to answe with 
play_again = '' # This looks like a space will start the game over again 
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'): # When complete these lines will ask if you would like to play again, "n" and "no" seem to be the only answers 
    match_color = random.choice(colors) # This could possibly mean that the answer will be randomly generated using one of the several colors above
    count = 0 # This line looks like it shows your count before you input your first answer, being 0
    color = '' # No colors entered at this point 
    while (color != match_color): # This line sets up all possible answers 
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip() # This strips away unecessary spaces and allows the answer to be in lower case 
        count += 1 # One color has been entered at this point 
        if (color == match_color): # If the answer is one of the colors listed above you will recieve a "Correct"
            print('Correct!') # This line shows the player has answered correctly 
        else: # If you don't use an appropriate answer you will recieve a "Sorry, try again. You have guessed {guesses} times.""
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #After answering this line will display the amount of guesses you have used
    print('\nYou guessed it in {0} tries!'.format(count)) # This line displays how many guesses it took the user beforea answering correctly 
    if (count < best_count): # This line prompts the best guess line 
        print('This was your best guess so far!') # this line displays the players best score 
        best_count = count # This line looks like it prompts the next line asking if you would like to play again 
    play_again = input("\nWould you like to play again? ").lower().strip() # This line asks the player if they would like to play again 
print('Thanks for playing!') # This line thanks the player for playing!