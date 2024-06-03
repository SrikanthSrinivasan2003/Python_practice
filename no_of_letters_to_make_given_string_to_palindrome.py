def min_chars_to_add_for_palindrome(s: str) -> int:
    def compute_kmp_table(s):
        n = len(s)
        kmp_table = [0] * n
        j = 0
        i = 1
        while i < n:
            if s[i] == s[j]:
                j += 1
                kmp_table[i] = j
                i += 1
            else:
                if j != 0:
                    j = kmp_table[j - 1]
                else:
                    kmp_table[i] = 0
                    i += 1
        return kmp_table
    rev_s = s[::-1]
    concat = s + '#' + rev_s
    kmp_table = compute_kmp_table(concat)
    longest_prefix_suffix_len = kmp_table[-1]
    min_chars_to_add = len(s) - longest_prefix_suffix_len
    return min_chars_to_add
s = input("Enter the string\n")
print(min_chars_to_add_for_palindrome(s))
