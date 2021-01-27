Test=int(input())
for i in range (Test):
    n=int(input())
    binary=input()
    binary_list=[]
    new=""
    
    for j in range(0,n):
        new=binary[j:j+n]
        binary_list.append(new)     
    
    str=''
    for k in range(len(binary_list)):
        str+=(binary_list[k])[k]
    print(str)