###
### template of code for Problem 4 of Problem Set 2, Fall 2008
###
"""
bestSoFar = 0     # variable that keeps track of largest number
                  # of McNuggets that cannot be bought in exact quantity
packages = (6,9,20)   # variable that contains package sizes

for n in range(1, 150):   # only search for solutions up to size 150
    ## complete code here to find largest size that cannot be bought
    ## when done, your answer should be bound to bestSoFar
"""
from struct import pack
import ps2a

ps2a.p01
def p04(n, package:tuple={6,9,20}):
    """
    “Given package sizes <x>, <y>, and <z>, the largest number of McNuggets that
cannot be bought in exact quantity is: <n>”
    """
    assert n < 200, "n must be less than 200 bro"
    x,y,z = sorted(list(package))
    ans = ps2a.p03(199, package)
    return print(f"Given package sizes {x}, {y}, and {z}, the largest number of McNuggets that \
cannot be bought in exact quantity is: {ans}")

def p04Test():
    p04(199, {3,5,7})
    input()
    p04(199, {3,5,8})
    input()
    p04(199, {3,5,9})
    input()
    p04(199, {3,5,10})
    input()
    p04(199, {4,5,7})
    input()
    p04(199, {4,6,7})
    input()
    p04(199, {5,7,8})
    input()
    p04(199, {13,15,17})
    input()
    p04(199, {23,25,27})
    input()
    p04(199, {13,14,15})
    input()
    p04(199, {14,15,16})

p04Test()