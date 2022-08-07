"""
Name : SangWoo Lee
Data : 2022.08.07
Email : i.am.sangwoo.lee@gmail.com
"""
from ps3b import subStringMatchExact
from ps3_template import subStringMatchOneSub

def subStringMatchExactlyOneSub(target:str, key:str):
    """
    Returns every index that represent string that matching with only one sub keys in form of tuple.
    """
    exact_ans = set(subStringMatchExact(target, key))
    inexact_ans = set(subStringMatchOneSub(key, target))
    ans = inexact_ans.difference(exact_ans)
    return tuple(ans)
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

def test():
    for target in tarli:
        for key in keyli:
            print(subStringMatchExactlyOneSub(target, key))
    
test()