class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.nextLetter = []
        self.path = []
        
    def addNext(self, nextLetter):
        if nextLetter != self.nextLetter:
            self.nextLetter.append(nextLetter)

    def isLastLetter(self):
        return not self.nextLetter

    def makeAlphabet(self):
        if self.path:
            return self.path
        if self.isLastLetter():
            return [self.letter]
        for letter in self.nextLetter:
            aux = [self.letter]
            aux.extend(letter.makeAlphabet())
            if len(aux) > len(self.path):
                self.path = aux
        return self.path
    
    def __str__(self):
        return self.letter
            
class Alphabet:
    def __init__(self, letter):
        self.firstLetter = [letter]
        self.lastLetter = [letter]
        self.letters = {letter.letter: letter}
        
    def addLetter(self, letter):
        self.letters[letter.letter] = letter

    def getLetter(self, letter):
        if letter in self.letters:
            return self.letters[letter]
        return None
        
    def addFirstLetter(self, firstLetter):
        self.firstLetter.append(firstLetter)
        
    def removeFirstLetter(self, firstLetter):
        if firstLetter in self.firstLetter:
            self.firstLetter.remove(firstLetter)

    def addLastLetter(self, lastLetter):
        self.lastLetter.append(lastLetter)
        
    def removeLastLetter(self, lastLetter):
        if lastLetter in self.lastLetter:
            self.lastLetter.remove(lastLetter)

    def make(self):
        if len(self.firstLetter) > 1 or len(self.lastLetter) > 1:
            return False
        return self.firstLetter[0].makeAlphabet()


inputFile = open("submitInput.txt","r")
outputFile = open("submitOutput.txt","w")

cases = int(inputFile.readline())

for i in range(cases):
    #print(i+1)
    wordsNumber = int(inputFile.readline())
    if wordsNumber == 1:
        word = inputFile.readline().strip()
        if len(set(word)) > 1:
            outputFile.write("Case #{0}: AMBIGUOUS\n".format(i+1))
        else:
            outputFile.write("Case #{0}: {1}\n".format(i+1, word[0]))
    else:
        words = [inputFile.readline().strip() for j in range(wordsNumber)]
        totalCharacters = len(set("".join(words)))
        # Construye un grafo dirigido con las letras
        alphabet = Alphabet(Letter(words[0][0]))
        for j in range(1, wordsNumber):
            before = words[j-1]
            after = words[j]
            k = 0
            while before[k] == after[k] and k < len(before)-1:
                k +=1
            beforeLetter = alphabet.getLetter(before[k])
            if beforeLetter == None:
                beforeLetter = Letter(before[k])
                alphabet.addLetter(beforeLetter)
                alphabet.addFirstLetter(beforeLetter)
            alphabet.removeLastLetter(beforeLetter)
            if before[k] != after[k]:
                afterLetter = alphabet.getLetter(after[k])
                if afterLetter == None:
                    afterLetter = Letter(after[k])
                    alphabet.addLetter(afterLetter)
                    alphabet.addLastLetter(afterLetter)
                alphabet.removeFirstLetter(afterLetter)
                beforeLetter.addNext(afterLetter)

        alphabetList = alphabet.make()
        if not alphabetList or len(alphabetList) < totalCharacters:
            outputFile.write("Case #{0}: AMBIGUOUS\n".format(i+1))
        else:
            outputFile.write("Case #{0}: {1}\n".format(i+1, " ".join(alphabetList)))

inputFile.close()
outputFile.close()
