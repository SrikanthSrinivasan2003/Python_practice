#Counting the numbers which is having unit digit and hundredth digit as equal from m to n
m = int(input())
n = int(input())
count = 0
for i in range(m,n+1):
    val = str(i)
    length = len(val)
    if val[0] == val[length-1]:
        count += 1
print(count)
