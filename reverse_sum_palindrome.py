def reverse_num(number):
    reversed_num = number[::-1]
    reversed_num = int(reversed_num)
    final = int(number) + reversed_num
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
        reverse_num(str(sum_))
initial_input = input("Enter the number\n")
reverse_number = initial_input[::-1]
result = int(initial_input) + int(reverse_number)
is_palindrome(result)
