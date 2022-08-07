from email.policy import default
from struct import pack


def p01(start:int, end:int, a = 6, b = 9, c = 20):
    """
    Solution for McNugget Problem.\n
    Get two integers 'start', 'end'
    'start' and 'end' is making list range of (start to end),
    this list will be used as 'n' in formula.\n
    This function works from 46. Under 46 doesn't have five serial possible 'n' 
    Check all the possible combinations from the formula\n
    'ax + by + cz = n'\n
    And returns possible combinations in the form of
    [x, y, z, n] and so on.
    """
    assert isinstance(start, int), "start point must be integer"
    assert isinstance(end, int), "end point must be integer"
    assert start >= 0, "start value must be same or greater than 0" 
    assert end >= 1, "end value must be same or greater than 1"
    assert start<end, "starting point should be smaller than ending point"
    # 6x + 9y + 20z = n
    ans = []
    nuggets = range(start, end+1)
    # change n from 50 to 55
    for num in nuggets:
        # change z from 0 to z <= n/20
        for z in range(num//c + 1):
            # change y from 0 to y <= (n-20*z)/9
            for y in range((num-c*z)//b + 1):
                # if (num - 20*z - 9*y)%6 == 0 there is answer
                if (num - c*z - b*y)%a == 0:
                        ans.append([(num - c*z - b*y)//a,y,z,num])
    return ans

def p01Test(start:int, end:int):
    """
    testing p01 function in steps of 5 from 'start' to 'end'.
    Those value should be positive integer and 'end' should be greater than 'start'
    Print boolean value which tells every 5 steps has possible combinations.
    This does not return anything.
    """
    for i in range(start, end+1, 5):
        isEmpty = len(p01(i, i+5)) > 0
        print(f"The guess from {i} to {i+5} having possible combination is {isEmpty}")

def p03(num:int, package:tuple={6, 9, 20}):
    li = []
    x, y, z = package
    for i in p01(0,num, x, y, z)[:]:
        li.append(i[-1])
    diff = set(range(num+1)).difference(set(li)) 
    #print(f"Largest number of McNuggets that cannot be bought in exact quantity: {max(diff)}")
    return max(diff)
p03(200)
print(p01(1,200, 23,25,27))