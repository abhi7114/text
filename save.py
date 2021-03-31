lst=list()
even=[]
ans=0
while True:
    num=int(input())
    if num<0:
        break
    else:
        lst.append(num)
i=0
while i in range(len(lst)):
    if lst[i]%2==0:
        even.append(lst[i])
    else:
        if len(even)>=3:
           ans+=1
        even=[]
    i+=1
if lst[i-1]%2==0:
    if len(even)<=3:
        ans+=1
print(ans)