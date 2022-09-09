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
    if len(string)==0:
        return None
    string = re.sub(r'\.', ', ', string)
    # if the period is at the end of string change it to !



def main():


if __name__ == '__main__':
    # Do not change this part
    main()
