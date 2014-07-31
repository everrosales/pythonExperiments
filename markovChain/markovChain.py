from random import randrange as rand
import sys, getopt

class MarkovChain:
    """Basic class for generating Markov Chains from text files. """
    def __init__(self, textFile, isParagraph):
        """Reads input text files and filters out Non Ascii characters. """
        text = open(textFile)
        listTextLines = text.readlines()
        if isParagraph:
            listTextLines = [self.filterText(line) for line in listTextLines]
        else:
            listTextLines = [self.filterText(line.replace('.', '. [$STOP]')) for line in listTextLines]
        self.textLines = listTextLines
        text.close()

    def randChain(self):
        """Generates Markov Chain uses stored textLines. Returns str."""
        wordDict = {}
        for lineIndex in range(len(self.textLines)):
            splitLine = self.textLines[lineIndex].split()
            if lineIndex < len(self.textLines) - 1 and self.textLines[lineIndex + 1] == ['\n']:
                splitLine.append('[$STOP]')
            for wordIndex in range(len(splitLine)):
                if wordIndex > 0 and wordIndex < len(splitLine) - 1:
                    if splitLine[wordIndex] == '[$STOP]' or splitLine[wordIndex - 1] == '[$STOP]':
                        pass
                    elif splitLine[wordIndex] in wordDict:
                        wordDict[splitLine[wordIndex - 1] + " " + splitLine[wordIndex]] += [splitLine[wordIndex + 1]] 
                    else:
                        wordDict[splitLine[wordIndex - 1] + " " + splitLine[wordIndex]] = [splitLine[wordIndex + 1]]
        randWordPair = self.getStartingWord(wordDict)
        return self.createChain(randWordPair, randWordPair, wordDict)

    def getStartingWord(self, wordDict):
        """Randomly select a starting word and ensure that it is Capitalized. """
        randWordPair = wordDict.keys()[rand(0,len(wordDict.keys()))]
        if randWordPair[0].isupper():
            return randWordPair
        return self.getStartingWord(wordDict)

    def createChain(self, startWord, chain, wordDict):
        """Recussively creates chain until hitting a keyword ([$STOP})
            chain str stored in MarkovChain.chain.
            """
        if startWord == '[$STOP]':
            self.chain = chain
        elif startWord in wordDict:
            newWord = wordDict[startWord][rand(0,len(wordDict[startWord]))]
            if newWord == '[$STOP]':
                self.chain = chain
                return
            chain += ' ' + newWord
            return self.createChain(startWord.split()[1] + ' ' + newWord, chain, wordDict)
        else:
            self.chain = chain

    def filterText(self, string):
        """Filters Non Acsii characters. Returns str. """
        return "".join(char for char in string if ord(char)<128)

    def __str__(self):
        """Overrides __str__ to print chain stored in MarkovChain.chain. """
        return self.chain

def main(argv):
    """Random Markov Chain Generator

        Description:
            Takes an input file and returns either a sentence or
            a paragraph of psuedo random text.
            
        Usage:
            -f <fileName>   Specifies input file.
            -h              Help command.
            -p              Indicates whether to return a sentence
                            or a paragraph, "-p" returns a paragraph.
            
            --input_file=<fileName>     Same as "-i", see above.
            --help                      Same as "-h", see above.
        """
    usage = 'Usage: markov.py --input_file=<targetFile> [Optional: -p]'
    try:
        opts, args = getopt.getopt(argv, 'hf:p',['help', 'input_file='])
    except getopt.GetoptError:
        print usage
        sys.exit(2)
    isParagraph = False
    targetFile = None
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print help(main)
            sys.exit()
        elif opt in ('-f','--input_file'):
            targetFile = arg
        elif opt == '-p':
            isParagraph = True
    if not targetFile:
        print usage
        sys.exit(2)
    markov = MarkovChain(targetFile, isParagraph)
    markov.randChain()
    print markov
    sys.exit()



if __name__ == "__main__":
    main(sys.argv[1:])
