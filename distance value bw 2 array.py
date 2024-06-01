n = int(input("Enter first array size: \n"))
m = int(input("Enter the second array size: \n "))
d = int(input("Enter distance value:\n"))
n_array = []
m_array = []
count = 0

for i in range(n):
    val = int(input("Enter first array Elements:\n"))
    n_array += [val]

for i in range(m):
    val = int(input("Enter second array Elements:\n"))
    m_array += [val]

for i in range(n):
    for j in range(m):
        value = n_array[i] - m_array[j]
        if value < 0:
            value *= -1
            if value <= d:
                count += 1

print(count)

