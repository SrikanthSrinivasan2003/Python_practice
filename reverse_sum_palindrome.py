def reverse_num(number):
    reversed_num = str(number)
    reversed_num = reversed_num[::-1]
    reversed_num = int(reversed_num)
    final = number + reversed_num
    is_palindrome(final)


def is_palindrome(num):
    temp = num
    sum_ = 0

    while num > 0:
        val = num % 10
        sum_ = (sum_ * 10) + val
        num = int(num/10)

    if sum_ == temp:
        print(sum_)
    else:
        reverse_num(sum_)


def str_to_int(num_list):
    new_list = []
    for i in num_list:
        new_list.append(int(i))
    return new_list


initial_input = input("Enter the number\n")
reverse_number = initial_input[::-1]
initial_input = int(initial_input)
reverse_number = int(reverse_number)
result = initial_input + reverse_number
is_palindrome(result)
