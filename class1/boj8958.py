n=int(input())
for i in range(n):
    score=input()
    length=len(score)
    cnt=0
    sum=0
    for j in range(length):
        if score[j]=='O':
            cnt=cnt+1

        if score[j]=='X':
            cnt=0
        sum=sum+cnt
    print(sum)

