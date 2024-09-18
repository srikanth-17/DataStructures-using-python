"""
1 TO N

def f(i,n):
    if i>n:
        return None
    print(i)
    f(i+1,n)
f(10,15)"""

"""
N TO 1

def f(i,n):
    if i<1:
        return None
    print(i)
    f(i-1,n)
f(20,10)"""

"""
SUM OF N NUMBERS
def f(n):
    if n==0:
        return 0
    return n+f(n-1)
print(f(10))
    """
"""
FACTORIAL
def f(n):
    if n==1:
        return 1
    return n*f(n-1)
print(f(5))"""

def rev(l):
    if len(l) == 0:
        return []
    return [l[-1]]+rev(l[:-1])

print(rev([1,2,3,4,5]))
