def min_distanced(arr):
    element_indices = {}
    min_distance = float('inf')
    for i, element in enumerate(arr):
        if element in element_indices:
            distance = i - element_indices[element]
            min_distance = min(min_distance, distance)
        element_indices[element] = i
    return min_distance if min_distance != float('inf') else -1
array = []
n = int(input("Enter array size:\n"))
for _ in range(n):
    val = int(input("Enter element:\n"))
    array.append(val)
print(min_distanced(array))
