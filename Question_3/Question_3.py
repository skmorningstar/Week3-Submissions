q=int(input())
flag=0
for i in range(q):
    str_1=input()
    str_2=input()
    if len(str_1)==len(str_2):
        count=(ord(str_2[0])-ord(str_1[0]))
        for j in range (len(str_1)):
            if abs(ord(str_2[j])-ord(str_1[j]))!=abs(count) and abs(ord(str_2[j])-ord(str_1[j]))!=26-abs(count):
                flag=-1
                break
            else:
                flag=1
    else:
      flag=-1
    
    
    
    if flag==1:
        if count>=0:
           print(count)
        else:
            print(26-abs(count))
    elif flag==-1:
        print(-1)
   