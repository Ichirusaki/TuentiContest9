def getIndexPair(typewriter, character):
    charIndex = typewriter.index(character)
    return charIndex // 10, charIndex % 10

def sustractPair(x, y):
    return (x[0] - y[0]) % 4, (x[1] - y[1]) % 10

def addPair(x, y):
    return (x[0] + y[0]) % 4, (x[1] + y[1]) % 10

inputFile = open("submitInput.txt", "r")
outputFile = open("submitOutput.txt", "w")
cases = int(inputFile.readline())

typewriter = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
              "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P",
              "A", "S", "D", "F", "G", "H", "J", "K", "L", ";",
              "Z", "X", "C", "V", "B", "N", "M", ",", ".", "-"]

indexB = 3, 4
indexG = 2, 4

for i in range(cases):
    writer = inputFile.readline().strip()
    message = inputFile.readline().strip()
    
    swift = 0, 0
    if writer == "B":
        swift = sustractPair(indexB, getIndexPair(typewriter,message[-1]))
    else:
        swift = sustractPair(indexG, getIndexPair(typewriter,message[-1]))
    originalMessage = ""
    for character in message:
        if character != " ":
            charIndex = getIndexPair(typewriter, character)
            charIndex = addPair(charIndex, swift)
            charIndex = (charIndex[0] * 10 + charIndex[1]) % 40
            character = typewriter[charIndex]
        originalMessage += character
    outputFile.write("Case #{0}: {1}\n".format(i+1, originalMessage)) 
        

inputFile.close()
outputFile.close()
