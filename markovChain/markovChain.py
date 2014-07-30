from random import randrange as rand
import sys, getopt

class MarkovChain:
    def __init__(self, textFile, isParagraph):
        text = open(textFile)
        lines = text.readlines()
        wordDict = {}
        if isParagraph:
            lines = [delNonAscii(line) for line in lines]
        else:
            lines = [delNonAscii(line.replace('.', '. [$STOP]')) for line in lines]
        for lineIndex in range(len(lines)):
            splitLine = lines[lineIndex].split()
            if lineIndex < len(lines) - 1 and lines[lineIndex + 1] == ['\n']:
                splitLine.append('[$STOP]')
            for wordIndex in range(len(splitLine)):
                if wordIndex > 0 and wordIndex < len(splitLine) - 1:
                    if splitLine[wordIndex] == '[$STOP]' or splitLine[wordIndex - 1] == '[$STOP]':
                        pass
                    elif splitLine[wordIndex] in wordDict:
                        wordDict[splitLine[wordIndex - 1] + " " + splitLine[wordIndex]] += [splitLine[wordIndex + 1]] 
                    else:
                        wordDict[splitLine[wordIndex - 1] + " " + splitLine[wordIndex]] = [splitLine[wordIndex + 1]]
        self.words = wordDict
        text.close()
        self.rand()

    def rand(self):
        randWordPair = self.getStartingWord()
        return self.createChain(randWordPair, randWordPair)

    def getStartingWord(self):
        randWordPair = self.words.keys()[rand(0,len(self.words.keys()))]
        if randWordPair[0].isupper():
            return randWordPair
        return self.getStartingWord()

    def createChain(self, startWord, chain):
        if startWord == '[$STOP]':
            self.chain = chain
        elif startWord in self.words:
            newWord = self.words[startWord][rand(0,len(self.words[startWord]))]
            if newWord == '[$STOP]':
                self.chain = chain
                return
            chain += ' ' + newWord
            return self.createChain(startWord.split()[1] + ' ' + newWord, chain)
        else:
            self.chain = chain

    def __str__(self):
        return self.chain


def delNonAscii(string):
    return "".join(char for char in string if ord(char)<128)


def main(argv):
    usage = 'Usage: markov.py --input_file=<targetFile> [Optional: -p]'
    try:
        opts, args = getopt.getopt(argv, 'hf:p',['help=', 'input_file='])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    isParagraph = False
    targetFile = None
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print usage
            sys.exit()
        elif opt in ('-f','--input_file'):
            targetFile = arg
        elif opt == '-p':
            isParagraph = True
    if not targetFile:
        print usage
        sys.exit(2)
    markov = MarkovChain(targetFile, isParagraph)
    print markov
    sys.exit()



if __name__ == "__main__":
    main(sys.argv[1:])
