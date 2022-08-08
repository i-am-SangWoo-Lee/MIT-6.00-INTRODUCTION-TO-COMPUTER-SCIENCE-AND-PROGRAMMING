# Problem Set 4
# Name: SangWoo Lee
# Collaborators: Alone
# Time: 2022.08.08
# Email : i.am.sangwoo.lee@gmail.com

#
# Problem 1
#


  
def nestEggFixed(salary:int, save:int, growthRate:int, years:int):
    """
    Helps to predict your retirement plan.\n
    Args:
      salary (int): the amount of money you make each year.\n
      save (int): the percent of your salary to save in the investment account each year (an integer between 0 and 100).\n
      growthRate (int): the annual percent increasein your investment account (an integer between 0 and 100).\n
      years (int): the number of years to work.\n
      return: a list whose values are the size of your retirement account at the end of each year.
    """
    # alpha = salary * (save * 0.01)
    # beta = 1 + (0.01 * growthRate)
    # li[-1] = alpha
    # li[-2] = li[-1] * beta + alpha
    # li[n+1] = li[n] * beta + alpha
    alpha = salary * (save * 0.01)
    beta = 1 + (0.01 * growthRate)
    li = [alpha]
    for i in range(1, years):
        li.append(li[i-1]*beta + alpha)
    # reverse list
    return li


def testNestEggFixed():
    """
    Test NestEggFixed
    Initial test case is
    sal = 10000
    save = 10
    growthRate = 15
    years = 5
    """
    salary     = 10000
    save       = 10
    growthRate = 15
    years = 5
    li = [
        [10000, 10, 15, 5],
        [12000, 15, 10, 5],
        [10000, 15, 15, 5]
        ]
    #savingsRecord = nestEggFixed(salary, save, growthRate, years)
    #print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    for i in li:
        savingsRecord = nestEggFixed(i[0], i[1], i[2], i[3])
        print(savingsRecord)

#testNestEggFixed()

#
# Problem 2
#

def nestEggVariable(salary:int, save:int, growthRates:list):
    # TODO: Your code here.
    """
    Args:
        salary (int): the amount of money you make each year.
        save (int): the percent of your salary to save in the investment account each(an integer between 0 and 100).
        growthRates (list): a list of the annual percent increases in your investment account (integers between 0 and 100).
        Return: a list of your retirement account value at the end of each year.
    """
    alpha = salary * (save * 0.01)
    li = [alpha] 
    for i, growthRate in enumerate(growthRates[1:]):
        beta = 1 + (0.01 * growthRate)
        li.append(li[i] * beta + alpha)
    return li

def testNestEggVariable():
    """
    test nestEggVariable
    Initial test case is
    salary = 10000
    save = 10
    growthRates = [3, 4, 5, 0, 3]
    """
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    #print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.
    li = [
        [10000, 10, [3, 4, 5, 0, 3]],
        [10000, 20, [2, -50, -10, -50, -70]]
    ]
    for j in li:
        savingsRecord = nestEggVariable(j[0], j[1], j[2])
        print(savingsRecord)

# testNestEggVariable()
#
# Problem 3
#

def postRetirement(savings:int, growthRates:list, expenses:int):
    """
    Args:
        savings (int): the initial amount of money in your savings account.
        growthRates (list): a list of the annual percent increases in your investment account (an integer between 0 and 100).
        expenses (int): the amount of money you plan to spend each year during retirement.
        return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    li = [savings * (1 + (0.01*growthRates[0])) - expenses] 
    for i, growthRate in enumerate(growthRates[1:]):
        beta = 1 + (0.01 * growthRate)
        li.append(li[i] * beta - expenses)
    return li

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    #print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    li = [
        [100000, [10, 5, 0, 5, 1], 30000],
        [100000, [1, 2, 3, 4, 5], 30000],
        [100000, [1, -1, 1, -1, 1], 30000]
    ]
    for i in li:
        print(postRetirement(i[0], i[1], i[2]))
#testPostRetirement()
#
# Problem 4
#

def findMaxExpenses(
    salary:int, save:int, preRetireGrowthRates:list, postRetireGrowthRates:list, epsilon:float):
    """
    Args:
        salary (int): the amount of money you make each year.
        save (int): the percent of your salary to save in the investment account each year (an integer between 0 and 100).
        preRetireGrowthRates (list): a list of annual growth percentages on investments while you are still working.
        postRetireGrowthRates (list): a list of annual growth percentages on investments while you are retired.
        epsilon (float): an upper bound on the absolute value of the amount remaining in the investment fund at the end of retirement.
        return : 
    """
    # TODO: Your code here.
    expense = 1000 
    pre = nestEggVariable(salary, save, preRetireGrowthRates)
    post = postRetirement(pre[-1], postRetireGrowthRates, expense)
    high = pre[-1]
    low = 0
    cnt = 0
    while abs(post[-1]) > epsilon:
        mid = (high+low) * 0.5
        expense = mid
        post = postRetirement(pre[-1], postRetireGrowthRates, expense)
        if post[-1] > epsilon:
            low = mid
        elif post[-1] < -epsilon:
            high = mid
        cnt += 1
        print(f"expense is {expense}, pre[-1] is {pre[-1]} post[-1] is {post[-1]}\nthis is {cnt} step\n")
    return (expense) 

def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986

    # TODO: Add more test cases here.

testFindMaxExpenses()