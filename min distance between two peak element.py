maximum_index_arr = []

def str_to_int(nums):
    new = []
    for i in nums:
        new += [int(i)]
    return new

def max_index(first_index, second_index, list_a):
    if first_index > second_index:
        val_index = list_a.index(first_index)
        maximum_index_arr.append(val_index)
    return

def max_index2(first_index, second_index, list_1):
    if second_index > first_index:
        val_index = list_1.index(first_index)
        maximum_index_arr.append(val_index)
    return


def max_index1(start, mid, end, list_1):
    if mid > start and mid > end:
        val_index = list_1.index(mid)
        maximum_index_arr.append(val_index)
    return

num_list = input("Enter the numbers\n").split()
num_list = str_to_int(num_list)
length = len(num_list)

for i in range(length):
    if i == 0:
        max_index(num_list[i], num_list[i + 1],num_list)
    elif i == length - 1:
        max_index2(num_list[i - 1], num_list[length - 1],num_list)
    else:
        max_index1(num_list[i - 1], num_list[i], num_list[i + 1],num_list)

minimum_distance = 999999
for i in range(len(maximum_index_arr)-1):
    dist = maximum_index_arr[i] - maximum_index_arr[i+1]
    if dist < 0:
        dist *= -1
    if dist < minimum_distance:
        minimum_distance = dist
if len(maximum_index_arr) < 2:
    print(-1)
else:
    print(minimum_distance)
