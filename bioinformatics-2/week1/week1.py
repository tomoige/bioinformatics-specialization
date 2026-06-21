def kmer_compositions(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return kmers

text = "TATGGGGTGC"
k = 3
print(kmer_compositions(text, k))

with open("week1-1.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0])
    text = lines[1]
    res = kmer_compositions(text, k)
    print(" ".join(res))
    with open("week1-1-output.txt", "x") as f2:
        f2.write(" ".join(res))