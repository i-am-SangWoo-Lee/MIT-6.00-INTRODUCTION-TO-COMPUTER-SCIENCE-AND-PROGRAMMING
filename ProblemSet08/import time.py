from cmath import log10
import time

a = 7**234
start = time.time()
print(len(str(a)))
end = time.time()
dur1 = end - start
start = time.time()
print((log10(a)))
end = time.time()
dur2 = end - start
print(dur1 > dur2)