word = input()
N = int(input())
first_part = word[:N]
length = len(word)
second_part_index = length - N 
second_part = word[second_part_index:]
print(first_part != second_part)
