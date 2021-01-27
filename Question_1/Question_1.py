str_1=input()
str_2=input()
flag=1
count=abs(ord(str_1[0])-ord(str_2[0]))    
if len(str_1)==len(str_2):
   for j in range(0,len(str_1)):
      if str_1[j]!=str_2[j]:
            if abs(ord(str_1[j])-ord(str_2[j]))<=count:
               flag=1
            else:
               flag=0
               break
   if flag==0:
      print("NO")
   else:
      print("YES")
else:
   print("NO")