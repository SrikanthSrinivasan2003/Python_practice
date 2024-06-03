def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return list(anagrams.values())


size = int(input("Enter Array Size\n"))
strs = []
for _ in range(size):
    string = input("Enter the string\n")
    strs.append(string)
print(group_anagrams(strs))
