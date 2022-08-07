"""
Computing Prime Numbers
A common type of computation is the generate-and-test method, in which one systematically
generates potential solutions to a problem, and then applies a sequence of one or more tests to
determine if the proposed solution is in fact valid. While one could in principle (and under some
circumstances one must) generate potential solutions randomly or according to some probability
distribution, often it is more efficient to devise a systematic method for generating all candidate
solutions.
Problem 1.
Write a program that computes and prints the 1000th prime number.

If you want to check that your code is correctly finding primes, you can find a list of
primes at http://primes.utm.edu/lists/small/1000.txt.
"""
    
def sqrt(num:float, iter:int):
    """
    Get sqrt with Newton Sqrt Method.
    Put number and iteration number.
    """
    n = num
    for i in range(iter):
        n = (n + num/n)/2
    return n



def ps01p01ComputingPrimeNumbers(n):
    """
    just print out 1000th prime number.
    search every number's remainder from 2 to round of square root of itself.
    """
    # check every numbers from 2
    # if the very number is prime, add 1 in count variable
    # if counting variable hits 1000, then exit
    # and print the number
    num = 2
    arr = []
    isEnough = False
    while not isEnough:
        isEnough = len(arr) == n 
        isPrime = True 
        for i in range(2, round(sqrt(num, 10))+1):
            #print(i)
            if num % i == 0:
                isPrime = False
                break
        if isPrime == True:
            arr.append(num)
        num += 1
        #print(arr)
    return arr 


"""
The Product of the Primes
There is a cute result from number theory that states that for sufficiently large n the product of
the primes less than n is less than or equal to e**n and that as n grows, this becomes a tight
bound (that is, the ratio of the product of the primes to e**n gets close to 1 as n grows).
Computing a product of a large number of prime numbers can result in a very large number,
which can potentially cause problems with our computation. (We will be talking about how
computers deal with numbers a bit later in the term.) So we can convert the product of a set of
primes into a sum of the logarithms of the primes by applying logarithms to both parts of this
conjecture. In this case, the conjecture above reduces to the claim that the sum of the
logarithms of all the primes less than n is less than n, and that as n grows, the ratio of this sum
to n gets close to 1.
To compute a logarithm, we can use a built in mathematical functions from Python. To have
access to these functions, you need to get them into your environment, which you can do by
including the
from math import *
statement at the beginning of your file. This will allow you to use the function log in your code,
e.g. log(2) will return the logarithm base e of the number 2.
Problem 2.
Write a program that computes the sum of the logarithms of all the primes from 2 to some
number n, and print out the sum of the logs of the primes, the number n, and the ratio of these
two quantities. Test this for different values of n.
You should be able to make only some small changes to your solution to Problem 1 to solve this
problem as well.
"""

def ps01p2ProductOfPrimes(n):
    assert n>0, "number should be greater than 0, not" + str(n)
    import math
    logarithmicsum = 0
    for i in ps01p01ComputingPrimeNumbers(n-1):
        #print(i)
        logarithmicsum += math.log(i)
    return (logarithmicsum, ps01p01ComputingPrimeNumbers(n-1)[-1]) 

def ps01p2Test():
    for i in range(1, 10000, 1000):
        a, b= ps01p2ProductOfPrimes(i)
        print(f"logarithmic sum is {a}, n is {b}, ratio is {a/b}")


print(f"Answer if problem 1 of problem-set 1 is {ps01p01ComputingPrimeNumbers(1000)[-1]}")
ps01p2Test()