Q=int(input())
for i in range(Q):
    S=input()
    T=input()
    diff=(ord(T[0])-ord(S[0]))
    if diff<0:
        diff+=26
    for j in range(1,len(S)):
        z=(((ord(S[j])+diff-65))%26)+65
        if z!=ord(T[j]):
            print(-1)
            break
    else:
        print(diff)
