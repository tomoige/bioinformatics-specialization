import random

def randomly_select_kmers(k, dna):
    selected_kmers = []
    for string in dna:
        random_idx = random.randint(0, len(dna[0]) - k)
        selected_kmers.append(string[random_idx:random_idx + k])
    return selected_kmers

dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]

print(randomly_select_kmers(4, dna))

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

def compute_probability(profile, string):
    probability = 1
    for i in range(len(string)):
        current_char = string[i]
        probability = probability * profile[current_char][i]
    return probability

def get_motifs(profile, dna, k):
    motifs = []
    for string in dna:
        probability = -1.0
        best_motif = ""
        for i in range(len(string) - k + 1):
            cur_string = string[i:i+k]
            new_prob = compute_probability(profile, cur_string)
            if new_prob > probability:
                probability = new_prob
                best_motif = cur_string
        motifs.append(best_motif)
    return motifs

def score_motifs(motifs):
    k = len(motifs[0])
    t = len(motifs)
    score = 0
    for i in range(k):
        column = [motif[i] for motif in motifs]
        max_count = max(column.count(nucleotide) for nucleotide in "ACGT")
        score += t - max_count
    return score

def randomized_motif_search(dna, k, t):
    best_motifs = randomly_select_kmers(k, dna)
    score_best_motifs = score_motifs(best_motifs)

    while True:

        profile = compute_profile(best_motifs)
        motifs = get_motifs(profile, dna, k)
        score = score_motifs(motifs)

        if score < score_best_motifs:
            score_best_motifs = score
            best_motifs = motifs
        else:
            return best_motifs, score_best_motifs

k = 8
t = 5
dna = ["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

# best_motifs, score_best_motifs = randomized_motif_search(dna, k, t)

# for i in range(10000):
#     if(i % 10 == 0):
#         print("Iteration: ", i+1)
#     cur_motifs, cur_score = randomized_motif_search(dna, k, t)
#     print(cur_score, score_best_motifs)
#     if cur_score < score_best_motifs:
#         best_motifs = cur_motifs
#         score_best_motifs = cur_score

# print("Best motifs are: ", " ".join(best_motifs), " with a score of: ", score_best_motifs)

with open("week4-1.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0].split(" ")[0])
    t = int(lines[0].split(" ")[1])
    dna = lines[1].split(" ")

    best_motifs, score_best_motifs = randomized_motif_search(dna, k, t)

    for j in range(100):
        loops_without_change = 0
        for i in range(1000):
            if(i % 50 == 0):
                print("Iteration: ", j, i+1)
                print(score_best_motifs)
            cur_motifs, cur_score = randomized_motif_search(dna, k, t)
            if cur_score < score_best_motifs:
                best_motifs = cur_motifs
                score_best_motifs = cur_score
                loops_without_change = 0
            else:
                loops_without_change += 1
        
        print("Best motifs are: ", " ".join(best_motifs))
    print("Best motifs are: ", " ".join(best_motifs), " with a score of: ", score_best_motifs)
    