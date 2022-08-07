"""
MIT OpenCourseWare
http://ocw.mit.edu
6.00 Introduction to Computer Science and Programming
Fall 2008
For information about citing these materials or our Terms of Use, visit: http://ocw.mit.edu/terms.

A Very Simple Program: Entering and Printing Your Name
The goal of this programming exercise is simply to get you more comfortable with using IDLE,
and to begin using simple elements of Python. Standard elements of a program include the
ability to print out results (using the print operation), the ability to read input from a user at the
console (for example using the raw_input operation), and the ability to store values in a
variable, so that the program can access that value as needed.

Problem 1.
Write a program that does the following in order:
1. Asks the user to enter his/her last name.
2. Asks the user to enter his/her first name.
3. Prints out the user’s first and last names in that order.

An example of an interaction with your program is shown below (the words printed in blue
are from the computer, based on your commands, the words in black are a user’s input –
the colors are simply here to help you distinguish the two components):

Enter your last name:
**Grimson
Enter your first name:
**eric
eric
Grimson
"""

lastname = input("Enter your last name:\n**")
firstname = input("Enter your first name:\n**")
print(f'{firstname}\n{lastname}')