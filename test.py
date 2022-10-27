# #for i in range(100):
#     #print('i',i)
#     #print('i%2', i%2)
#     #print('(i%2)*2', (i%2)*2)
#     #if((i%2)*2 == i):
#         #print('even?')
#     #print(f"end of {i}th loop")

# def exp(a,b):
#     if b == 1:
#         return a
#     if (b%2) == 0:
#         return exp(a*a,b/2)
#     else: return a*exp(a, b-1)

# def test():
#     for i in range(2,10):
#         for j in range(2,10):
#             print(f"i, j is '{i}', '{j}', and {exp(i,j)} is '{exp(i,j)}'")
# test()
class Shape(object):
    def __cmp__(s1, s2):
        return cmp(s1.area(), s2.area())

class Square(Shape):
    def __init__(self, h):
        self.side = float(h)
    def area(self):
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
def f(L):
    if len(L) == 0: return None
    x = L[0]
    print(L[1], L[2])
    # print(x)
    for s in L:
        if s >= x:
            x = s
    return x
s = Square(4)
print(s.area())
L = []
shapes = {0:Circle, 1: Square}
for i in range(10):
    L.append(shapes[i%2](i))
print(L[4])
print(f(L))