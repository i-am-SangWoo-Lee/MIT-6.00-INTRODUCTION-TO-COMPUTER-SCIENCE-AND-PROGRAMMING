#for i in range(100):
    #print('i',i)
    #print('i%2', i%2)
    #print('(i%2)*2', (i%2)*2)
    #if((i%2)*2 == i):
        #print('even?')
    #print(f"end of {i}th loop")

def exp(a,b):
    if b == 1:
        return a
    if (b%2) == 0:
        return exp(a*a,b/2)
    else: return a*exp(a, b-1)

def test():
    for i in range(2,10):
        for j in range(2,10):
            print("i, j is",i,j," and exp(i,j) is ",exp(i,j))
test()
