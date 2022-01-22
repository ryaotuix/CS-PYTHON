"""
Author: Harrison Park, park1244@purdue.edu
Assignment: m.n - File Analysis
Date: 11/13/2021

Description:
    read files named xian1 and xian2. Then, from each text file, find the word
    and freqeuncy of the word of each file; print it in a new file.
    Moreover, we should find common words and words that are not common; print
    them in a new file


Contributors:
    Harrison Park, park1244@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [x] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import random as r

def get_list_of_words (filename):
    l = [] # create a list
    with open(filename) as fo:
        for line in fo:
            x = line.lower().strip().split(" ") # create new list splitted by space
            l += x
        for i in range(len(l)):
            l[i] = l[i].strip("!()-[]{};:\,<>./?@#$%^&*_~ \"\' ") # strip punctuations for each object in list
    l = list(filter(lambda string : string.strip(), l)) # get rid of empty object in list
    return l

def get_freqeuncy_of_words(a): # a is get all words
    set_version = sorted(list(set(a)))
    list_of_tuples = [] #[(word, freqeuncy)... ]

    for i in range(len(set_version)):
        word = set_version[i]
        frequency = a.count(word)
        t = (word, frequency)
        list_of_tuples.append(t)
    return list_of_tuples

def frequency_to_file(list_of_tuples, filename):
    with open(filename, 'w') as fo:
        for i in range(len(list_of_tuples)):
            word = list_of_tuples[i][0] # reference the list of tuples in method above
            frequency = list_of_tuples[i][1]
            fo.write(word + ': ' + str(frequency)) # word: frequency
            if i != len(list_of_tuples)-1:
                fo.write('\n')


def list_to_file(list, filename): # used when making a file for common and either
    with open(filename, 'w') as fo:
        for i in range(len(list)):
            fo.write(list[i])
            if i != len(list)-1:
                fo.write('\n')

def main():

    # task for xian 1 file
    xian1 = get_list_of_words('xian_1.txt') # get list of words
    set_xian1 = get_freqeuncy_of_words(xian1) # set of xian1
    frequency_to_file(set_xian1, 'xian_1_word_frequency.txt')
    # task for xian 2 file
    xian2 = get_list_of_words('xian_2.txt')
    set_xian2 = get_freqeuncy_of_words(xian2)
    frequency_to_file(set_xian2, 'xian_2_word_frequency.txt')

    #task for common and either
    xian1_setted = set(xian1)
    xian2_setted = set(xian2)
    words_in_both = xian1_setted & xian2_setted
    all_words = xian1_setted.union(xian2_setted)
    words_in_either = all_words - words_in_both

    list_to_file(sorted(list(words_in_both)), 'common_words.txt')
    list_to_file(sorted(list(words_in_either)), 'eitherbutnotboth.txt')




if __name__ == '__main__':
    # Do not change this part
    main()
