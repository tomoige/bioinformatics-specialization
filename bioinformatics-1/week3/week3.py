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

