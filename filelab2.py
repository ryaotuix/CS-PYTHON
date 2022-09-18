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
            line = re.sub(r'\s+', ' ', line)
            l = line.split()
            number = len(l)
            nums.append(number)
    return nums

def averageWords(filename):
    l = numWords(filename)
    avg = sum(l)/len(l)
    return avg


def countLines(filename):
    l = 0
    pattern = re.compile(f'\w*ing\w*')
    with open (filename) as f:
        for line in f:
            if (bool(re.search(pattern, line))):
                l += 1
    return l

# Write a function to read text from an input file, find all unique palindromes and return them in
# sorted order.

# findPalindromes(filename) takes as input the file to read the text from, and returns a list of the
# unique palindromes sorted in decreasing lexicographic order (reverse sorted order), in lower case.
# You can use your code above for checking if a string is a palindrome.

# For example,
# filename: palindrome_test.txt
# output: ['tattarrattat', 'redivider', 'detartrated', 'aibohphobia', 'a']


def findPalindromes(filename):
    with open (filename) as f:
        l = f.read()
        return uniquePalindromes(l)
    ###
    ### YOUR CODE HERE
    ###


def main():
    print( countLines('first.txt') )


if __name__ == '__main__':
    main()
