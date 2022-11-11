'''
Programming Task #2
Create a game where the user must correctly guess a randomly generated integer between 1 and 100.
The user should be notified whether their guess was “lower” or “higher” than the target number.
Note that you will need to use the random library’s randint function.
Remember:
- Use functions to group code
- Try to have functions that only do one “thing” (e.g. print a message, validate user input, check what message to display)
- Check for invalid inputs, notifying the user and re-prompting for a valid input
'''

# Import randint the random library.
from random import randint

def guess_number():
    '''This function will ask a user to guess a number.'''
    user_input = input('Please enter your guess number: ')
    return user_input

def input_validation(input_value):
    '''This function will check whether the value of input would be valid or not.
    If the input is invalid, it will return True.'''
    if input_value == '':  # The input must not be empty.
        print('Your input must not be empty.')
        return True
    elif input_value.isnumeric() is False:  # The input must be a number.
        print('Your input must be an integer.')
        return True
    else:
        return False

def check_value(guessNumber, targetNumber):
    '''This function will check whether the value of input would be greater or lower than the target number.
    If the guess number is not correct, it will return True and a message to inform the user.'''
    if int(guessNumber) < int(targetNumber):  # Use 'int' function for converting a string to an integer.
        print('Your number is lower than the target.')
        return True
    elif int(guessNumber) > int(targetNumber):  # Use 'int' function for converting a string to an integer.
        print('Your number is higher than the target.')
        return True
    return False

def message_forwinner():
    '''This function will print a congratulation message to a user.'''
    print('Congratulations! Your guess is correct.')

def main():
    '''This function will call all function related to the game.'''
    target_num = randint(1,100)  # Set a target number by using the 'randint' function.
    guess_num = guess_number()  # Set a guess number to store an input from a user.

    # When the user's input is not valid, keep asking for a new one.
    while input_validation(guess_num) is True:
        guess_num = guess_number()

    # If the guess number is not equal to the target number, keep asking for a new one.
    while check_value(guess_num, target_num) is True:
        guess_num = guess_number()
        # When the user's input is not valid, keep asking for a new one.
        while input_validation(guess_num) is True:
            guess_num = guess_number()

    # If the user got the correct answer, print a congratulation message.
    message_forwinner()

# Execute the main function.
main()
