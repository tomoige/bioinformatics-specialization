import math

k = 3 
d= 1
strings = ["ATTTGGC", "TGCCTTA", "CGGTATC", "GAAAATT"]

## generate neighbours from week 2

def generateNeighbours(pattern, d):
    neighbours = set()
    characters = ["A", "C", "T", "G"]
    ## off by one
    for i in range(len(pattern)):
        for j in range(len(characters)):
            neighbours.add(pattern[:i] + characters[j] + pattern[i+1:])

    if d == 1:
        return neighbours
    
    ## off by two
    newNeighbours = set()
    for word in neighbours:
        for i in range(len(word)):
            for j in range(len(characters)):
                newNeighbours.add(word[:i] + characters[j] + word[i+1:])
    
    if d == 2:
        return newNeighbours
    
    ## off by three
    newNeighbours2 = set()
    for word in newNeighbours:
        for i in range(len(word)):
            for j in range(len(characters)):
                newNeighbours2.add(word[:i] + characters[j] + word[i+1:])
    
    return newNeighbours2

## hamming distance from week 2
def hammingDistance(text1, text2):
    count = 0
    for i in range(max(len(text1), len(text2))):
        if i >= (len(text1)) or i >= len(text2):
            count = count + 1
        elif text1[i] != text2[i]:
            count = count + 1
    
    return count

def motifEnumeration(dna, k, d):
    patterns = set()
    neighbours = set()
    for i in range(len(dna[0])- k + 1):
        word = dna[0][i:i+k]
        neighbours.update(generateNeighbours(word, d))
    print("neighbours: ", neighbours)
    for w in neighbours:
        inPattern = True
        for pattern in dna:
            found = False
            for j in range(len(pattern) - k + 1):
                print("comparing ", pattern[j:j+k], " with ", w)
                if hammingDistance(pattern[j:j+k], w) <= d:
                    found = True
                    print("found")
                    break
            if found == False:
                inPattern = False
        if inPattern:
            patterns.add(w)
    return patterns

print(motifEnumeration(strings, k, d))

