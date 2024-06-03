def max_distance(arr):
    indices = {}
    for i, value in enumerate(arr):
        if value in indices:
            indices[value][1] = i
        else:
            indices[value] = [i, i]
    max_dist = 0
    for first, last in indices.values():
        max_dist = max(max_dist, last - first)
    return max_dist
arr_size = int(input("Enter Array Size\n"))
arr = []
for i in range(arr_size):
    val = int(input("Enter value: "))
    arr.append(val)
print(max_distance(arr))
