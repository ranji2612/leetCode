# sqrt
# https://leetcode.com/problems/sqrtx/

def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x==0:
        return 0
    a = 1
    b = 2
    while b*b<=x:
        a = b
        b*=b
    c = (a+b)/2
    while b-a>1:
        if x-c*c == 0:
            return c
        if x-c*c > 0:
            a=c
        else:
            b=c
        c = (a+b)/2
    return a