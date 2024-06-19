size = input().split()
N = int(size[0])
M = int(size[1])
count = 1
for line in range(N):
    if line < N//2:
        print((".|."*count).center(M, "-"))
        count += 2

    elif line == N//2:
        print("WELCOME".center(M, "-"))
        count -= 2
    else:
        print((".|."*count).center(M, "-"))
        count -= 2
