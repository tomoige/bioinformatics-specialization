# ## where skew starts increase is probably the ori
# ## skew starts increasing when we start losing Cs which means we probably crossed the ori

def findMinimum(text):
    minVal = 0
    count = 0
    for i in range(len(text) + 1):

        if(i < len(text)):
            if text[i] == "C":
                count = count - 1
            elif text[i] == "G":
                count = count + 1
        minVal = min(minVal, count)

    count = 0
    string = ""
    for i in range(len(text)):
        if count == minVal:
            string = string + str(i) + " "
        if i < len(text):
            if text[i] == "C":
                count = count - 1
            elif text[i] == "G":
                count = count + 1
            minVal = min(minVal, count)

    print(string)

with open("week2-1.txt") as f:
    findMinimum(f.read())

## compute hamming distance

def hammingDistance(text1, text2):
    count = 0
    for i in range(max(len(text1), len(text2))):
        if i >= (len(text1)) or i >= len(text2):
            count = count + 1
        elif text1[i] != text2[i]:
            count = count + 1
    
    return count

text1 = "GGGCCGTTGGT"
text2 = "GGACCGTTGAC"
print(hammingDistance(text1, text2))

with open("week2-2.txt") as f:
    myList = f.read().strip().split("\n")
    print(hammingDistance(myList[0], myList[1]))

def approximatePatternMatch(text, pattern, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if(hammingDistance(text[i: i + len(pattern)], pattern)) <= d:
            positions.append(i)
    return positions

pattern = "ATTCTGGA"
text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"

print(approximatePatternMatch(text, pattern, 3))

with open("week2-3.txt") as f:
    myList = f.read().strip().split("\n")
    pattern = myList[0]
    text = myList[1]
    d = int(myList[2])
    positions = approximatePatternMatch(text, pattern, d)
    print(" ".join(map(str, positions)))

# counting the number of times the pattern appears with hamming distance of d or less

def approximatePatternCount(text, pattern, d):
    count = 0
    for i in range(len(text) - len(pattern) + 1):
        if(hammingDistance(text[i: i + len(pattern)], pattern)) <= d:
            count += 1
    return count

pattern = "GAGG"
text = "TTTAGAGCCTTCAGAGG"
d = 2

print(approximatePatternCount(text, pattern, d))

with open("week2-4.txt") as f:
    myList = f.read().strip().splitlines()
    pattern = myList[0]
    text = myList[1]
    d = int(myList[2])
    print(approximatePatternCount(text, pattern, d))

text = "TTTAGAGCCTTCAGAGG"
d = 2

## finding the pattern with most matches
## pattern doesn't have to be in the text that's why we generate neighbours for each pattern in the text

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

def frequentWordsWithMismatch(text, k, d):
    myMap = {}
    max = 0
    string = ""
    for i in range(len(text) - k + 1):
        word = text[i:i+k]
        neighbours = generateNeighbours(word, d)
        for j in neighbours:

            count = approximatePatternCount(text, j, d)
            myMap[j] = count
            if count > max:
                max = count
    for (key,value) in myMap.items():
        if value == max:
            string = string + key + " "
    print(myMap)
    return (string, max)
        
print(frequentWordsWithMismatch(text, 6, 2))

print(generateNeighbours("AAAAA", 1))

with open("week2-5.txt") as f:
    myList = f.read().strip().splitlines()
    text = myList[0]
    k = int(myList[1])
    d = int(myList[2])
    res = frequentWordsWithMismatch(text, k, d)
    print(res[0], res[1])
