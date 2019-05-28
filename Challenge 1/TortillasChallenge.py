from math import ceil

def howMuchTortillas(nPeople):
    return ceil(nPeople/2)

inputFile = open("submitInput.txt", "r")
outputFile = open("submitOutput.txt", "w")
iterations = int(inputFile.readline())

for i in range(iterations):
    inputLine = inputFile.readline().split()
    withOnion = int(inputLine[0])
    withoutOnion = int(inputLine[1])
    totalTortillas = howMuchTortillas(withOnion) + howMuchTortillas(withoutOnion)
    outputFile.write("Case #{0}: {1}\n".format(i+1, totalTortillas))

inputFile.close()
outputFile.close()
