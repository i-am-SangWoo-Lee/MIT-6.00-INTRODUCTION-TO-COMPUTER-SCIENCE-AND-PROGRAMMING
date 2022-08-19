import time

numCalls = 0
def fastFib(n:int, memo:dict) -> int:
    global numCalls
    numCalls += 1
    # print(f"n is {n}, and type of n is {type(n)}")
    if not n in memo:
        memo[n] = fastFib(n-1, memo) + fastFib(n-2, memo)
    return memo[n]

def fib(n:int) -> int:
    memo = {0:0, 1:1}
    return fastFib(n, memo)

def main():
    start = time.time()
    num = int(input("Fib of : "))
    print(fib(num))
    print(f"number of calls: {numCalls}")
    end = time.time()
    print(f"time spent : {(end - start):.2f}")


if __name__ == '__main__':
    main()