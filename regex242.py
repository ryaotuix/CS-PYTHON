import re
def getWords(sentence, letter):
    l = []
    if len(sentence)==0 or letter=='':
        return l

    print(sentence)
    print(letter)

    sentence = re.split('\s+', sentence)
    pattern = re.compile(f"(?i)^\s*{letter}\s*$|(?i)^\s*{letter}\w*{letter}\s*$")

    for i in range(len(sentence)):
        match = bool(re.match(pattern,sentence[i]))
        if match:
            l.append(sentence[i])
    return l

def removeMultipleSpaces(string):
    string = re.sub(r'\s+', ' ', string) # any white spaces become one space
    return string

def commaConverter(string):
    if not string:
        return None
    string = re.sub(f'\.$', '!', string)
    string = re.sub(r'\.', ', ', string)
    return string
    # if the period is at the end of string change it to !
def findSequence(string):
    strip = re.sub(r'[^\w\s]','',string) # get rid of punctuation and strip string

    alnum_white = re.compile(f'[A-Z]\w+|^[A-Z]\w+$')

    l = re.findall(alnum_white, strip) # find pattern in stripped string

    nl = []
    for i in range(len(l)): # if element in l exists in original string
        if l[i] in string:
            nl.append(l[i])

    if len(nl)==0:
        return None

    nl.sort()

    return nl

def removeZeros(string):
    pattern = re.compile(f'\.0+')
    string = re.sub(pattern,'.',string)
    return string

def findStrings(string):
    pattern = re.compile(f'\w*ly') # words that end with ly

    l = []
    i = 0

    while(True):
        search = re.search(pattern, string)
        if (bool(search) == False): #
            break

        start = search.start()
        end = search.end()
        l.append(f'{start+i}-{end+i}: {string[start:end]}')

        string = string[end:]
        i += end

    result = ', '.join(l) # make list into string with comma

    return result

def main():
    print(findStrings("Clearly, he has no excuse for such behavior.")) #-> 0-7: Clearly
    print(findStrings("The soldier fought bravely and strongly.")) #-> 19-26: bravely, 31-39: strongly
    print(findStrings("The boy happily went to home and gladly completed his assignments.")) #-> 8-15: happily, 33-39: gladly

if __name__ == '__main__':
    # Do not change this part
    main()
