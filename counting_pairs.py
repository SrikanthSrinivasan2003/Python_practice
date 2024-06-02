def find_pairs_of_socks(socks):
    # Dictionary to keep count of each type of sock
    sock_counts = {}
    
    # Count each type of sock
    for sock in socks:
        if sock in sock_counts:
            sock_counts[sock] += 1
        else:
            sock_counts[sock] = 1
    
    # Calculate the number of pairs for each type of sock
    pairs = 0
    for count in sock_counts.values():
        pairs += count // 2
    
    return pairs

# input
n = int(input())
socks = []
for i in range(n):
    a = int(input())
    socks.append(a)

print("Number of pairs:", find_pairs_of_socks(socks))
