from string import *
from ps3b import subStringMatchExact
from ps3c import constrainedMatchPair
# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'
tarli = [target1, target2]

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
keyli = [key10, key11, key12, key13]



### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        # print(f"target is '{target}', \nand breaking key '{key}' into '{key1}', '{key2}'")
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1) # works
        match2 = subStringMatchExact(target,key2) # works
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers += filtered
        # print(f"match1 : '{match1}'")
        # print(f"match2 : '{match2}'")
        # print(f"possible matches for '{key1}', '{key2}' start at '{filtered}'\n\n")
        allAnswers = tuple(set(allAnswers))
    return allAnswers
        
# def test():
#     for target in tarli:
#         for key in keyli:
#             print(f"allAnswers for '{key}' in '{target}'is \n{subStringMatchOneSub(key, target)}")

# test()