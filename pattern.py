def wordPattern(pattern, s):
    words = s.split()
    if len(pattern) !=  len(words):
        return False

    p2w, w2p = {}, {}
    for p, w in zip(pattern, words):
        if p not in p2w and w not in w2p:
            p2w[p] = w
            w2p[w] = p
        elif p2w.get(p)!= w or w2p.get(w)!= p:
            return False
    return True
pattern = input("Enter the patterns\n")
strings = input("Enter the strings\n")
result = wordPattern(pattern,strings)
print(result)
