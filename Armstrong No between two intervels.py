m = int(input())
n = int(input())
z=[]
for i in range(m,n+1):
    length=len(str(i))
    sum=0
    temp=i 
    while temp>0:
        digit=temp%10
        sum=sum+digit**length
        temp//=10
    if i==sum:
        print(i,end=' ')
        z.append(i)
if len(z)==0:
    print(-1)
    
