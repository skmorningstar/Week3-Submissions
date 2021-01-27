A=input()
B=input()
if len(A)!=len(B):
    print("NO")
else:
    z=[]
    LA=[ord(i) for i in A]
    LB=[ord(j) for j in B]
    for i in range(len(A)-1,-1,-1):
        z+=[LB[i]-LA[i]]
    k=sorted(z)
    print(z)
    print(k)
    if k==z:
        print("YES")
    else:
        print("NO")
