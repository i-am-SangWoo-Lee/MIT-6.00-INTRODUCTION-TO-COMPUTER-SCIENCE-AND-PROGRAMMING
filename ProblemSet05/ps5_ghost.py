# Problem Set 5: Ghost
# Name: SangWoo Lee
# Collaborators: Alone
# Time: 2022.08.08
# Email : i.am.sangwoo.lee@gmail.com

import random
from re import T

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open(WORDLIST_FILENAME) as inFile:
    # wordlist: list of strings
        wordlist = []
        for line in inFile:
            wordlist.append(line.strip().lower())
        print(f"'{len(wordlist)}', words loaded.")
        return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


# (end of helper code)
# -----------------------------------

# Actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program.
wordlist = load_words()

# TO DO: your code begins here!
def getWord():
    """
    check the user input a lowercase english letter. And return it. 
    Returns:
        str: return only one lowercase english letter
    """
    while True:
        char = str(input())
        if len(char) == 1 and (97 <= ord(char) <= 122):
            return char
        elif len(char) > 1:
            print("Only one character is allowed.")
        elif ord(char)<97 or ord(char)>122:
            print("Only lowercase english alphabet is allowed.")
        else:
            print("invalid input. somethings wrong.")


def isValid(word:list, wordList:list, num:int):
    """
    Check word is ok to win.

    Args:
        word (list): 
        wordList (list): 

    Returns:
        bool: whether word is in list or not. and num should be over three.
    """
    cnt = 0
    isInList = False
    while cnt < len(wordList):
        if wordList[cnt] == word and num > 3:
            # print(f"wordlist[{cnt}] is '{wordlist[cnt]}'. word is '{word}'")
            isInList = True
        cnt += 1
    return isInList

def isPossible(word:list, wordList:list):
    """
    Check whether word is subset of wordList.

    Args:
        word (list): 
        wordList (list): 
    Returns:
        bool: whether word subset or not.
    """
    length = len(word)
    for w in wordlist:
        if length < len(w):
            cnt = 0
            for i, c in enumerate(word):
                if w[i] == c:
                    cnt += 1
            if cnt == length:
                return True
    return False


def whichPlayerTurn(cnt:int):
    """
    Check which players turn

    Args:
        cnt (int): counter for while loop to check the turn

    Returns:
        int: '1' for player1, '2' for player2
    """
    if cnt%2 == 0:
        print("Turn for player1 to input a character.")
        return 1
    else:
        print("Turn for player2 to input a character.")
        return 2

def game_start(wordlist:list):
    isOver = False
    cnt = 0
    li = []
    while (not isOver):
        playerNumber = whichPlayerTurn(cnt)
        cnt += 1
        li.append(getWord())
        # print(f"li is {li}")
        if isValid(''.join(li), wordlist, cnt) == True:
            print(f"Player{playerNumber} Complte the word '{''.join(li)}'\nWIN!")
            isOver = True
        if isPossible(li, wordlist) == True:
            continue
        else:
            print(f"There is no word begin with '{''.join(li)}' left in word list")
            print(f"Player{playerNumber} Loose!")
            isOver = True
    
def play_game(wordlist:list):
    while True:
        cmd = input('Enter n to play a new game, or e to end game: ')
        if cmd == 'n':
            game_start(wordlist)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")

if __name__ == '__main__':
    play_game(wordlist)