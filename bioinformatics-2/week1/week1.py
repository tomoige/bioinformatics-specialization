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

def prefix(string):
    return string[:len(string)-1]

def suffix(string):
    return string[1:]

def adjacency_list(kmers):
    adjacency_list = {}
    for i, kmer in enumerate(kmers):
        suffix_ = suffix(kmer)
        for i2, second_kmer in enumerate(kmers):
            if i == i2:
                continue
            prefix_ = prefix(second_kmer)
            if suffix_ == prefix_:
                if kmer in adjacency_list:
                    adjacency_list[kmer].append(second_kmer)
                else:
                    adjacency_list[kmer] = [second_kmer]
    return adjacency_list

kmers = ["ATGCG", "GCATG", "CATGC", "AGGCA", "GGCAT", "GGCAC"]

# for key,value in adjacency_list(kmers).items():
#     print(key, ":", " ".join(value))

# with open("week1-3.txt") as f:
#     kmers = f.read().strip().split(" ")
#     with open("week1-3-output.txt", "x") as f2:
#         for key,value in adjacency_list(kmers).items():
#             f2.write(key + " : " + " ".join(value).strip() + "\n")
        
k = 4
text = "AAGATTCTCTAAGA"

def get_kmers(text, k):
    kmers = []
    for i in range(len(text) - k + 1):
        kmers.append(text[i:i+k])
    return kmers

def adjacency_list_debruijn(kmers):
    adjacency_list = {}
    for kmer in kmers:
        prefix_ = prefix(kmer)
        suffix_ = suffix(kmer)
        if prefix_ in adjacency_list:#
            adjacency_list[prefix_].append(suffix_)
        else:
            adjacency_list[prefix_] = [suffix_]
    return adjacency_list


# kmers = get_kmers(text, 4)
# res = adjacency_list_debruijn(kmers)
# print(kmers)
# for key, value in res.items():
#     print(key + " : " + str(value))

# with open("week1-4.txt") as f:
#     lines = f.read().strip().splitlines()
#     k = int(lines[0])
#     text = lines[1]
#     kmers = get_kmers(text, k)
#     res = adjacency_list_debruijn(kmers)
#     with open("week1-4-output.txt", "x") as f2:
#         for key,value in res.items():
#             f2.write(key + ": " + " ".join(value).strip() + "\n")

kmers = ["GAGG", "CAGG", "GGGG", "GGGA", "CAGG", "AGGG", "GGAG"]
res = adjacency_list_debruijn(kmers)
print(kmers)
for key, value in res.items():
    print(key + ": " + " ".join(value))

with open("week1-5.txt") as f:
    kmers = f.read().strip().split(" ")
    res = adjacency_list_debruijn(kmers)
    with open("week1-5-output.txt", "x") as f2:
        for key,value in res.items():
            f2.write(key + ": " + " ".join(value).strip() + "\n")