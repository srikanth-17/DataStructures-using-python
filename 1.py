'''l=[int(i) for i in input().split()]
print(l)

def square(x):
    return x%2

l=[1,2,3,4,5]
r=map(square,l)
a=list(r)
print(a)
print(a.count(1))
'''

l=[i for i in input().split()]
print(f"my name is {l[0]}")
print(f"my age is {l[1]}")