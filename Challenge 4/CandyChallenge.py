from math import gcd

inputFile = open("submitInput.txt", "r")
outputFile = open("submitOutput.txt", "w")
cases = int(inputFile.readline())

for i in range(cases):
    entriesSize = int(inputFile.readline())
    entries = list(map(int, inputFile.readline().split()))
    entriesUnique = set(entries)
    multiplier = max(entries)

    for entry in entriesUnique:
        if multiplier % entry != 0:
            multiplier = entry * multiplier

    people = 0
    candies = 0
    
    for entry in entriesUnique:
        person = (entries.count(entry) * multiplier) // entry
        people += person
        candies += (entry*person)

    gcdCandiesPeople = gcd(candies, people)
    people //= gcdCandiesPeople
    candies //= gcdCandiesPeople

    caseString = "Case #{0}: {1}/{2}\n".format(i+1, candies, people)
    print(caseString)
    outputFile.write(caseString)

inputFile.close()
outputFile.close()
