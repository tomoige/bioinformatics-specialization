# ## where skew starts increase is probably the ori
# ## skew starts increasing when we start losing Cs which means we probably crossed the ori

# def findMinimum(text):
#     minVal = 0
#     count = 0
#     for i in range(len(text) + 1):

#         if(i < len(text)):
#             if text[i] == "C":
#                 count = count - 1
#             elif text[i] == "G":
#                 count = count + 1
#         minVal = min(minVal, count)

#     count = 0
#     string = ""
#     for i in range(len(text)):
#         if count == minVal:
#             string = string + str(i) + " "
#         if i < len(text):
#             if text[i] == "C":
#                 count = count - 1
#             elif text[i] == "G":
#                 count = count + 1
#             minVal = min(minVal, count)

#     print(string)

# with open("week2-1.txt") as f:
#     findMinimum(f.read())

## compute hamming distance

def hammingDistance(text1, text2):
    count = 0
    for i in range(max(len(text1), len(text2))):
        if i >= (len(text1)) or i >= len(text2):
            count = count + 1
        elif text1[i] != text2[i]:
            count = count + 1
    
    return count

# text1 = "GGGCCGTTGGT"
# text2 = "GGACCGTTGAC"
# print(hammingDistance(text1, text2))

# with open("week2-2.txt") as f:
#     myList = f.read().strip().split("\n")
#     print(hammingDistance(myList[0], myList[1]))

def approximatePatternMatch(text, pattern, d):
    positions = []
    for i in range(len(text) - len(pattern) + 1):
        if(hammingDistance(text[i: i + len(pattern)], pattern)) <= d:
            positions.append(i)
    return positions

# pattern = "ATTCTGGA"
# text = "CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAAT"

# print(approximatePatternMatch(text, pattern, 3))

with open("week2-3.txt") as f:
    myList = f.read().strip().split("\n")
    pattern = myList[0]
    text = myList[1]
    d = int(myList[2])
    positions = approximatePatternMatch(text, pattern, d)
    print(" ".join(map(str, positions)))