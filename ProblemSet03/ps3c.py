def constrainedMatchPair(firstMatch:tuple, secondMatch:tuple, length:int):
    ans = []
    for i in firstMatch:
        for j in secondMatch:
            if int(i) + length + 1 == int(j):
                ans.append(i)
    return tuple(ans)

