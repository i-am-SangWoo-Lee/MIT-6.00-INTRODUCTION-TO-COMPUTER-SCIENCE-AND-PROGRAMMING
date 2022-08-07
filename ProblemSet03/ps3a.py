"""
Name : SangWoo Lee
Data : 2022.08.07
Email : i.am.sangwoo.lee@gmail.com
"""
# print("atgacatgcacaagtatgcat".find("ggcc")) 
# # don't need to import 'string' as pdf said.

def countSubStringMatch(target:str,key:str):
    """
    Take two arguments 'target'(string) and 'key'(string).\n
    Returns the counts of instances of the key in target string in Non-recursive way.
    """
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
    """
    Takes two string arguments 'target' and 'key'.\n
    Returns the counts of instances of the key in target string in recursive way.
    """
    ans = 0 
    if len(target) == 1 and target == key:
        return 1 
    for i,w in enumerate(target):
        if key[0] == w:
            ans += countSubStringMatchRecursive(target[i+1:i+len(key)], key[1:])
    return ans

# def Test():
#     targets = ['abcdbcdegdgbcdezebcde', 'aaabbbcccdddabcdcba', 'f24dv3dvs23154322ffv23f2', 'sangiscodingnowforgettingjob']
#     keys = ['bcd', 'ab', '23', 'ng']
#     for target, key in zip(targets, keys):
#         print(f"target is '{target}', key is '{key}'")
#         print(f"countSubStrinMatch is '{countSubStringMatch(target, key)}'")
#         print(f"countSubStrinMatchRecursive is '{countSubStringMatchRecursive(target, key)}'")
#         input()
# Test()