def subStringMatchExact(target:str, key:str):
    ans = [] 
    cnt = 0
    keyLength = len(key)
    if keyLength == 0:
        li = [i for i in range(len(target))]
        return tuple(li)
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


def testing():
    targets = ['atgacatgcacaagtatgcat', 'atgaatgcatggatgtaaatgcag']
    keys = ['a', 'atg', 'atgc', 'atgca']
    for t in targets:
        for k in keys:
            print(f"for target '{t}' and key for '{k}' is ", end="")
            print(subStringMatchExact(t, k))

# testing()
print(subStringMatchExact('atgacatgcacaagtatgcat', ''))