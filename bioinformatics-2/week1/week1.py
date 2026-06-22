def kmer_compositions(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return kmers

text = "TATGGGGTGC"
k = 3
print(kmer_compositions(text, k))

# with open("week1-1.txt") as f:
#     lines = f.read().strip().splitlines()
#     k = int(lines[0])
#     text = lines[1]
#     res = kmer_compositions(text, k)
#     print(" ".join(res))
#     with open("week1-1-output.txt", "x") as f2:
#         f2.write(" ".join(res))

def genome_path(genome):
    string = ""
    for i, genomeslice in enumerate(genome):
        if(i == len(genome) - 1):
            string += genomeslice
        else:
            string += genomeslice[0]
    return string

genome = ["ACCGA", "CCGAA", "CGAAG", "GAAGC", "AAGCT"]
print(genome_path(genome))

with open("week1-2.txt") as f:
    genome = f.read().strip().split(" ")
    print(genome_path(genome))