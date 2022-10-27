1.
    1) T

    2) T

    3) F

    4) F

    5) T

    6) F
1. ```python
    def findMedian(L):
    """Finds median of L.
    L: a non-empty list of floats
    Returns:
        If L has an odd number of elements, returns the median
        element of L. For example, if L is the list
        [15.0, 5.3, 18.2], returns 15.0.
        If L has an even number of elements, returns the average
        of the two median elements. For example, if L is the
        list [1.0, 2.0, 3.0, 4.0], returns 2.5.
        If the list is empty, raises a ValueError exception.
    Side effects: none.
    """
        length = len(L)
        L.sort()
        if length%2 == 0:
            return (L[length//2] + L[length//2 -1])/2
        else:
            return L[(length+1)//2 -1]
1.  16\n Circle with radius 4\n 
1.  
    1) 

