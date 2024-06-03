def min_distance(arr):
    indices = {}
    for i, value in enumerate(arr):
        if value in indices:
            indices[value][1] = i
        else:
            indices[value] = [i, i]
    min_dist = 99999999
    for first, last in indices.values():
        result = first - last == 0
        if not result:
            min_dist = min(min_dist, last - first)
    return min_dist
arr_size = int(input("Enter Array Size\n"))
arr = []
for _ in range(arr_size):
    val = int(input("Enter value: "))
    arr.append(val)
print(min_distance(arr))
