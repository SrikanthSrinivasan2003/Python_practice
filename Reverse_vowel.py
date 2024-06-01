n = input("Enter the input\n")
arr = []
new_word = ""
vowel = "aeiou"
for i in n:
    if i in vowel:
        arr += [i]
reverse = arr[::-1]
val = 0
for i in n:
    if i in vowel:
        new_word += reverse[val]
        val += 1
    else:
        new_word += i
print(new_word)
