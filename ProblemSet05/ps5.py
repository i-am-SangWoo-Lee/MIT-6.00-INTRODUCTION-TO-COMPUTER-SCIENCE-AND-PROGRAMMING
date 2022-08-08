# Problem Set 5: 6.00 Word Game
# Name: SangWoo Lee
# Collaborators: Alone
# Time: 2022.08.08
# Email : i.am.sangwoo.lee@gmail.com

import random
from typing import Union
VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
        print(f"  '{len(wordlist)}', words loaded.")
        return wordlist

def get_frequency_dict(sequence: Union[str, list]):
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

#
# Problem #1: Scoring a word
#
def get_word_score(word:str, n:int):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # TO DO ...
    score = 0
    for char in word:
        score += SCRABBLE_LETTER_VALUES[char]
    if len(word) >= n:
        score += 50
    return score

#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand:dict):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=" ")              # print all on the same line
    print()                             # print an empty line
#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n:int):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = int(n // 3)
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand:dict, word:str):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    newHand = hand.copy() 
    for char in word:
        if newHand.get(char, 0) != 0:
            newHand[char] -= 1
            if newHand[char] == 0:
                newHand.pop(char)
    return newHand

#
# Problem #3: Test word validity
#
def isInList(word:str, word_list:list):
    """
    Check whether the word is in word_list or not.
    Args:
        word (str): 
        word_list (list): 

    Returns:
        bool: if word is in list returns True. else, False
    """
    isInList = False
    cnt = 0
    while cnt < len(word_list):
        if word_list[cnt] == word:
            # print(f"word_list[{cnt}] = {word_list[cnt]}\nword = {word}\n")
            isInList = True
        cnt += 1    
    return isInList

def isInHand(word:str, hand:dict, word_list:list):
    """
    Check wheter the word is subset of hand or not.
    Args:
        word (str): 
        hand (dict): 
        word_list (list): 

    Returns:
        bool: if word is subset of hand returns True. else, False
    """
    # make word to dictionary to compare with hand
    # 👇 my stupid code. there was same function named 'get_frequency_dict'
    # for char in word:
    #     cnt = 0
    #     for i in word:
    #         if i == char:
    #             cnt += 1
    #     if new_word.get(char) == None:
    #         new_word[char] = cnt 
    # 👆 I used double nested loop💩    
    isInHand = False
    new_word = get_frequency_dict(word)
    # compare word to hand
    vartocheck = 0
    for char, num in new_word.items():
        # print(f"char is {char} num is {num}\n hand.get({char},0) = {hand.get(char,0)}")
        if hand.get(char, 0) >= num:
            vartocheck += 1
    if vartocheck == len(new_word):
        isInHand = True    
    # print(f"word : {word}\nnew_word : {new_word}\nhand : {hand}")
    # print(f"is in hand? : {isInHand}\nis in list? : {isInList}")
    return isInHand

def is_valid_word(word:str, hand:dict, word_list:list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # TO DO ...
    boolInHand = False
    boolInList = False
    # check word is in list
    boolInList = isInList(word, word_list)
    boolInHand = isInHand(word, word_list)
    return (boolInHand and boolInList)
#
# Problem #4: Playing a hand
#
def play_hand(hand:dict, word_list:list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand 
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...
    totalScore = 0
    cnt = 1
    newhand = hand.copy()
    while len(newhand) > 0:
        print("Current Hand: ", end="")
        display_hand(newhand)
        x = input("Enter word, or a . to indicate that you are finished: ")
        if x == '.':
            print(f"Total score: {totalScore}")
            break
        if is_valid_word(x, hand, word_list):
            score = get_word_score(x, len(hand))
            totalScore += score
            print(f"him earned {score} points. Total: {totalScore} points")
            newhand = update_hand(newhand, x)
        else: print("Invalid word, please try again.")
        cnt += 1

x = {'a':1, 's':1 ,'t':2, 'w':1, 'f':1, 'o':1}
y = {'a':1, "c":1, "i":1, "h":1, "m":2, "z":1}
# play_hand(x, load_words())

#
# Problem #5: Playing a game
# Make sure you understand how this code works!
# 
def play_game(word_list:list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """
    # TO DO ...
    
    # uncomment the following block of code once you've completed Problem #4
    hand = deal_hand(HAND_SIZE) # random init
    while True:
       cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
       if cmd == 'n':
           hand = deal_hand(HAND_SIZE)
           play_hand(hand.copy(), word_list)
           print()
       elif cmd == 'r':
           play_hand(hand.copy(), word_list)
           print()
       elif cmd == 'e':
           break
       else:
           print("Invalid command.")

#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

