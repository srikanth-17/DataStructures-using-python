def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
def strongnum(s:str) -> bool:
    c=0
    for i in range(len(s)):
        if int(s[i])==0:
            c+=0
        else:
            c+=fact(int(s[i]))
    if int(s)==c:
        return True
    else:
        return False

l=[]
n=int(input("enter the num"))
i=0
while i<n:
    a=int(input())
    if a<0:
        print("Write again")
        i+=0
    else:
        l.append(str(a))
        i+=1
for x in l:
    if strongnum(x):
        print(int(x),end="  ")
    