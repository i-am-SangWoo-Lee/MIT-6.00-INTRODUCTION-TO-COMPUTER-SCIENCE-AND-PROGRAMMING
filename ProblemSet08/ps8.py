# 6.00 Problem Set 8
#
# Intelligent Course Advisor
#
# Name:
# Collaborators:
# Time:
#

from multiprocessing.sharedctypes import Value
from re import M
import time

SUBJECT_FILENAME = "/Users/goaswon/Code/MIT600/ProblemSet08/subjects.txt"
VALUE, WORK = 0, 1

#
# Problem 1: Building A Subject Dictionary
#
def loadSubjects(filename:str) -> dict:
    """
    Returns a dictionary mapping subject name to (value, work), where the name
    is a string and the value and work are integers. The subject information is
    read from the file named by the string filename. Each line of the file
    contains a string of the form "name,value,work".

    returns: dictionary mapping subject name to (value, work)
    """

    # The following sample code reads lines from the specified file and prints
    # each one.
    dic = {}
    with open(filename) as inputFile:    
        for line in inputFile:
            subject, value, work = line.split(sep=',') 
            dic[subject] = (int(value), int(work))
    return dic
    # TODO: Instead of printing each line, modify the above to parse the name,
    # value, and work of each subject and create a dictionary mapping the name
    # to the (value, work).

def printSubjects(subjects:dict):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0,0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    subNames = sorted(subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) +'\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)

def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return  val1 > val2

def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return  work1 < work2

def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is 
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    ratio1 = float(val1) / work1
    ratio2 = float(val2) / work2
    return ratio1 > ratio2 

#
# Problem 2: Subject Selection By Greedy Optimization
#
def greedyAdvisor(subjects:dict, maxWork:int, comparator) -> dict:
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    comparator: function taking two tuples and returning a bool
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...
    dicRes = {}
    workHour = 0
    cmpKey = None
    while maxWork - workHour > 0:
        cmpVal = (0, 10000)
        for key, val in subjects.items():
            if maxWork - (val[WORK] + workHour) >= 0:
                if key not in dicRes.keys():
                    if comparator(val, cmpVal):
                        cmpVal = val
                        cmpKey = key
        dicRes[cmpKey] = subjects[cmpKey]
        workHour += subjects[cmpKey][WORK]
    return dicRes

def greedyTime(comparator):
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    ratio = None
    previous = 0
    for i in range(1, 100):
        start = time.time()
        greedyAdvisor(subjects, i, comparator)
        end = time.time()
        time_spent = end - start
        if previous > 0.00:
            ratio = time_spent / previous
            print(f"At maxwork: {i}, It took {time_spent:.2f} seconds. And ratio is {ratio:.2f}")
        else:
            print(f"At maxwork: {i}, It took {time_spent:.2f} seconds.")
        previous = time_spent 

def bruteForceAdvisor(subjects:dict, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    # print(tupleList)
    bestSubset, bestSubsetValue = \
            bruteForceAdvisorHelper(tupleList, maxWork, 0, None, None, [], 0, 0)
    outputSubjects = {}
    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]
    return outputSubjects

def bruteForceAdvisorHelper(subjects:list, maxWork:int, i:int, bestSubset:list, bestSubsetValue:int,
                            subset:list, subsetValue:int, subsetWork:int):
    # Hit the end of the list.
    if i >= len(subjects):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subjects[i]
        # Try including subjects[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subjects,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue

#
# Problem 3: Subject Selection By Brute Force
#
def bruteForceTime():
    """
    Runs tests on bruteForceAdvisor and measures the time required to compute
    an answer.
    """
    ratio = None
    previous = 0
    for i in range(1, 100):
        start = time.time()
        bruteForceAdvisor(subjects, i)
        end = time.time()
        time_spent = end - start
        if previous > 0.00:
            ratio = time_spent / previous
            print(f"At maxwork: {i}, It took {time_spent:.2f} seconds. And ratio is {ratio:.2f}")
        else:
            print(f"At maxwork: {i}, It took {time_spent:.2f} seconds.")
        previous = time_spent
    # TODO...

# Problem 3 Observations
# ======================
#
# TODO: write here your observations regarding bruteForceTime's performance
# time grows exponentially. growth ratio is 4 ~ 2 at each step.
#
# Problem 4: Subject Selection By Dynamic Programming
#
def dpAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work) that contains a
    set of subjects that provides the maximum value without exceeding maxWork.

    subjects: dictionary mapping subject name to (value, work)
    maxWork: int >= 0
    returns: dictionary mapping subject name to (value, work)
    """
    # TODO...

#
# Problem 5: Performance Comparison
#
def dpTime():
    """
    Runs tests on dpAdvisor and measures the time required to compute an
    answer.
    """
    # TODO...

# Problem 5 Observations
# ======================
#
# TODO: write here your observations regarding dpAdvisor's performance and
# how its performance compares to that of bruteForceAdvisor.

if __name__ == '__main__':
    subjects = loadSubjects(SUBJECT_FILENAME)
    # print(subjects)
    # printSubjects(subjects)
    # print(f"in cmpValue {greedyAdvisor(subjects, 45, cmpValue)}")
    # print(f"in cmpRatio {greedyAdvisor(subjects, 45, cmpRatio)}")
    # print(f"in cmpWork {greedyAdvisor(subjects, 40, cmpWork)}")
    bruteForceTime()
    greedyTime(cmpRatio)