# 6.00 Problem Set 9
#
# Name: SangWoo Lee
# Collaborators: None
# Time: 2022.08.27

from string import *
# from turtle import shape

class Shape(object):
    def area(self):
        # raise AttributeException("Subclasses should override this method.")
        raise AttributeError("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return float(self.side**2)
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return float(3.14159*(self.radius**2))
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        if isinstance(other, Circle) and isinstance(self, Circle):
            if self.radius == other.radius: return True
            else: return False
        else: return False

#
# Problem 1: Create the Triangle class
#
## TO DO: Implement the `Triangle` class, which also extends `Shape`.
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)

    def area(self):
        return float(self.base * self.height * 0.5)

    def __str__(self):
        return f"Triangle with base {self.base:0.1f} and height {self.height:0.1f}"

    def __eq__(self, other):
        """
        Two triangles are equal if they have the same dimension.
        other: object to check for equality
        """
        if isinstance(self, Triangle) and isinstance(other, Triangle): 
            if self.base*self.height == other.base * other.height: return True
            else: return False
        else: return False


#
# Problem 2: Create the ShapeSet class
## TO DO: Fill in the following code skeleton according to the
##    specifications.

class ShapeSet():
    def __init__(self, ):
        """
        Initialize any needed variables
        """
        self.shapes = [] 

    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        if sh not in self.shapes:
            self.shapes.append(sh)

    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        return iter(self.shapes)

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        return '\n'.join(sh.__str__() for sh in self.shapes)
        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    ## TO DO
    res = [] 
    max_area = max(sh.area() for sh in shapes)
    print(f"max_area:{max_area}")
    for sh in shapes:
        if sh.area() == max_area:
            res.append(sh)
    return tuple(res)


#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    ## TO DO
    ss = ShapeSet()
    with open(filename) as f:
        for l in f: 
            l = l.rstrip().split(',')
            if l[0].lower() == 'circle':
                ss.addShape(Circle(l[1]))
            elif l[0].lower() == 'square':
                ss.addShape(Square(l[1]))
            elif l[0].lower() == 'triangle':
                ss.addShape(Triangle(l[1], l[2]))
    return ss

if __name__ == '__main__':
    ss = readShapesFromFile('shapes.txt')
    findLargest(ss)