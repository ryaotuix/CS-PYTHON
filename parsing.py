def findUniqueWords(filename):
    # tuple 1. number of unique character in the files
    # 2. sort in decreasing lexicographic (alphabetical order)
    # non alphanumeric charcacter should be removed before/ convert to a lower case
    dic = dict()
    with open(filename) as fo:
        s = fo.read()
