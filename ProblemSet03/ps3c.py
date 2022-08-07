"""
Name : SangWoo Lee
Data : 2022.08.07
"""
def constrainedMatchPair(firstMatch:tuple, secondMatch:tuple, length:int):
    """
    Takes two tuple arguments and one integer arguments, 'firstMatch', 'secondMatch', 'length'.\n
    Returns index that satisfying\n
    'index of first match(part of key)' + 'length of key' = 'index of second match(part of key)'\n
    this formula in form of tuple.
    """
    ans = []
    if len(firstMatch) == 0:
        return tuple(secondMatch)
    elif len(secondMatch) == 0:
        return tuple(firstMatch)
    else:
        for i in firstMatch:
            for j in secondMatch:
                if int(i) + length + 1 == int(j):
                    ans.append(i)
        return tuple(ans)

