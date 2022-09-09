import re

def findUniqueWords(filename):
    with open(filename) as fo:
        s = fo.read().lower()


    string = re.sub(r'\s+', ' ', s) # any white spaces become one space
    words = string.split()

    for i in range(len(words)):
        words[i] = re.sub(r'\W+', '', words[i])

    uwords = list(set(words))
    uwords.sort() #sort alphabetical

    incidents = []
    for i in range(len(uwords)):
        incident = words.count(uwords[i])
        incidents.append(incident)


    uniqueWords = []
    for i in range(len(uwords)):
        if incidents[i]==1:
            uniqueWords.append(uwords[i])
    num = len(uniqueWords)
    uniqueWords.reverse()


    return ((num, uniqueWords))

def main():

    print(findUniqueWords("first.txt"))


if __name__ == '__main__':
    # Do not change this part
    main()
