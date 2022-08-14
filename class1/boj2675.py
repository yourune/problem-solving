t=int(input())
lst=[]
for i in range(t):
    r,s=input().split()
    r=int(r)
    l=len(s)
    p=''
    for j in range(l):
        p=p+s[j]*r
    lst.append(p)
for j in range(t):
    print(lst[j])