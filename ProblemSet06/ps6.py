# 6.00 Problem Set 6
#
# The 6.00 Word Game
#

from itertools import permutations
import random
from re import A
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
MAX_TIME = 10

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
        print("  ", len(wordlist), "words loaded.")
        return wordlist

def get_frequency_dict(sequence:list) -> dict:
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

def get_word_score(word:str, n:int) -> int:
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
    score = 0
    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
    if len(word) == n:
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
             print(letter,end=', ')              # print(all on the same line
    print()                             # print an empty line

#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n:int) -> dict:
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
    num_vowels = n // 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def update_hand(hand:dict, word:str) -> dict:
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    freq = get_frequency_dict(word)
    newhand = {}
    for char in hand:
        newhand[char] = hand[char]-freq.get(char,0)
    return newhand
    #return dict( ( c, hand[c] - freq.get(c,0) ) for c in hand )
        

def is_valid_word(word:str, hand:dict, word_list:list) -> str:
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
    
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    freq = get_frequency_dict(word)
    for letter in word:
        if freq[letter] > hand.get(letter, 0):
            return False
    return word in word_list

# def return_permuation(hand:list, li:list) -> list:
#     for i in range(len(hand)):
        


def dict2list(hand:dict) -> list:
    li = []
    tmp = hand.copy()
    print(hand)
    for key, val in tmp.items():
        if val > 0:
            for _ in range(val):
                li.append(key)
    return li

def return_max_key(dic:dict) -> str:
    # print(f"dic is {dic}")
    key = list(dic.keys()) 
    val = list(dic.values())
    # print(f"key is {key}")
    # print(f"val is {val}")
    res = key[val.index(max(val))] 
    return res

def pick_best_word(hand:dict, points_dict:dict) -> str:
    """
    Return the highest scoring word from points_dict that can be made with the given hand.
    
    Return '.' if no words can be made with the given hand.
    """
    liHand = dict2list(hand)
    # print(f"liHand is {liHand}")
    per = []
    for i in range(1, len(liHand)):
        per += permutations(liHand, i)
    li = []
    for i in range(len(per)):
        li.append(''.join(per[i]))
    li = list(set(li))
    # print(f"length is {len(li)}")
    # print(f"per is {li}")
    dic = {}
    done = False
    for word in li:
        if ''.join(word) in points_dict:
            # print("!!!")
            # print(f"word is {word}")
            # print(f"word val is {points_dict[word]}")
            dic[word] = points_dict[word]
            done = True
    if done is False:
        return '.'
    # print(f"dic1 is {dic}")
    res = return_max_key(dic)
    # print(f"res is {res}")
    return res

def get_words_to_points(word_list:list) -> dict:
    """
    Return a dict that maps every word in word_list to its point value.
    """
    dic = {}
    for word in word_list:
        dic[word] = get_word_score(word, -1)
    return dic

def play_hand(hand:dict, word_list:list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """    
    total = 0
    done = False
    left_time = MAX_TIME
    initial_handlen = sum(hand.values())
    points_dict = get_words_to_points(word_list)
    while sum(hand.values()) > 0:
        print('Current Hand:',)
        display_hand(hand)
        input()
        start_time = time.time()
        # userWord = input('Enter word, or a . to indicate that you are finished: ') # Replaced by pick_best_word
        best_word = pick_best_word(hand, points_dict)
        end_time = time.time()
        spent_time = end_time - start_time
        div_time = max(1, spent_time) # if spent_time less than one , will divide score with one
        left_time -= spent_time
        print(f"It took {spent_time:.2f} seconds to provide an answer.")
        if left_time >= 0:
            print(f"You have {left_time:.2f} seconds remaining.")
        else:
            print(f"Total time exceeds {-left_time:.2f} seconds. ", end='')
            done = True
        # if userWord == '.' or done:
        if best_word == '.' or done:
             break
        else:
            # isValid = is_valid_word(userWord, hand, word_list)
            isValid = is_valid_word(best_word, hand, word_list)
            if not isValid:
                print('Invalid word, please try again.')
            else:
                # points = get_word_score(userWord, initial_handlen)/div_time
                points = get_word_score(best_word, initial_handlen)/div_time
                total += points
                # print(f'{userWord} earned {points:.2f} points. Total: {total:.2f} points')
                # hand = update_hand(hand, userWord)
                print(f'{best_word} earned {points:.2f} points. Total: {total:.2f} points')
                hand = update_hand(hand, best_word)
    if done:
        print(f"You scored {total:.2f} points.")
    else:
        print(f'Total score: {total:.2f} points.')


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
