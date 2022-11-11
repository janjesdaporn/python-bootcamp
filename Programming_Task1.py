'''
Programming Task #1
Given a list of digits, determine the integer that it represents.
For example, given the list: [8,3,5,1], your program should output 8351.
Note: You are not allowed to use conversion / casting functions, (i.e., str or int)
'''

# Create a list of digits.
a_list = [8,3,5,1]

# Crate a for loop to print out each item from the list.
for position in range(0, len(a_list)):  # The first position in the list starts with 0.
    print(a_list[position], end='')  # Put an 'end' argument to make the program print without a new line.
