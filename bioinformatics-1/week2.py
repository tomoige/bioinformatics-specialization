## where skew starts increase is probably the ori
## skew starts increasing when we start losing Cs which means we probably crossed the ori

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