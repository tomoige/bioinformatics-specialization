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

        profile = compute_profile(best_motifs, pseudocounts = True)
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

def run_randomized_motif_search(dna, k, t, iterations):
    best_motifs, score_best_motifs = randomized_motif_search(dna, k, t)

    for i in range(iterations):
        if(i % 10 == 0):
            print("Iteration: ", i+1)
        cur_motifs, cur_score = randomized_motif_search(dna, k, t)
        print(cur_score, score_best_motifs)
        if cur_score < score_best_motifs:
            best_motifs = cur_motifs
            score_best_motifs = cur_score

    print("Best motifs are: ", " ".join(best_motifs), " with a score of: ", score_best_motifs)

with open("week4-1.txt") as f:
    lines = f.read().strip().splitlines()
    k = int(lines[0].split(" ")[0])
    t = int(lines[0].split(" ")[1])
    dna = lines[1].split(" ")

    # run_randomized_motif_search(dna, k, t, 2000)
    # best_motifs, score_best_motifs = randomized_motif_search(dna, k, t)

    # for j in range(100):
    #     loops_without_change = 0
    #     for i in range(1000):
    #         if(i % 50 == 0):
    #             print("Iteration: ", j, i+1)
    #             print(score_best_motifs)
    #         cur_motifs, cur_score = randomized_motif_search(dna, k, t)
    #         if cur_score < score_best_motifs:
    #             best_motifs = cur_motifs
    #             score_best_motifs = cur_score
    #             loops_without_change = 0
    #         else:
    #             loops_without_change += 1
        
    #     print("Best motifs are: ", " ".join(best_motifs))
    # print("Best motifs are: ", " ".join(best_motifs), " with a score of: ", score_best_motifs)

def pick_random(probabilities):
    sum_probs = sum(probabilities)
    adjusted_probs = [prob/sum_probs for prob in probabilities]

    randomNum = random.uniform(0,1)
    cur_sum = 0
    
    for i in range(len(adjusted_probs)):
        cur_sum += adjusted_probs[i]
        if randomNum <= cur_sum:
            return i
            

print(pick_random([0.1,0.2,0.3]))

## randomly select kmers

def random_kmers(dna, k):
    selected_kmers = [];
    for string in dna:
        random_int = random.randint(0,len(dna[0]) - k)
        selected_kmers.append(string[random_int:random_int + k])

    return selected_kmers

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

# def compute_probability(pattern, profile):
#     probability = 1
#     for i in range(len(pattern)):
#         probability = probability * float(profile[pattern[i]][i])
#     return probability

def profile_randomly_generated_kmer(string, k, profile):
    probabilities = []
    for i in range(len(string) - k + 1):
        probabilities.append(compute_probability(profile, string[i:i+k]))
    index = pick_random(probabilities)
    return string[index:index+k]


def gibbs_sampler(dna, k, t, N):
    kmers = random_kmers(dna, k)
    best_motifs = kmers
    best_score = score_motifs(kmers)
    for j in range(N):
        ## chose which row to remove
        i = random.randint(0,t-1)
        kmers.pop(i)
        profile = compute_profile(kmers, pseudocounts = True)
        ## can escape local optima because sometimes it doesn't choose the most likely kmer
        random_kmer = profile_randomly_generated_kmer(dna[i], k, profile)
        kmers.insert(i, random_kmer)
        score = score_motifs(kmers)
        if score < best_score:
            best_motifs = kmers.copy()
            best_score = score
    return best_motifs, score

dna = [
    "CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA", "GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG", "TAGTACCGAGACCGAAAGAAGTATACAGGCGT", "TAGATCAAGTTTCAGGTGCACGTCGGTGAACC", "AATCCACCAGCTCCACGTGCAATGTTGGCCTA"
]
k = 8
t = 5
best_motifs, best_score = gibbs_sampler(dna, k, t, 200)
for i in range(500):
    if(i%10 == 0):
        print(i, "/", 500)
    motifs, score = gibbs_sampler(dna, k, t, 200)
    if score < best_score:
        best_score = score
        best_motifs = motifs

print(" ".join(best_motifs), best_score)
    
# with open("week4-2.txt") as f:
#     lines = f.read().strip().splitlines()
#     k = int(lines[0].split(" ")[0])
#     t = int(lines[0].split(" ")[1])
#     iterations = int(lines[0].split(" ")[2])
#     dna = lines[1].split(" ")

#     best_motifs, best_score = gibbs_sampler(dna, k, t, 200)
#     for i in range(500):
#         if(i%10 == 0):
#             print(i, "/", iterations)
#         motifs, score = gibbs_sampler(dna, k, t, 200)
#         if score < best_score:
#             best_score = score
#             best_motifs = motifs

#     print(" ".join(best_motifs), best_score)


with open("DosR.txt") as f:
    dna = f.read().strip().splitlines()
    t = len(dna)
    for k in range(8,10):
        run_randomized_motif_search(dna, k, t, 2000)