with open("week3-1.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0])
    d = int(lines[1])
    dna = lines[2].split(" ")
    print(k, d, dna)
    string = ""
    for i in motifEnumeration(dna, k, d):
        string += i + " "
    print(string) 

## computing entropy in a motif matrix
## -(pi log_2(pi) + pi+1 log_2(pi+1)...)

matrix = ["TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"]

def computeEntropy(matrix):
    profile = {
        "A":[],
        "T":[],
        "C":[],
        "G":[]
    }

    for col in range(len(matrix[0])):
        a = 0
        t = 0
        c = 0
        g = 0
        for row in matrix:
            if row[col] == "A": a += 1
            if row[col] == "T": t+= 1
            if row[col] == "C": c+= 1
            if row[col] == "G": g+= 1
        profile["A"].append(a/len(matrix))
        profile["T"].append(t/len(matrix))
        profile["C"].append(c/len(matrix))
        profile["G"].append(g/len(matrix))

    ## calculate entropy
    ## calculated per column
    ## -(pi log_2(pi) + pi+1 log_2(pi+1)...)
    total_entropy_per_col = []
    for col in range(len(matrix[0])):
        total = 0
        if(profile["A"][col] != 0):
            total += profile["A"][col]*math.log2(profile["A"][col])
        if(profile["T"][col] != 0):
            total += profile["T"][col]*math.log2(profile["T"][col])
        if(profile["C"][col] != 0):
            total += profile["C"][col]*math.log2(profile["C"][col])
        if(profile["G"][col] != 0):
            total += profile["G"][col]*math.log2(profile["G"][col])
        total_entropy_per_col.append(-total)
    return(sum(total_entropy_per_col))

print(computeEntropy(matrix))

dna = [
    "TTACCTTAAC",
    "GATATCTGTC",
    "ACGGCGTTCG",
    "CCCTAAAGAG",
    "CGTCAGAGGT"
]

pattern = "AAA"

def motifs(pattern, dna):
    """Returns the motifs minimizing score for a pattern"""
    k = len(pattern)
    motifs = []
    score = 0
    for string in dna:
        mindist = k
        closest_pattern = ""
        for i in range(len(string) - k + 1):
            checking = string[i:i+k]
            dist = hammingDistance(checking, pattern)
            if dist <= mindist:
                mindist = dist
                closest_pattern = checking
        score += mindist
        motifs.append(closest_pattern)
    
    return motifs, score

print(motifs(pattern, dna))

## creating a set of kmers of length k

kmers = set()

def generate_kmers(k, initial_kmer, i):
    """generates all kmers of length k"""
    if(i > k):
        return
    kmers.add(initial_kmer)
    ## places an A in
    new_kmer = initial_kmer[:i] + "A" + initial_kmer[i+1:]
    generate_kmers(k, new_kmer, i+1)
    ## places an T in
    new_kmer = initial_kmer[:i] + "T" + initial_kmer[i+1:]
    generate_kmers(k, new_kmer, i+1)
    ## places an C in
    new_kmer = initial_kmer[:i] + "C" + initial_kmer[i+1:]
    generate_kmers(k, new_kmer, i+1)
    ## places an G in
    new_kmer = initial_kmer[:i] + "G" + initial_kmer[i+1:]
    generate_kmers(k, new_kmer, i+1)

## now finding the median string
dna = [
    "AAATTGACGCAT",
    "GACGACCACGTT",
    "CGTCAGCGCCTG",
    "GCTGAGCACCGG",
    "AGTTCGGGACAG"
]

def median_string(dna, k):
    generate_kmers(k, "A"*k, 0)
    lowest_score = k*len(dna)
    closest_pattern = "A"*k
    for pattern in kmers:
        motifs_score = motifs(pattern, dna)
        if motifs_score[1] < lowest_score:
            # print("testing: " + pattern)
            # print(motifs_score)
            lowest_score = motifs_score[1]
            closest_pattern = pattern
    return closest_pattern

print(median_string(dna, 3))

with open("week3-2.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0])
    dna = lines[1].splitlines()
    print(median_string(dna,k))

## compute probability of a pattern given a profile
matrix = ["TCGGGGGTTTTT",
"CCGGTGACTTAC",
"ACGGGGATTTTC",
"TTGGGGACTTTT",
"AAGGGGACTTCC",
"TTGGGGACTTCC",
"TCGGGGATTCAT",
"TCGGGGATTCCT",
"TAGGGGAACTAC",
"TCGGGTATAACC"]

def compute_profile(dna, pseudocounts=False):
    k = len(dna[0])
    ## pseudocounts makes sure there's at least 1 in each row so it never equals 0
    if pseudocounts:
        profile = {nucleotide: [1] * k for nucleotide in "ACGT"}
        for row in dna:
            for col, nucleotide in enumerate(row):
                profile[nucleotide][col] += 1
        total = len(dna) + 4
        for nucleotide in profile:
            profile[nucleotide] = [count / total for count in profile[nucleotide]]
        return profile

    profile = {
        "A":[],
        "C":[],
        "G":[],
        "T":[]
    }

    for col in range(len(dna[0])):
        a = 0
        t = 0
        c = 0
        g = 0
        for row in dna:
            if row[col] == "A": a += 1
            if row[col] == "T": t+= 1
            if row[col] == "C": c+= 1
            if row[col] == "G": g+= 1
        profile["A"].append(a/len(dna))
        profile["T"].append(t/len(dna))
        profile["C"].append(c/len(dna))
        profile["G"].append(g/len(dna))
    
    return profile

print(compute_profile(matrix))


def compute_probability(pattern, profile):
    probability = 1
    for i in range(len(pattern)):
        probability = probability * float(profile[pattern[i]][i])
    return probability

print(compute_probability("TCGTGGATTTCC", compute_profile(matrix)))

## profile most probable k-mer problem

def profile_most_probable_kmer(text, k, profile):
    highest_probability = -1.0
    highest_probability_pattern = ""
    for i in range(len(text) - k + 1):
        pattern = text[i:i+k]
        probability = compute_probability(pattern, profile)
        if probability > highest_probability:
            highest_probability = probability
            highest_probability_pattern = pattern
    return highest_probability_pattern

text = "ACCTGTTTATTGCCTAAGTTCCGAACAAACCCAATATAGCCCGAGGGCCT"
k = 5
profile = {
    "A": [0.2, 0.2, 0.3, 0.2, 0.3],
    "C": [0.4, 0.3, 0.1, 0.5, 0.1],
    "G": [0.3, 0.3, 0.5, 0.2, 0.4],
    "T": [0.1, 0.2, 0.1, 0.1, 0.2]
}

print(profile_most_probable_kmer(text, k, profile))

with open("week3-3.txt") as f:
    lines = f.read().strip().splitlines()
    text = lines[0]
    k = int(lines[1])
    profile = {
        "A": [float(x) for x in lines[2].split(" ")],
        "C": [float(x) for x in lines[3].split(" ")],
        "G": [float(x) for x in lines[4].split(" ")],
        "T": [float(x) for x in lines[5].split(" ")]
    }
    print(profile_most_probable_kmer(text, k, profile))

    ## greedy motif search

def get_consensus_string(y):
    x = compute_profile(y)
    ## check the highest probability in each column
    ## columns
    consensus_string = ""
    for i in range(len(x["A"])):
        ## rows
        max_prob = 0.0
        max_char = "A"
        for key, value in x.items():
            if value[i] > max_prob:
                max_prob = value[i]
                max_char = key
        consensus_string += max_char
    return consensus_string

def get_score(motifs, consensus_string):
    score = 0
    for string in motifs:
        for i in range(len(string)):
            if string[i] != consensus_string[i]:
                score += 1
    return score


def score_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in "ACGT")
        score += t - max_count
    return score


def greedy_motif_search(k, t, dna, pseudocounts=False):
    best_motif_matrix = [dna[i][0:k] for i in range(len(dna))]
    best_score = score_motifs(best_motif_matrix)

    for i in range(len(dna[0]) - k + 1):
        motif = dna[0][i:i+k]
        current_motif_matrix = [motif]
        profile = compute_profile(current_motif_matrix, pseudocounts=pseudocounts)
        for j in range(1, t):
            most_probable = profile_most_probable_kmer(dna[j], k, profile)
            current_motif_matrix.append(most_probable)
            profile = compute_profile(current_motif_matrix, pseudocounts=pseudocounts)
        score = score_motifs(current_motif_matrix)
        if score < best_score:
            best_score = score
            best_motif_matrix = current_motif_matrix

    return best_motif_matrix

newdna = [
    "GGCGTTCAGGCA", "AAGAATCAGTCA", "CAAGGAGTTCGC", "CACGTCAATCAC", "CAATAATATTCG"
]

# print(greedy_motif_search(3, 5, newdna))  # sample: CAG CAG CAA CAA CAA

USE_PSEUDOCOUNTS = False  # False = basic greedy, True = with pseudocounts step

with open("week3-4.txt") as f:
    lines = f.read().strip().splitlines()
    k, t = map(int, lines[0].split())
    dna = " ".join(lines[1:]).split()

print(" ".join(greedy_motif_search(k, t, dna, pseudocounts=USE_PSEUDOCOUNTS)))

print(" ".join(greedy_motif_search(3, 5, newdna, True)))

with open("week3-5.txt") as f:
    lines = f.read().strip().splitlines()
    k, t = map(int, lines[0].split())
    dna = " ".join(lines[1:]).split()

print(" ".join(greedy_motif_search(k, t, dna, pseudocounts=True)))

def distance_between_pattern_and_string(pattern, dna):
    k = len(pattern)
    distance = 0
    for string in dna:
        hamming_distance = k*len(dna)
        for i in range(len(string) - k + 1):
            cur_pattern = string[i:i+k]
            cur_hamming_distance = hammingDistance(pattern, cur_pattern)
            if hamming_distance > cur_hamming_distance:
                hamming_distance = cur_hamming_distance
        distance = distance + hamming_distance
    return distance

pattern = "AAA"
dna = ["TTACCTTAAC", "GATATCTGTC", "ACGGCGTTCG", "CCCTAAAGAG", "CGTCAGAGGT"]

print(distance_between_pattern_and_string(pattern, dna))

with open("week3-6.txt") as f:
    lines = f.read().strip().splitlines()
    pattern = lines[0]
    dna = lines[1].split(" ")
    print(distance_between_pattern_and_string(pattern, dna))



