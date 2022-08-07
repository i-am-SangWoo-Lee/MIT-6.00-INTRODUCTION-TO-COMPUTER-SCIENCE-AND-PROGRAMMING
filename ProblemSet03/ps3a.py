import enum
from string import *

def countSubStringMatch(target:str,key:str):
    ans = 0 
    cnt = 0
    for i, w in enumerate(target):
        if w == key[cnt]:
            cnt += 1
            if cnt == len(key):
                ans += 1
                cnt = 0
        else: cnt = 0
    if ans == 0:
        return -1
    else: return ans

def countSubStringMatchRecursive (target:str, key:str):
    ans = 0 
    if len(target) == 1 and target == key:
        return 1 
    for i,w in enumerate(target):
        if key[0] == w:
            ans += countSubStringMatchRecursive(target[i+1:i+len(key)], key[1:])
    return ans

def Test():
    print("target is 'abcdbcdegdgbcdezebcde', key is 'bcd'")
    print("countSubStrinMatch is ", end="")
    print(countSubStringMatch("abcdbcdegdgbcdezebcde", "bcd"))
    print("countSubStrinMatchRecursive is ", end="")
    print(countSubStringMatchRecursive("abcdbcdegdgbcdezebcde", "bcd"))
    input()
    print("target is 'aaabbbcccdddabcdcba', key is 'ab'")
    print("countSubStrinMatch is ", end="")
    print(countSubStringMatch("aaabbbcccdddabcdcba", "ab"))
    print("countSubStrinMatchRecursive is ", end="")
    print(countSubStringMatchRecursive("aaabbbcccdddabcdcba", "ab"))
    input()
    print("target is 'f24dv3dvs23154322ffv23f2', key is '23'")
    print("countSubStrinMatch is ", end="")
    print(countSubStringMatch("f24dv3dvs23154322ffv23f2", "23"))
    print("countSubStrinMatchRecursive is ", end="")
    print(countSubStringMatchRecursive("f24dv3dvs23154322ffv23f2", "23"))
    input()
    print("target is 'sangiscodingnowforgettingjob', key is 'ng'")
    print("countSubStrinMatch is ", end="")
    print(countSubStringMatch("sangiscodingnowforgettingjob", "ng"))
    print("countSubStrinMatchRecursive is ", end="")
    print(countSubStringMatchRecursive("sangiscodingnowforgettingjob", "ng"))

Test()