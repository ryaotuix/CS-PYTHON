import re

def sumValues(dictionary):
    l = dictionary.values()
    return sum(l)

def maxValue(dictionary):
    vals = list(dictionary.values())
    keys = list(dictionary.keys())
    maximum = max(vals)
    i = vals.index(maximum)
    return keys[i]


def numberOfUniqueElements(listOfElements):
    l = list(set(listOfElements))
    return len(l)

def splitStringCount(string):
    string = re.sub(r'\s+', ' ', string)
    l = string.split()
    return len(l)

def isPalindrome(string):
    if len(string)==0:
        return False
    string = string.lower()
    back = -1
    for i in range(len(string)):
        if string[i] != string[back]:
            return False
        back = back-1
    return True

def uniquePalindromes(string):
    string = re.sub(r'\s+', ' ', string)
    string = string.lower()
    words = list(set(string.split()))

    palindromes = []
    for word in words:
        if isPalindrome(word):
            palindromes.append(word)
    palindromes.sort()
    palindromes.reverse()
    return palindromes

def numWords(filename):
    nums = []
    with open(filename) as f:
        for line in f:
            line = f.readline()
            line = re.sub(r'\s+', ' ', line)
            l = line.split()
            number = len(l)
            print(f"{number}\n")
            # nums = nums.append(number)

    return nums



def main():
    numWords("first.txt")

if __name__ == '__main__':
    main()
