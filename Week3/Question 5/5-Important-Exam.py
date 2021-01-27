n,m=map(int,input().split())
l=[]
for i in range(n):
    x=input()
    l+=[x]
l1=list(map(int,input().split()))
sum1=0
for i in range(m):
    subl=[l[j][i] for j in range(n)]
    d={}
    for k in subl:
        if k not in d:
            d[k]=1
        else:
            d[k]+=1
    l2=sorted(list(d.values()))
    sum1+=l2[len(l2)-1]*l1[i]
print(sum1)
