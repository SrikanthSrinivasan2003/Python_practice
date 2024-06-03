def group_anagrams(strs):
    anagrams = {}
    for s in strs:
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(s)
        else:
            anagrams[sorted_str] = [s]
    return list(anagrams.values())


strs = input("Enter the strings with space\n").split()
print(group_anagrams(strs))
