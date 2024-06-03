def isIsomorphic(s, t):
    if len(s) != len(t):
        return False
    s_to_t = {}
    t_chars_used = set()
    for i in range(len(s)):
        if s[i] in s_to_t:
            if s_to_t[s[i]] != t[i]:
                return False
        else:
            if t[i] in t_chars_used:
                return False
            else:
                s_to_t[s[i]] = t[i]
                t_chars_used.add(t[i])
    return True
s1 = input("Enter first String:\n")
s2 = input("Enter second String:\n")
print(isIsomorphic(s1,s2))
