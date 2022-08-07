"""
Name : SangWoo Lee
Data : 2022.08.07
Email : i.am.sangwoo.lee@gmail.com
"""
def subStringMatchExact(target:str, key:str):
    """
    Takes two string arguments 'target', and 'key'.\n
    Returns every index that pointing where the 'key' exactly matching with the 'target'
    """
    ans = []
    cnt = 0
    keyLength = len(key)
    if keyLength == 0:
        return ()
    for i, w in enumerate(target):
        if w == key[cnt]:
            cnt += 1
            if cnt == keyLength:
                ans.append(i-cnt+1)
                cnt = 0
        elif target[i-1] == w:
            if cnt == keyLength:
                ans.append(i-cnt+1)
                cnt = 0
        else: cnt = 0
    if ans == 0:
        return ()
    else: return tuple(ans)


# def testing():
#     targets = ['atgacatgcacaagtatgcat', 'atgaatgcatggatgtaaatgcag']
#     keys = ['a', 'atg', 'atgc', 'atgca']
#     for t in targets:
#         for k in keys:
#             print(f"for target '{t}' and key for '{k}' is ", end="")
#             print(subStringMatchExact(t, k))

# testing()
# print(subStringMatchExact('atgacatgcacaagtatgcat', ''))