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
initial_input = input("Enter the number\n")
reverse_number = initial_input[::-1]
initial_input = int(initial_input)
reverse_number = int(reverse_number)
result = initial_input + reverse_number
is_palindrome(result)
