def convert_str_to_num(num_list):
    new = []
    for char in num_list:
        new += [int(char)]
    return new


n = input("Enter the numbers\n").split()
result = convert_str_to_num(n)
first_part = ""
second_part = ""
for i in result:
    if i == 0:
        second_part += "0 "
    else:
        first_part += str(i) + " "
result_array = first_part + second_part
print(result_array)

