def readPlanets(totalPlanets):
    planets = {}
    for i in range(totalPlanets):
        planet = inputFile.readline().split(":")
        planets[planet[0]] = planet[1].strip("\n").split(",")
    return planets

def ImAtNewEarth(planet, planets, totalPaths):
    if planet == "New Earth":
        return totalPaths + 1
    else:
        destinations = planets[planet]
        for i in range(len(destinations)):
            totalPaths = ImAtNewEarth(destinations[i], planets, totalPaths)
        return totalPaths
    


inputFile = open("submitInput.txt", "r")
outputFile = open("submitOutput.txt", "w")
cases = int(inputFile.readline())

for i in range(cases):
    totalPaths = 0
    totalPlanets = int(inputFile.readline())
    planets = readPlanets(totalPlanets)
    totalPaths = ImAtNewEarth("Galactica", planets, totalPaths)
    outputFile.write("Case #{0}: {1}\n".format(i+1, totalPaths))

inputFile.close()
outputFile.close()
