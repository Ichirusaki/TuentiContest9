def unfold(punchesList, direction, width, height):
    if direction == "L":
        newPunchesList = [[punchesList[i][0] + width, punchesList[i][1]] for i in range(len(punchesList))]
        newPunchesList.extend([[width - punchesList[i][0] - 1, punchesList[i][1]] for i in range(len(punchesList))])
        punchesList = newPunchesList
        width = width * 2
    elif direction == "R":
        newPunchesList = [[2*width - punchesList[i][0] - 1, punchesList[i][1]] for i in range(len(punchesList))]
        punchesList.extend(newPunchesList)
        width = width * 2
    elif direction == "T":
        newPunchesList = [[punchesList[i][0], punchesList[i][1] + height] for i in range(len(punchesList))]
        newPunchesList.extend([[punchesList[i][0], height - punchesList[i][1] - 1] for i in range(len(punchesList))])
        punchesList = newPunchesList
        height = height * 2
    else:
        newPunchesList = [[punchesList[i][0], 2*height - punchesList[i][1] - 1] for i in range(len(punchesList))]
        punchesList.extend(newPunchesList)
        height = height * 2
    return punchesList, width, height


inputFile = open("submitInput.txt", "r")
outputFile = open("submitOutput.txt", "w")
cases = int(inputFile.readline())

for i in range(cases):
    inputData = inputFile.readline().split()
    width = int(inputData[0])
    height = int(inputData[1])
    folds = int(inputData[2])
    punches = int(inputData[3])
    punchesList = []

    foldsList = [inputFile.readline().strip() for j in range(folds)]

    for j in range(punches):
        arrayReaded = inputFile.readline().split()
        punchesList.append([int(arrayReaded[0]), int(arrayReaded[1])])

    for j in range(len(foldsList)):
        punchesList, width, height = unfold(punchesList, foldsList[j], width, height)

    punchesList.sort()
    
    outputFile.write("Case #{}:\n".format(i+1))
    for j in range(len(punchesList)):
        outputFile.write("{0} {1}\n".format(punchesList[j][0],punchesList[j][1]))
        

inputFile.close()
outputFile.close()
